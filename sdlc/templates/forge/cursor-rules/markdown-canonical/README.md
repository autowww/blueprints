---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Markdown-canonical Cursor rules (copy bundle)

**Purpose:** Focused **`.cursor/rules/*.mdc`** seeds for **Forge SDLC** repos that commit to **Markdown-only** canonical artifacts (no CSV SoT). Copy into a **consuming** repository’s `.cursor/rules/` (merge with existing Forge/Versona rules).

**Do not** commit these as the only rules if the repo already uses **`sync-forge-cursor-rules.sh`** — merge deliberately; see [`../../../../methodologies/forge/setup/CURSOR-RULES-QUICKSTART.md`](../../../../methodologies/forge/setup/CURSOR-RULES-QUICKSTART.md).

## Files

| File | `alwaysApply` | Role |
|------|---------------|------|
| `markdown-artifact-policy.mdc` | **true** | Markdown-only SoT; paths; no history in `blueprints/` |
| `canonicalization-policy.mdc` | **true** | Search + **A–G** + ledger |
| `request-classifier.mdc` | false | Intake classification |
| `meta-request-decomposer.mdc` | false | Roadmap / WBS / trace |
| `spark-planner.mdc` | false | Forge Sparks + Charge |
| `historical-import.mdc` | false | Cursor import |
| `estimation.mdc` | false | ESTIMATES + ESTIMATION-RULES |
| `defect-rca-testing.mdc` | false | Defects + ISTQB impact |
| `versona-routing.mdc` | false | Which Versona / session |

## AGENTS.md

Copy **`AGENTS.template.md`** to repo root as **`AGENTS.md`** and adjust for your paths.

## Upstreaming

These files **are** upstream in **blueprints**; consuming repos **copy** or **submodule-reference** paths in AGENTS. Optional future work: wire a **preset** in `sync-forge-cursor-rules.sh` to install this bundle alongside recommended Versonas.
