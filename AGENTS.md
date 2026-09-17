# Agent instructions

## Publications update

For any task that discovers or updates the PEPkit publications list, read and
follow `automation/update-publications.md` completely.

For Jules runs:

- Let Jules manage its own working branch and pull request publication.
- Do not run `gh pr create`, `git push`, or other manual PR-publication steps.
- Before making changes, check whether an open pull request labeled
  `publications` already exists. If one exists, make no changes and stop; the
  fixed lookback window in the canonical procedure will rediscover anything
  still missing on a later run.
- If no new verified publications qualify, make no repository changes.
- Never merge the resulting pull request automatically.
