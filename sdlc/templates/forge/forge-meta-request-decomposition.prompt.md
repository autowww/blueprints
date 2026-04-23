---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Meta-request decomposition — roadmap / WBS / Forge artifacts

**Purpose:** **Follow-on prompt** when [`forge-request-classifier-intake.prompt.md`](forge-request-classifier-intake.prompt.md) (or equivalent) classifies work as a **meta-request** needing decomposition. The assistant acts as **Product Manager + BA + Forge planning orchestrator** and materializes **Markdown-only** repo artifacts.

**Related:** [`../../methodologies/forge/planning/PLANNING-FLOW.md`](../../methodologies/forge/planning/PLANNING-FLOW.md) · [`../../methodologies/forge/planning/README.md`](../../methodologies/forge/planning/README.md) · [`../../methodologies/forge/NAMING-REFERENCE.md`](../../methodologies/forge/NAMING-REFERENCE.md) · [`../../DOCUMENTATION-STRUCTURE.md`](../../DOCUMENTATION-STRUCTURE.md) (nested requirements layout) · [`../../methodologies/markdown-canonical-workspace-policy.md`](../../methodologies/markdown-canonical-workspace-policy.md) · [`../../methodologies/forge/versona/VERSONA-CONTRACT.md`](../../methodologies/forge/versona/VERSONA-CONTRACT.md) · **Then execute:** [`forge-direct-execution-sparks-charge.prompt.md`](forge-direct-execution-sparks-charge.prompt.md)

---

## How to use

1. Run the **classifier** prompt first; confirm output **A** includes **meta-request** (or equivalent).  
2. Copy everything from **“Act as Product Manager…”** through **“E. Missing Versonas…”** below.  
3. Paste the **same original user request** (or the classified summary + raw request) into the **Input request** fence.  
4. Prefer **editing** existing `docs/requirements/**` files over adding parallel trees.  
5. **Never** commit project-specific history under `blueprints/` (submodule is read-only framework).

---

## Prompt body (copy from here)

Act as **Product Manager + BA + Forge planning orchestrator** for this workspace.

Convert the classified **meta-request** into **markdown-based** repository artifacts using Forge SDLC concepts and the **existing** `docs/` structure.

**Input request:**

```
<<<PASTE REQUEST HERE>>>
```

**Workspace rules:**

- **Canonical outputs:** `.md` only — Markdown tables, lists, front matter, linked detail files. **No CSV**, spreadsheets, or JSON as canonical SoT.  
- **Terminology:** Use **Ore**, **Product Spark**, **Ingot**, **Forge Spark**, **Forge iteration**, **Charge**, **Ember Log**, **Assay** consistently. **Product Spark** (release / roadmap slice) **≠** **Forge Spark** (executable task). Roadmap and release-slice planning stay at **Product Spark** level; implementation commitment for the current cycle appears as **Forge Spark** rows and on **`forge/charge.md`** when the repo uses Forge daily ops.  
- **Layout:** Follow the repo’s adopted tree (typically `docs/requirements/milestones/M{n}/…` with `epic.md`, `story.md`, `tasks/*-task.md` per [`DOCUMENTATION-STRUCTURE.md`](../../DOCUMENTATION-STRUCTURE.md); if the team uses a `sparks/` folder for Forge Spark files, stay consistent with `docs/PROJECT.md`).

**Tasks:**

1. **Derive** and list:
   - **Business driver** or **roadmap intent** (problem/opportunity, “why now”).  
   - **Product Spark** candidates (coarse shippable slices — PoC / MVP / phase / milestone-aligned).  
   - **Ingot** candidates (refined items with acceptance shape — often story-level `M{n}E{n}S{n}`).  
   - **Forge Spark** candidates (executable slices — often task-level `…T{n}`, phase-prefixed where the team uses `discover:` / `specify:` / `build:` / `verify:` / `release:`).

2. **Map** the decomposition to the **current** Markdown WBS and **ID scheme** documented in `docs/requirements/WBS.md`, `docs/requirements/STRUCTURE-PROPOSAL.md` (if present), and `docs/PROJECT.md`. Do **not** invent a second ID namespace.

3. **Search** for existing same/similar items in at least:
   - `docs/ROADMAP.md`  
   - `docs/requirements/INDEX.md`  
   - `docs/requirements/WBS.md`  
   - Related **milestone / epic / story** Markdown files under `docs/requirements/milestones/…`  
   - **Forge Spark–level** task files (e.g. `tasks/M1E1S1T1-task.md` or team `sparks/*.md`)  
   - `docs/requirements/TRACEABILITY.md`  
   - Optionally `docs/requirements/ESTIMATES.md` if it exists.

