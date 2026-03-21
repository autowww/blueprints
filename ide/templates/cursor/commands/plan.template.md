Create a plan for implementing a work unit.

1. Ask for the **work-unit ID** (e.g. `M1E1S1` or issue `#N`) if not provided.
2. Read the spec file under `docs/requirements/` (or fetch the issue) to understand acceptance criteria.
3. Explore the codebase to find relevant files using search tools.
4. Create a plan file at `.cursor/plans/<work-unit-id>-<short-title>.md` with:
   - **Context**: spec link, acceptance criteria summary
   - **Approach**: what will change and why, key design decisions
   - **Files to change**: checklist of files and what changes in each
   - **Verification**: which tests to run or write, lint/build commands, manual checks
   - **Status**: checkboxes for plan reviewed / implementation complete / verification passed
5. Present the plan for review before implementing.
