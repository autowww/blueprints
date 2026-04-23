---
name: merge-parallel-versona-results
description: >
  Merge multiple §5-shaped or tasklet outputs from parallel Versona passes into one table:
  dedupe concerns, unify severity, single top-level recommendation.
---

# Merge parallel Versona results (Forge)

## When to use

- **Family aggregators**, **routing** meta-pass, or **multi-discipline** review on the same work item.
- After **parallel** `@versona-*` invocations (or repeated tasklet runs) need **one** report.

## Steps

1. **Collect inputs** — Paths to each `outputs/section5-*.md`, tasklet blocks, or pasted sections; note **discipline** and **session_id** per source.
2. **Normalize severities** — Only **critical** / **significant** / **minor** ([`VERSONA-FRAMEWORK.md`](../../../../methodologies/forge/versona/VERSONA-FRAMEWORK.md) §4.1).
3. **Merge concerns** — Union rows; **dedupe** same root cause; keep **highest** severity if duplicates conflict.
4. **Standards traceability** — If any child block included §5.1, **merge** `standards_*` fields or summarize conflicts once ([`VERSONA-CONTRACT.md`](../../../../methodologies/forge/versona/VERSONA-CONTRACT.md) §5.1 note for aggregators).
5. **Single recommendation** — Exactly one of **Proceed** / **Proceed with conditions** / **Rework** / **Bank** ([`VERSONA-FRAMEWORK.md`](../../../../methodologies/forge/versona/VERSONA-FRAMEWORK.md) §4.2); if children disagree, state **conditions** explicitly.
6. **Write** — `outputs/MERGED-REPORT.md` or replace parent session’s primary §5 file; optional `outputs/merge-notes.md` for traceability.

## Rules

- Do **not** silently drop **critical** items; escalate or flag **human gate**.

## Install

Copy to **`.cursor/skills/merge-parallel-versona-results/`**.

## References

- Tasklet: **`@forge-tasklet-merge-outputs`** (mechanical combine)
- [`VERSONA-SKILL-MATRIX.md`](../../../../methodologies/forge/versona/VERSONA-SKILL-MATRIX.md) — aggregators & routing
