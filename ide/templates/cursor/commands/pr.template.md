Create a pull request for the current changes.

1. Run `git diff` to see staged and unstaged changes.
2. Identify which **work-unit IDs** (e.g. `M1E1S1`, `#123`) the changes relate to.
3. Write a commit message with the work-unit reference in the subject (e.g. `Refs M1E1S1 — add OAuth callback handler`).
4. Stage relevant files, commit, and push to the current branch.
5. Use `gh pr create` to open a pull request with:
   - **Title**: work-unit ref + concise description
   - **Body**: summary of changes, work-unit IDs covered, link to specs under `docs/requirements/` if applicable
6. Return the PR URL when done.
