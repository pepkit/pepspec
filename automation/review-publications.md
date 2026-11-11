# Review a publications update

This is the second layer of the monthly publications update. A smaller model
followed `automation/update-publications.md` and appended new entries to
`docs/data/publications.yaml` in an open pull request. Check every added entry
yourself and keep only the ones that clearly qualify. Be strict: a wrong entry
sits on a public page, while a missing one is found again next month.

## Steps

1. Read `automation/update-publications.md` (the rules) and
   `publication_sources.yaml` (seeds, `tools`, `exclude_dois`). See what the
   pull request changes:
   `git diff origin/$PR_BASE -- docs/data/publications.yaml`.
2. Load the old file (`git show origin/$PR_BASE:docs/data/publications.yaml`)
   and the new one with PyYAML and compare them by DOI. Every old entry must
   still be there with exactly the same fields. Any entry whose DOI is not in
   the old file is an added entry. Restore any old entry that was changed or
   removed. (Step 4 lets you change an old entry in one case.)
3. Check each added entry. Save every API response under `/tmp/pubsearch/`
   before you read it, as the procedure does, and do not rely on search
   snippets or memory.
   - **The DOI resolves.** Look it up on Crossref
     (`https://api.crossref.org/works/<doi>`), then DataCite or `doi.org` as in
     step 7 of the procedure.
   - **The evidence is true.**
     - `cites:<seed-doi>`: the seed is listed under `seeds`, and the paper
       really cites it. Its OpenAlex record
       (`https://api.openalex.org/works/doi:<doi>?select=id,referenced_works&mailto=nsheff@databio.org`)
       must list the seed's `openalex` id, or its Crossref `reference` list
       must contain the seed DOI.
     - `fulltext:<id>`: open the Europe PMC full text
       (`https://www.ebi.ac.uk/europepmc/webservices/rest/<PMCID>/fullTextXML`,
       using the paper's PMC id) and find the passage. The tool must be used as software, in Methods,
       Code Availability or Data Availability, as step 6 requires. A passing
       mention, another meaning of the word, or an unclear match fails.
   - **It passes the filters in step 5.** Not in `exclude_dois`, not
     retracted, not a correction, editorial or erratum.
   - **It is not already listed.** Its DOI and `preprint_doi` are not among the
     old file's `doi` or `preprint_doi` values (lowercased), and its normalized
     title (lowercase, letters and digits only) matches no old title. It is
     not the preprint or the published version of an entry already listed:
     check Crossref's `relation` field (`has-preprint`, `is-preprint-of`) and
     look for near-identical titles. Two added entries must not be one work.
   - **The fields are right** (step 10 of the procedure), checked against
     Crossref: bare lowercase `doi`; plain-text `title` that matches the
     paper; `authors` as `<first surname> et al.` for three or more authors,
     `<A> and <B>` for two, or the surname for one; `year`; `journal` (left
     out for an unpublished preprint); a correct `preprint_doi` if present;
     `tools` left `[]` unless the evidence shows which tool was used; the
     `evidence` value; and `added` set to the run date.
4. Edit `docs/data/publications.yaml`:
   - If an added entry and an old entry are the same work (one is the
     preprint of the other), keep only the old entry and make it the
     published version: take its `doi`, `title`, `year` and `journal` from
     the published version's Crossref record, put the preprint's DOI in
     `preprint_doi`, and keep its `tools`, `evidence` and `added`. Then delete
     the added entry. Re-sort if the year changed. With both DOIs on the
     list, the search will not propose the work again.
   - Delete every other added entry that fails the DOI, evidence, filter, or
     duplicate check, and add its DOI to the end of `exclude_dois` in
     `publication_sources.yaml`, with a short comment giving the reason. The
     search skips those DOIs, so it will not propose them again.
   - For an entry that qualifies but has a wrong field, fix the field from the
     Crossref record.
   - Do not add new entries. Keep the sort order and the YAML style.
5. Write `/tmp/review.md`: one summary sentence, then a table with each added
   entry (DOI as a link and a short title), keep, fix, or remove, the reason,
   and the sources you opened. Name any old entry you changed and any DOI
   you added to `exclude_dois`.

When you finish, a hook re-runs `python validate_publications.py --check-dois`,
commits your changes, and posts your review on the pull request. A person then
merges it. If the pull request no longer changes anything, the hook closes
it. If the check fails, it tells you what to fix. Never commit, push, comment
on, merge, or close the pull request yourself.
