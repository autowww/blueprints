---
name: plan-and-verify
description: Plan-first workflow with verification contract for multi-file or unfamiliar changes.
---

# Plan-first workflow

For multi-file changes, unfamiliar code, or complex logic:

1. **Explore** — use Plan Mode. Read files and understand codebase context before writing code.
2. **Plan** — create a detailed implementation plan: approach, files to change, verification strategy. Reference the work-unit ID.
3. **Implement** — switch to Normal Mode. Work through the plan systematically in small batches.
4. **Verify** — run the project's test/lint/build commands. Failing tests or unmet acceptance criteria are the stop signal.
5. **Commit** — with work-unit reference (`Refs M1E1S1`) and clear message.

Skip the plan for single-file fixes or trivial changes describable in one sentence.

## Verification contract

- After changes, always run tests if the project has them.
- Check that acceptance criteria from the spec are met.
- If you cannot verify, say so explicitly.

## Session hygiene

- Use `/clear` between unrelated tasks.
- For large investigations, delegate to subagents to keep the main context focused.
- After two failed corrections, `/clear` and start fresh with a better prompt.
