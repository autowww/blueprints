---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Historical Cursor database import and reconstruction (markdown-only)

**Purpose:** Prompt for an AI assistant acting as **historical work reconstruction agent** in a **Forge SDLC** consuming repo. Translates **Cursor** history (SQLite and/or exports) into **canonical Markdown** artifacts without duplicating or corrupting existing history.

**Related:** [`../../methodologies/markdown-canonical-workspace-policy.md`](../../methodologies/markdown-canonical-workspace-policy.md) · [`forge-request-classifier-intake.prompt.md`](forge-request-classifier-intake.prompt.md) (classification alignment) · [`forge-meta-request-decomposition.prompt.md`](forge-meta-request-decomposition.prompt.md) · [`forge-direct-execution-sparks-charge.prompt.md`](forge-direct-execution-sparks-charge.prompt.md) · [`../../methodologies/forge/versona/ARTIFACT-CONTRACTS.md`](../../methodologies/forge/versona/ARTIFACT-CONTRACTS.md)

---

## Layout (consuming repo)

| Path | Role |
|------|------|
| `imports/cursor-history/raw/` | **Raw** SQLite DB copies, JSON/ZIP exports, screenshots — **non-canonical**; may stay binary or large; document retention in `AGENTS.md` / `.gitignore` |
| `imports/cursor-history/SCHEMA-NOTES.md` | Human/agent notes on **observed** Cursor schema (version, tables, fields) |
| `imports/cursor-history/normalized/` | **Normalized** `.md` per request or per **thread** |
| `imports/cursor-history/IMPORT-LEDGER.md` | **Deterministic** import index — append/update rows in Markdown tables |
| `docs/requirements/**`, `docs/defects/**`, `forge/**` | **Canonical** project artifacts (Markdown only under this profile) |

**Never** write imported content or project history into **`blueprints/`** (submodule is framework-only).

---

## How to use

1. Place exports / DB snapshot under **`imports/cursor-history/raw/`** (or document symlink path in `SCHEMA-NOTES.md`).  
2. Copy from **“Act as historical work reconstruction agent…”** through **“F. … ambiguities”**.  
3. Run with repo access so the agent can **read** raw sources, **write** normalized + ledger + canonical docs.  
4. Re-runs: use **`IMPORT-LEDGER.md`** and stable **`source_record_id`** to stay **idempotent**.

---

## Prompt body (copy from here)

Act as **historical work reconstruction agent** for a Forge SDLC workspace.

Your job is to translate **historical Cursor request data** into **canonical Markdown** repo artifacts **without** duplicating or corrupting existing history.

**Input source**

- Cursor SQLite database and/or raw exports under **`imports/cursor-history/raw/`** (paths and filenames as present in this repo).

**Workspace rules (markdown-only)**

- **Raw** source data may remain **SQLite / export** form under **`imports/cursor-history/raw/`**.  
- All **normalized** records, **ledgers**, and **canonical** repo artifacts must be **`.md`**.  
- Do **not** use CSV or spreadsheets as canonical SoT.  
- Use **Forge** terminology in normalized summaries and promoted artifacts: **Ore**, **Product Spark**, **Ingot**, **Forge Spark**, **Forge iteration**, **Charge**, **Ember Log**, **Assay** — **Product Spark ≠ Forge Spark**.

**Tasks**

1. **Inspect** available Cursor history sources and **infer** schema (document **Cursor / app version** if discoverable):  
   - request or message **ID**  
   - **timestamp**  
   - **workspace / repo** context (path, git remote if present)  
   - **user prompt** text  
   - **assistant / agent** response summary (if available)  
   - **attachments / images** (paths or hashes; store large binaries only under `raw/` or `raw/attachments/`)  
   - **conversation / thread** grouping (if available)

2. Document findings in **`imports/cursor-history/SCHEMA-NOTES.md`** (update in place on repeat runs — add a **“Revision history”** subsection rather than duplicating the whole doc).

3. **Normalize** records into Markdown under **`imports/cursor-history/normalized/`**:  
   - **Suggested pattern:** one `.md` per **source request** or per **reconstructed thread** (choose one convention per repo and state it in `SCHEMA-NOTES.md`).  
   - **YAML front matter:** `source_record_id`, `source_type`, `cursor_export_version` (if known), `timestamp_utc`, `workspace_path`, `repo` (if known), `classification_draft`, `confidence` (`high` \| `medium` \| `low`), `import_run_id` (optional).  
   - **Body:** concise **normalized summary**, **classification notes**, link to **raw** path (relative), optional blockquote of **original wording** when useful.

