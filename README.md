# pepspec

This repository holds the **PEP specification**, the site's own pages (home,
citations, statistics) and the **PEPkit publications list**. All are published
on [pep.databio.org](https://pep.databio.org).

The site itself is built by `databio/doc-hubs` (hub `hubs/pepkit`). Each PEPkit
tool keeps its own docs in its own repository (`docs/` plus `docs/docs.yml`),
and the hub pulls them all in at build time. Edit a page in the repository that
owns it:

| Pages | Repository |
|---|---|
| `/spec/...` | this repo, `docs/spec/` |
| `/data/publications.yaml`, the list on `/statistics/` | this repo, `docs/data/publications.yaml` |
| `/eido/`, `/geofetch/`, `/looper/`, `/pephub/`, `/peppy/`, `/pipestat/` | `pepkit/<tool>`, `docs/` |
| `/pephubclient/`, `/pepdbagent/`, `/geopephub/`, `/ubiquerg/` | `pepkit/<tool>`, `docs/` |
| `/pypiper/`, `/yacman/` | `databio/<tool>`, `docs/` |
| home page, `/citations/`, `/statistics/` | this repo, `docs/site/` |

The navigation for the specification is `docs/spec/docs.yml`. `docs/site/` is
mounted at the site root: `index.mdx` is the home page, and its `docs.yml` lists
the citations and statistics pages. Those are `.mdx` pages (Markdown that can
use components); `statistics.mdx` imports the publications list component from
the hub. A push to `master` that touches `docs/spec/`, `docs/site/` or
`docs/data/` tells the hub to rebuild the site
(`.github/workflows/notify-docs-*.yml`).

## Automated publications list

The "Publications that use PEPkit" section of the statistics page renders from
`docs/data/publications.yaml` when the site is built. The same file is published
as machine-readable data at <https://pep.databio.org/data/publications.yaml>.

The recurring publications search is designed to run as a Jules scheduled task.
Its canonical, agent-neutral procedure lives in `automation/update-publications.md`,
with Jules-specific guidance in `AGENTS.md`. The search uses OpenAlex for papers
citing the PEP manuscripts and Europe PMC for full-text mentions of the tools,
then appends only verified new entries to the YAML. The bot never modifies an
existing entry and never merges its own PR — a human reviews every one. Its
search configuration (seed papers, queries, tool vocabulary) is in
`publication_sources.yaml` at the repo root.

`.github/workflows/scheduled-publications-update.yml` is retained as a manual
`workflow_dispatch` fallback for running the same procedure with Claude Code;
it is no longer scheduled.

`.github/workflows/validate-publications.yaml` runs `validate_publications.py`
on every PR that touches this data: structural checks always, plus DOI
resolution for entries that are new in that PR.

To add a paper by hand, add an entry to `docs/data/publications.yaml` with
`evidence: manual` and today's date in `added`, then run
`python validate_publications.py --check-dois`.
