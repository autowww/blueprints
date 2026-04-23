---
slug: markdown-canonical-workspace-policy
tier: 201
lens: methodology
nav_section: Agentic Engineering
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Markdown-canonical workspace policy (optional repo profile)

**Purpose:** Reusable **preamble** for agent prompts, **root `AGENTS.md`**, or **project rules** when a team wants a **single markdown-shaped system of record** for project artifacts. This is an **optional profile** for **consuming repositories** — not a change to what the **`blueprints/`** submodule itself stores (the submodule remains **framework-only**, not project history).

**Related:** [`agentic-sdlc.md`](agentic-sdlc.md) · [`DOCUMENTATION-STRUCTURE.md`](../DOCUMENTATION-STRUCTURE.md) · [`forge/NAMING-REFERENCE.md`](forge/NAMING-REFERENCE.md) · [`forge/VERSONA-OPERATING-MODEL.md`](forge/VERSONA-OPERATING-MODEL.md) (optional JSON/JSONL for Versona tooling)

---

## Relationship to other blueprint conventions

| Topic | Default blueprint guidance | Under this profile |
|-------|---------------------------|-------------------|
| Traceability / risk matrices | [`DOCUMENTATION-STRUCTURE.md`](../DOCUMENTATION-STRUCTURE.md) allows **CSV** under `docs/requirements/traceability/` (and similar) for diffs and spreadsheet round-trip | Express the **same relationships** in **Markdown** (tables and lists) in agreed files such as `docs/requirements/TRACEABILITY.md`; do **not** treat CSV/spreadsheets as the **canonical** source of truth |
| Optional Versona machine artifacts | [`forge/VERSONA-OPERATING-MODEL.md`](forge/VERSONA-OPERATING-MODEL.md) — optional **`session.manifest.json`**, **JSONL** ledgers under `forge-logs/versona-track/` | Those files remain **tooling adjuncts**, not replacements for human-canonical specs and decisions in Markdown; teams that want **zero** JSON in-repo may omit that operating model or gitignore generated files per `AGENTS.md` |

**Forge vocabulary** in this profile matches [`forge/NAMING-REFERENCE.md`](forge/NAMING-REFERENCE.md): **Product Spark** and **Forge Spark** are **never** synonyms.

---

## Shared workspace policy

- **Blueprints** is a reusable submodule and **must not** store **project-specific** mutable history.
- All **canonical project artifacts** must be **Markdown only**.
- Do **not** create **CSV**, **spreadsheet**, or **JSON** files as **canonical** repository artifacts.
- **Raw imports** may remain in their **original format** under `imports/cursor-history/raw/`; **normalized** and **canonical** outputs must be **`.md`**.
- Use **Forge** terminology consistently: **Ore**, **Product Spark**, **Ingot**, **Forge Spark**, **Charge**, **Forge iteration**, **Ember Log**, **Assay**.
- **Product Spark** and **Forge Spark** are different and must **never** be treated as synonyms.
- Before creating a new artifact, inspect **existing** canonical Markdown files and apply **exactly one** canonicalization action (below).

### Canonicalization — initial states

1. Exact duplicate  
2. Near duplicate  
3. Same intent but broader existing item  
4. Same intent but narrower existing item  
5. Related but distinct item  
6. Conflicting definition  
7. Obsolete existing item  
8. Obsolete incoming item  
9. Ambiguous / insufficient evidence  

### Canonicalization — actions (choose exactly one)

| ID | Action |
|----|--------|
| **A** | Keep existing; deprecate or reject incoming |
| **B** | Update existing with incoming evidence |
| **C** | Merge incoming into existing and deprecate incoming |
| **D** | Keep both as distinct and cross-link them |
| **E** | Split one or both into multiple canonical items |
| **F** | Replace old canonical item with new one and deprecate old |
| **G** | Deprecate both and create a fresh consolidated canonical item |

### Ledger and traceability

- Every canonicalization decision must be documented in **Markdown** in the most relevant **ledger**, usually:
  - `docs/requirements/TRACEABILITY.md`
  - `imports/cursor-history/IMPORT-LEDGER.md`
  - Defect-local notes for defect cases (e.g. under `docs/defects/` when that layout is used)
- Preserve traceability back to the **source request**, imported Cursor record, or defect report.
- Prefer **updating** canonical Markdown files over scattering new files randomly.
- Use **YAML front matter** in per-item Markdown files when helpful for `id`, `type`, `status`, `parent`, repos, Versonas, and estimation fields.

---

## Using this block

- **Prompt preamble:** Paste the **Shared workspace policy** section (from the bullet list through **Ledger and traceability**) at the top of a task-specific prompt.  
- **Intake + routing:** Pair with [`../templates/forge/forge-request-classifier-intake.prompt.md`](../templates/forge/forge-request-classifier-intake.prompt.md) for day-to-day classification (Ore / Product Spark / Ingot / Forge Spark / defect / spike) and canonical Markdown targets; for **meta-requests**, follow with [`../templates/forge/forge-meta-request-decomposition.prompt.md`](../templates/forge/forge-meta-request-decomposition.prompt.md) to update **ROADMAP**, **WBS**, and **TRACEABILITY**; for **direct execution**, follow with [`../templates/forge/forge-direct-execution-sparks-charge.prompt.md`](../templates/forge/forge-direct-execution-sparks-charge.prompt.md) for **Forge Sparks** and **`forge/charge.md`**.  
- **Historical Cursor import:** Bulk reconstruction from SQLite/exports under `imports/cursor-history/raw/` → [`../templates/forge/forge-cursor-history-import.prompt.md`](../templates/forge/forge-cursor-history-import.prompt.md) (`SCHEMA-NOTES.md`, `normalized/`, **`IMPORT-LEDGER.md`**, promotion to `docs/`).  
- **Defects:** Triage, **RCA**, ISTQB-oriented **test impact** → [`../templates/forge/forge-defect-triage-rca-test-impact.prompt.md`](../templates/forge/forge-defect-triage-rca-test-impact.prompt.md) (`docs/defects/**`, **TRACEABILITY** updates).  
- **`AGENTS.md`:** Keep repo-wide defaults there ([`forge/VERSONA-OPERATING-MODEL.md`](forge/VERSONA-OPERATING-MODEL.md) §3); add this block or a link to this handbook page so agents inherit the profile.  
- **Declare adoption** in `docs/PROJECT.md` (or equivalent) so contributors know the repo chose **markdown-canonical** matrices instead of CSV.  
- **Cursor rules bundle:** copy [`../templates/forge/cursor-rules/markdown-canonical/`](../templates/forge/cursor-rules/markdown-canonical/) into `.cursor/rules/` and use [`AGENTS.template.md`](../templates/forge/cursor-rules/markdown-canonical/AGENTS.template.md) as root **`AGENTS.md`**.

---

*Blueprint reference — consuming repos opt in; does not override frozen submodule content policy.*
