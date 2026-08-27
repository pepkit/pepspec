---
name: update-publications
description: Search OpenAlex and Europe PMC for new papers that cite or use PEPkit tools, verify them, append them to docs/data/publications.yaml, and open a pull request. Use for the monthly publications update.
---

# Update the PEPkit publications list

Search the literature for new papers that cite or use PEPkit tools, append the
verified ones to `docs/data/publications.yaml`, and open a pull request.

The statistics page at <https://pep.databio.org/statistics/> renders that YAML
file at build time. Everything you add lands on a public page, so the bar for
including an entry is "I read this DOI out of an API response and I can say why
it qualifies" — not "it looked relevant".

## Process

### 1. Read state

Read `publication_sources.yaml` (repo root) and `docs/data/publications.yaml`.

From `publication_sources.yaml` you need: `lookback_months`, `max_new_per_run`,
`tools`, `seeds`, `fulltext_queries`, `banned_queries`, `exclude_dois`.

Build two dedup sets from the existing data file:

- **DOI set** — every `doi` and every `preprint_doi`, lowercased.
- **Title set** — every `title`, normalized by lowercasing and stripping every
  non-alphanumeric character. This is what catches a preprint and its published
  version, whose DOIs differ but whose titles do not.

Add every DOI in `exclude_dois` to the DOI set.

There is deliberately **no `last_run` field**. The search always uses a fixed
`lookback_months` window and relies on these dedup sets to discard what is
already listed. A moving cursor breaks the moment a PR sits unmerged for a
month; a fixed window plus dedup is self-healing.

### 2. Set up a scratch directory

```bash
mkdir -p /tmp/pubsearch
```

**Every API response gets written to a file in `/tmp/pubsearch` before anything
is read out of it. This is the anti-hallucination mechanism.** A DOI, title,
author, or year that is not present in one of those saved files does not go
into the YAML. No exceptions.

Compute the window once:

```bash
LOOKBACK=18  # read this from publication_sources.yaml
FROM=$(date -u -d "${LOOKBACK} months ago" +%Y-%m-%d)
TODAY=$(date -u +%Y-%m-%d)
```

### 3. Channel A — citations (OpenAlex)

Primary channel. The statistics page describes this section as "publications
that reference PEP manuscripts", so a citation of a seed paper is the
historically correct criterion and is self-justifying.

For each entry in `seeds`, using its `openalex` id:

```bash
curl -s "https://api.openalex.org/works?filter=cites:${OPENALEX_ID},from_publication_date:${FROM}&per-page=200&cursor=*&select=id,doi,title,publication_year,publication_date,authorships,primary_location,type,is_retracted&mailto=nsheff@databio.org" \
  -o /tmp/pubsearch/cites_${OPENALEX_ID}_1.json
```

Paginate: read `meta.next_cursor` from the response and re-issue the request
with `cursor=<that value>`, incrementing the file suffix, until `next_cursor`
is null.

Always send `mailto=nsheff@databio.org`. It is what keeps the request in
OpenAlex's polite pool; without it the API rate-limits hard.

The `doi` field comes back as a `https://doi.org/...` URL. Strip the prefix and
lowercase it before comparing or writing.

Record the evidence value for each survivor as `cites:<seed-doi>` — the seed's
`doi` from `publication_sources.yaml`, not its OpenAlex id.

### 4. Channel B — full-text mention (Europe PMC)

Secondary channel, and the only one that finds a paper that *uses* a tool
without citing anything. Europe PMC indexes open-access full text, so
Methods-section tool mentions are searchable.

For each entry in `fulltext_queries`:

```bash
Q=$(python3 -c 'import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1]))' "$QUERY AND FIRST_PDATE:[$FROM TO $TODAY]")
curl -s "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=${Q}&format=json&pageSize=100&cursorMark=*&resultType=core" \
  -o /tmp/pubsearch/epmc_${N}.json
```

Paginate with `nextCursorMark` until it stops changing.

Record the evidence value for each survivor as `fulltext:<europepmc-id>` — the
`id` field from the result (e.g. `fulltext:PMC10312938`).

### 5. Filter

Drop a candidate if **any** of these is true:

- its DOI is already in the dedup set (which includes `exclude_dois`)
- its normalized title matches an existing entry — this is the preprint /
  published catch
- `is_retracted` is true, or the title starts with `Retracted:`, `Withdrawn:`,
  or `Correction:`
- `type` is `paratext`, `editorial`, or `erratum`
- it has no DOI at all

### 6. Judge the Channel B hits

A citation is self-justifying. A full-text hit is not.

