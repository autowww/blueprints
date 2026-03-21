Review current code and tests against a spec's acceptance criteria.

1. Ask for the **work-unit ID** (e.g. `M1E1S1` or issue `#N`) if not provided.
2. Read the spec file under `docs/requirements/` to extract acceptance criteria.
3. Search the codebase for the implementation — find relevant source files and tests.
4. Compare each acceptance criterion against the implementation:
   - Is it implemented?
   - Is it tested?
   - Are there edge cases the spec mentions that the code doesn't handle?
5. Report:
   - **Covered**: criteria that are implemented and tested
   - **Partially covered**: implemented but not tested, or missing edge cases
   - **Missing**: criteria not yet addressed
   - **Suggestions**: improvements or gaps not in the spec