4. For **each** candidate item, choose **exactly one** canonicalization **action** from the shared workspace policy — **A** through **G** — and give a **one-line why** (duplicate / merge / split / replace / etc.).

5. **Create or update** Markdown artifacts, including where applicable:
   - `docs/ROADMAP.md`  
   - `docs/requirements/INDEX.md`  
   - `docs/requirements/WBS.md`  
   - `docs/requirements/TRACEABILITY.md`  
   - `docs/requirements/ESTIMATES.md` (if used — estimation **placeholders** only until sized)  
   - Milestone / epic / story / task (Forge Spark) files under `docs/requirements/…`  
   - If the repo uses **`forge/releases/`** for Product Spark plans, add or update the appropriate release-plan Markdown there and **link** from `ROADMAP.md` / WBS.

6. For **each** new or materially updated item, capture in **YAML front matter** (preferred) or a **consistent “Item record”** subsection in the body:

   - `title`  
   - `id`  
   - `parent` (parent ID)  
   - `type` (`ore` \| `product_spark` \| `milestone` \| `epic` \| `ingot` \| `story` \| `forge_spark` \| `task` — use the set the repo already uses)  
   - `status`  
   - `rationale` (short)  
   - `dependencies` (ids or links)  
   - `repos` (repos affected)  
   - `versonas` (Versonas needed)  
   - `estimation` (placeholder, e.g. `TBD`)  
   - `source_request` (pointer back to intake / ticket / `IMPORT-LEDGER.md` line)  
   - `canonicalization` (action letter **A–G** + target id if merged/replaced)

7. Update **WBS** and **traceability** sections using **Markdown tables** or **linked section lists** (no CSV).

8. If a **Versona** is needed but **no** suitable template exists in `blueprints/…/versona/catalog/`, **propose** a **new** discipline or workflow Versona **spec** (not necessarily a file in `blueprints/` from this task): **trigger**, **inputs**, **outputs**, **guardrails**, and **§5** expectations per [`VERSONA-CONTRACT.md`](../../methodologies/forge/versona/VERSONA-CONTRACT.md). Prefer reusing **Product Management**, **BA**, **Architecture**, **UX**, **SE**, **Testing**, **PM (governance)** before inventing a name.

9. **Preserve traceability** from the **original request** to **every** touched artifact (IDs + file paths in `TRACEABILITY.md` and/or a new row in `imports/cursor-history/IMPORT-LEDGER.md` if the request came from import).

**Execution mode:**

- **High confidence** — apply edits **directly** in the repo (create/update the listed Markdown files).  
- **Lower confidence** — output **exact** proposed file paths and **full** Markdown bodies for human review before apply.

**Constraints:**

- Do **not** write project-specific narrative into **`blueprints/`**.  
- Do **not** use **CSV** for canonical matrices.

**Return (structured output):**

**A. Artifact decomposition** — table or nested list: driver → Product Sparks → Ingots → Forge Sparks (with IDs).  
**B. File-by-file markdown change plan** — path, action (create/update/deprecate stub), one-line intent.  
**C. Traceability map** — request → artifact IDs → file paths.  
**D. Canonicalization decisions** — per candidate: action **A–G**, similarity state, ledger note location.  
**E. Missing Versonas or skills to add** — bullet list or “none”; if new, include trigger / inputs / outputs / guardrails.

---

## Maintainer notes

- **Ore** that is not yet refined may live only in `docs/ROADMAP.md` or a backlog section until refined into Ingots — avoid minting `story.md` files without acceptance criteria.  
- **Product Spark** planning depth: use templates under [`../../methodologies/forge/planning/`](../../methodologies/forge/planning/) (`poc-plan`, `mvp-plan`, `phase-plan`, `release-plan`) when the repo adopts them; store **instances** under `forge/releases/` or `docs/` per `docs/PROJECT.md`.  
- After decomposition, use [`forge-direct-execution-sparks-charge.prompt.md`](forge-direct-execution-sparks-charge.prompt.md) to pull **Forge Sparks** onto **`forge/charge.md`**, or return to [`forge-request-classifier-intake.prompt.md`](forge-request-classifier-intake.prompt.md) for re-classification.