For each Channel B survivor, fetch the matching passage and confirm the tool
name is being used **as software** — a Methods, Code Availability, or Data
Availability mention. Europe PMC's `textMinedTerms` and the full-text endpoint
(`.../{source}/{id}/fullTextXML`) both help here.

This step exists because bare tool-name searches are catastrophically noisy:
`"peppy"` returns psychology papers about autism first-responder training and
yoga posture studies, and `"pepkit"` returns peptide-chemistry papers about
"glycoreplica peptides". That is why those terms are in `banned_queries` and
why every remaining full-text hit needs a human-readable justification.

If the snippet is ambiguous, **drop it**. Under-inclusion is cheap. A wrong
entry on a public page is not.

### 7. Verify every DOI

Before writing anything, resolve each surviving DOI:

```bash
curl -s -o /tmp/pubsearch/doi_check.json -w "%{http_code}" "https://api.crossref.org/works/${DOI}"
# on 404:
curl -s -o /tmp/pubsearch/doi_check.json -w "%{http_code}" "https://api.datacite.org/dois/${DOI}"
# on 404 there too:
curl -sIL -o /dev/null -w "%{http_code}" "https://doi.org/${DOI}"
```

Anything other than a 2xx/3xx from the last step means the DOI is dropped. Do
not guess at, repair, or invent a DOI.

Crossref is also the right place to read the canonical `title`, `journal`
(`container-title`), and `publication_year` from, when the search response's
values look truncated or mangled.

### 8. Handle preprint / published pairs

If both a preprint and its published version survive, keep **the published
one** and record the preprint's DOI in that entry's `preprint_doi` field. Do
not add two entries for one work.

### 9. Cap

If more than `max_new_per_run` candidates survive, keep the most-cited ones
(OpenAlex `cited_by_count`) and note the truncation in the PR body. The next
monthly run picks up the rest — the fixed lookback window guarantees nothing is
lost.

### 10. Write

Append entries to `docs/data/publications.yaml`, then re-sort the whole list by
year descending, then by author. Preserve the file's comment header and match
the existing indentation and block-scalar (`>-`) style.

Field rules:

- `doi` (**required**) — bare DOI, lowercase, no `https://doi.org/` prefix.
- `title` (**required**) — plain text. No HTML entities; the renderer escapes.
- `authors` (**required**) — a display string, not a list. Derive it as
  `<first author surname> et al.` for three or more authors, `<A> and <B>` for
  exactly two, and the bare surname for one. This matches the existing entries.
- `year` (**required**) — integer.
- `journal` (optional) — omit entirely for unpublished preprints.
- `preprint_doi` (optional) — see step 8.
- `tools` (optional) — values from the `tools` vocabulary in
  `publication_sources.yaml`. Leave it `[]` unless you actually know which tool
  was used.
- `evidence` (**required**) — `cites:<seed-doi>` or `fulltext:<europepmc-id>`,
  as recorded in step 3 or 4.
- `added` (**required**) — today's ISO date.

### 11. Validate

```bash
python validate_publications.py --check-dois
```

If it fails, fix the data and re-run. **Do not open a PR on a failing
validator.**

### 12. Commit and open a PR

First check whether the bot already has an open PR:

```bash
gh pr list --label publications --state open --json number,headRefName
```

If one exists, check out that branch and push to it rather than opening a
second PR. Otherwise:

```bash
git checkout -b publications-update-$(date -u +%Y-%m)
git add docs/data/publications.yaml
git commit -m "Add N publications citing PEPkit tools"
git push -u origin publications-update-$(date -u +%Y-%m)
gh pr create --label publications --label needs-review \
  --title "Add N publications citing PEPkit tools" --body "..."
```

The PR body must contain:

1. **A table of every added entry** — authors, year, title, journal, the DOI as
   a link, and the `evidence` value.
2. **A section listing candidates that were found and rejected**, each with its
   reason (already listed, retracted, ambiguous full-text match, DOI did not
   resolve, ...).

That rejection list is what makes the PR reviewable. It is how a human catches
a filter that has become too aggressive. Do not omit it.

### 13. If nothing new is found

Create no branch and no PR. Report "no new publications" and stop.

## Important rules

- **Never write a DOI you did not read out of a saved API response file.** If it
  is not in `/tmp/pubsearch/*.json`, it does not go in the YAML.
- **Never search for a term in `banned_queries`.** They are ordinary English
  words. They return garbage.
- **Never modify an existing entry.** This job only appends.
- **Never touch `docs/statistics.md`.** The page renders from the YAML now;
  editing the markdown is always a mistake.
- **Never merge the PR.** A human reviews every one.
- **When in doubt, exclude.** A missing paper is fixed next month. A wrong one
  is on a public page until someone notices.
- **Preserve YAML formatting.** Match the indentation and block-scalar style
  already in the file.
