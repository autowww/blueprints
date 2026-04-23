# AGENTS — Forge SDLC (markdown-canonical)

This repository uses **Forge SDLC** with **Markdown-only** canonical artifacts: planning, traceability, estimates, defects, and import ledgers are **`.md`** (tables, front matter, links)—**not** CSV or spreadsheets as system of record.

## Repo layout (typical)

| Area | Path | Notes |
|------|------|--------|
| Blueprints (read-only) | `blueprints/` | Submodule — **framework only**; do **not** commit project history here |
| Forge daily | `forge/charge.md`, `forge/journal/`, `ember-logs/` | Stock Charge path; optional `forge/current/*` **only** if documented below |
| Requirements | `docs/requirements/` | `INDEX.md`, `WBS.md`, `ESTIMATES.md`, `TRACEABILITY.md`, `milestones/…` |
| Roadmap | `docs/ROADMAP.md` | Optional roll-up |
| Defects | `docs/defects/` | `INDEX.md`, `DEF-NNNN/defect.md`, `rca.md`, `test-impact.md` |
| Testing trace | `docs/testing/TRACEABILITY.md` | **Optional** — omit if all test links live in `docs/requirements/TRACEABILITY.md` |
| Cursor import | `imports/cursor-history/` | `raw/`, `normalized/`, `SCHEMA-NOTES.md`, `IMPORT-LEDGER.md` |
| Estimation rules | `forge/estimation/ESTIMATION-RULES.md` | Method standard; ledger in `docs/requirements/ESTIMATES.md` |
| Versona sessions | `forge-logs/versona/<actor>/<session-id>/` | §5 outputs, handoffs |

**Path aliases:** If this repo uses `forge/current/ITERATION.md` or `forge/current/CHARGE.md` instead of `forge/charge.md`, that choice is recorded in **`docs/PROJECT.md`**. Agents default to **`forge/charge.md`** for alignment with `forge-charge.sh`.

## Forge naming (do not conflate)

- **Ore** — raw intake  
- **Product Spark** — coarse **product / release** slice (PoC, MVP, phase)  
- **Ingot** — refined, plannable (often story-level)  
- **Forge Spark** — smallest **delivery** task (~1–4 h), often `M{n}E{n}S{n}T{n}`  
- **Forge iteration** — timeboxed delivery cycle  
- **Charge** — today’s selected Forge Sparks  
- **Ember Log** — decision memory  
- **Assay** — evidence-based release gate  

**Product Spark** and **Forge Spark** are **not** synonyms.

Full lexicon: `blueprints/sdlc/methodologies/forge/NAMING-REFERENCE.md`.

## Where work is tracked

- **Backlog / WBS:** `docs/requirements/WBS.md` + milestone tree  
- **Cross-links:** `docs/requirements/TRACEABILITY.md`  
- **Sizing:** `docs/requirements/ESTIMATES.md` + per-item front matter (`est_fib`, `est_tshirt`, `est_tokens`, …)  
- **Today’s execution:** `forge/charge.md` (or alias in `docs/PROJECT.md`)

## Defects

- Registry: `docs/defects/INDEX.md`  
- Per defect: `docs/defects/DEF-NNNN/defect.md`, `rca.md`, `test-impact.md`  
- Link defects to requirement / Spark ids in `TRACEABILITY.md`

## Estimation

- Rules: `forge/estimation/ESTIMATION-RULES.md`  
- Ledger + calibration: `docs/requirements/ESTIMATES.md`  
- **PM** owns **commitments**; **Estimation** method / roll-up questions → **`versona-estimation`** when installed

## Versonas

- Installed Cursor rules: `.cursor/rules/versona-*.mdc`, `forge-*.mdc`  
- Routing: attach **`versona-all`** or **`forge-versona`** when uncertain  
- Sync from blueprint templates: `blueprints/sdlc/methodologies/forge/setup/sync-forge-cursor-rules.sh`  
- Markdown-canonical guardrails: copy from `blueprints/sdlc/templates/forge/cursor-rules/markdown-canonical/*.mdc` into `.cursor/rules/`

## Historical Cursor imports

- Raw: `imports/cursor-history/raw/`  
- Normalized: `imports/cursor-history/normalized/*.md`  
- Ledgers: `SCHEMA-NOTES.md`, `IMPORT-LEDGER.md`  
- Prompt: `blueprints/sdlc/templates/forge/forge-cursor-history-import.prompt.md`  
- Runs must be **idempotent** (stable `source_record_id`)

## Canonicalization

Before creating a new requirement, Spark, or defect: search existing `.md`; choose **exactly one** action **A–G** (see `canonicalization-policy.mdc` and `blueprints/sdlc/methodologies/markdown-canonical-workspace-policy.md`). Record the decision in `TRACEABILITY.md` or `IMPORT-LEDGER.md`.

## Operational prompts (blueprints)

| Step | Prompt path under `blueprints/sdlc/templates/forge/` |
|------|------------------------------------------------------|
| Classify / route | `forge-request-classifier-intake.prompt.md` |
| Meta decomposition | `forge-meta-request-decomposition.prompt.md` |
| Direct Sparks / Charge | `forge-direct-execution-sparks-charge.prompt.md` |
| Cursor history | `forge-cursor-history-import.prompt.md` |
| Estimation bootstrap | `forge-estimation-bootstrap.prompt.md` |
| Defects | `forge-defect-triage-rca-test-impact.prompt.md` |

---

*Copy this file to the **repository root** as `AGENTS.md` and customize paths if `docs/PROJECT.md` overrides any layout.*
