# Agent instructions

## Publications update

For any task that discovers or updates the PEPkit publications list, read and
follow `automation/update-publications.md` completely. To review a proposed
update, follow `automation/review-publications.md`.

The update runs monthly as the GitHub Actions workflow
`.github/workflows/scheduled-publications-update.yml`. Claude Haiku proposes
new entries; when it finishes, a hook (`automation/publish-pr.sh`) checks them,
commits them, and opens a pull request. Claude Opus then reviews that pull
request, and a person merges it. Never create a branch, commit, push, open a
pull request, or merge one yourself.
