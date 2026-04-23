---
name: build-versona-handoff
description: >
  Produce a machine-readable handoff (handoff.json) plus human summary so the next Versona
  or human knows required inputs and artifact paths.
---

# Build Versona handoff (Forge)

## When to use

- End of a session that **continues** in another discipline or actor.
- After §5 when **Suggested next Versonas** should be backed by **paths**, not only chat text.

## Steps

1. **Summarize** — One short paragraph: conclusion, open concerns, recommended next lens.
2. **List artifacts** — Repo-relative paths: §5 file, specs read, recipe `run.log`, screenshots, etc.
3. **Write `outputs/handoff.json`** — Validate against [`handoff-payload.schema.json`](../../../../methodologies/forge/schemas/handoff-payload.schema.json): required `summary`, `artifact_paths`, `created_at`; optional `open_concerns` with severities from [`VERSONA-FRAMEWORK.md`](../../../../methodologies/forge/versona/VERSONA-FRAMEWORK.md) §4.1.
4. **Link in SESSION.md** — Point to `outputs/handoff.json` and target Versona or human owner.
5. **Downstream** — Next session’s **`inputs/`** may copy or symlink (team policy); at minimum reference paths in the new `SESSION.md`.

## Output shape (human index in SESSION.md)

```markdown
## Handoff

- **Payload:** outputs/handoff.json
- **Next:** @versona-… (reason)
```

## Install

Copy to **`.cursor/skills/build-versona-handoff/`**.

## References

- [`ARTIFACT-CONTRACTS.md`](../../../../methodologies/forge/versona/ARTIFACT-CONTRACTS.md) §2 examples
