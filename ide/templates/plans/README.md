# Plan convention

## What a plan is

A **plan** is a short-lived markdown artifact created before implementing a multi-file or unfamiliar change. It bridges the gap between the **spec** (durable intent with acceptance criteria) and the **implementation** (code and tests).

Plans are **not** durable specs — they are session artifacts that guide implementation and are discarded or archived after the work is merged.

## When to create a plan

- **Multi-file changes** — touching 3+ files or multiple system boundaries.
- **Unfamiliar code** — areas you haven't worked in before.
- **Complex logic** — non-obvious algorithms, data migrations, security-sensitive changes.
- **Uncertain approach** — multiple valid strategies with tradeoffs to evaluate.

## When to skip

- **Single-file fixes** — typos, config tweaks, log line additions.
- **Well-known patterns** — following an established template in the codebase.
- **Trivial changes** — the diff is describable in one sentence.

## Where plans live

- **`.cursor/plans/`** — Cursor native (typically gitignored). Plans saved from Plan Mode go here automatically.
- **`docs/plans/`** — alternative if the team wants plans in git history for audit or reference.

## Naming convention

`<work-unit-id>-<short-title>.md`

Examples:
- `M1E1S1-google-auth-callback.md`
- `42-fix-session-timeout.md`

## Lifecycle

1. **Create** — during plan mode or at the start of a task. Reference the work-unit ID and spec.
2. **Review** — team or self-review the approach before implementing.
3. **Use** — follow the plan during implementation; update it if the approach changes.
4. **Discard or archive** — after the work is merged, delete the plan or move to an archive. Plans are not meant to be maintained long-term.

## Template

See [`PLAN.template.md`](PLAN.template.md) for the plan file template.