4. **Classify** each historical record (draft in normalized file; confirm in ledger):  
   - **Ore** · **Product Spark** · **Ingot** · **Forge Spark** · **defect** · **informational / noise** · **duplicate / superseded**  
   - **Discipline exploration spike** — if the record is learning-only, classify per [`DISCIPLINE-SPIKE.md`](../../methodologies/forge/versona/DISCIPLINE-SPIKE.md) and **do not** promote to Forge Spark without a delivery outcome.

5. For each **accepted** (non-noise, non-duplicate) item, **compare** to existing canonical Markdown (`docs/ROADMAP.md`, `docs/requirements/WBS.md`, milestone tree, `TRACEABILITY.md`, `forge/charge.md`, `docs/defects/**`) and choose **exactly one** canonicalization action **A–G** from [`markdown-canonical-workspace-policy.md`](../../methodologies/markdown-canonical-workspace-policy.md).

6. **Build / maintain** **`imports/cursor-history/IMPORT-LEDGER.md`** with a **deterministic** Markdown table (or section per batch). Each row should capture:  
   - `source_record_id`  
   - `normalized_file` (path)  
   - `canonical_ids` (WBS / defect / Spark ids **created or linked**; empty if rejected)  
   - `import_status` (`pending` \| `normalized_only` \| `promoted` \| `rejected` \| `superseded`)  
   - `confidence`  
   - `canonicalization_action` (**A–G**)  
   - `ambiguity_notes`  
   - **Idempotency:** if `source_record_id` already has `promoted` or `rejected` with same decision, **do not** duplicate canonical artifacts — **update** notes only if new evidence warrants **B** or **C** with human-visible rationale.

7. For each **accepted** item chosen for promotion, **create or update** canonical Markdown:  
   - Roadmap / WBS / requirement files  
   - Spark / **task** files under `docs/requirements/...`  
   - Defect files under `docs/defects/...` (if used)  
   - **`docs/requirements/TRACEABILITY.md`** (link **source_record_id** → **canonical id**)

8. **Never** write imported raw data into **`blueprints/`**.

9. If **one** record spans **multiple** work items, **split** into multiple normalized files (or one file with multiple **Item** sections with distinct provisional ids) and **preserve** cross-links.

10. If **ambiguous**, keep the normalized record, set **low** confidence, **minimum safe** interpretation in notes, and prefer **`normalized_only`** status until a human promotes.

11. Preserve **historical timestamps** and **original wording** (quoted) where useful; **normalize** headings and links to **Forge** terms in summaries.

12. **Idempotent runs:** same `source_record_id` must not create **second** canonical rows; **update** ledger and existing Markdown **in place**.

**Execution mode**

- When possible, perform **normalization** and **Markdown updates** **directly** in the repo.  
- If the repo lacks `imports/cursor-history/` or policies forbid writes, output **exact** paths and **full** Markdown for each file to create.

**Return (structured output)**

**A. Schema inference** — tables/fields discovered, Cursor version notes, limitations.  
**B. Normalization plan** — file naming, one-vs-thread convention, front matter keys.  
**C. Classification rules** — how you mapped record types to Forge classes (including noise/duplicate).  
**D. Import ledger design** — table columns, status enum, idempotency rule.  
**E. Canonical markdown files created or updated** — path list with one-line purpose.  
**F. Canonicalization decisions and ambiguities** — per promoted or rejected item: **A–G**, similarity state, open questions.

---

## Maintainer notes

- **Privacy:** scrub secrets, tokens, and personal data from **normalized** `.md` before commit; keep full fidelity only in **local** `raw/` if policy allows.  
- **Binary / size:** prefer **not** committing large SQLite files — document **export** procedure in `SCHEMA-NOTES.md` and use **trimmed** exports when possible.  
- **Promotion workflow:** optional second pass with [`forge-meta-request-decomposition.prompt.md`](forge-meta-request-decomposition.prompt.md) for **meta** bundles, or [`forge-direct-execution-sparks-charge.prompt.md`](forge-direct-execution-sparks-charge.prompt.md) for **execution**-shaped history.
