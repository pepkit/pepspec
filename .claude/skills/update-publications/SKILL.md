---
name: update-publications
description: Run the recurring PEPkit publications discovery and update procedure.
---

# Update the PEPkit publications list

Follow `automation/update-publications.md` completely.

For Claude Code runs only:

- If there is already an open pull request labeled `publications`, update that
  branch instead of opening a second PR.
- Otherwise, create a branch named `publications-update-YYYY-MM`, commit the
  changes, push it, and open a pull request labeled `publications` and
  `needs-review`.
- Never merge the pull request.
- If the canonical procedure finds no qualifying new publications, create no
  branch and no pull request.
