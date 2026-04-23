---
name: record-versona-event
description: >
  Record a Forge decision or session event: Ember Log vs SESSION.md vs optional graph JSONL,
  without duplicating long policy in the Versona rule.
---

# Record Versona event (Forge)

## When to use

- **Trade-off, risk acceptance, scope change, or waiver** → prioritize **Ember Log**.
- **Session progress, links, artifact list** → **SESSION.md** body or frontmatter pointers.
- **Automation / analytics** (optional) → append **`forge-logs/versona-track/`** JSONL per operating model.

## Steps

1. **Classify the event**
   | Kind | Primary sink |
   |------|----------------|
   | Decision / why we chose X | `ember-logs/YYYY-MM-DD.md` via `forge-ember.sh` |
   | “What we did” in-session | `SESSION.md` + `outputs/` |
   | Intake / routing audit | `request-ledger.jsonl` (optional) |
2. **Ember Log** — From repo root: `./blueprints/sdlc/methodologies/forge/scripts/forge-ember.sh "summary"` (or project wrapper). Keep entries **decision-shaped**, not full transcripts.
3. **SESSION.md** — Short dated bullets or links to `outputs/` files; keep large text in `outputs/` or gitignored `transcript.md`.
4. **Optional manifest** — Update `artifact-manifest.json` when recipe outputs are consumed ([`artifact-manifest.schema.json`](../../../../methodologies/forge/schemas/artifact-manifest.schema.json)).

## Rules

- One **canonical** home per fact: avoid pasting the same paragraph in Ember Log and journal; **cross-link** paths instead.

## Install

Copy to **`.cursor/skills/record-versona-event/`**.

## References

- [`daily/README.md`](../../../../methodologies/forge/daily/README.md)
- Tasklet: **`@forge-tasklet-log-event`**
