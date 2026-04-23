---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Direct execution — Forge Sparks and Charge candidates

**Purpose:** **Follow-on prompt** when [`forge-request-classifier-intake.prompt.md`](forge-request-classifier-intake.prompt.md) classifies work as a **direct execution** request. The assistant acts as **Forge execution planner** and proposes **Forge Spark(s)**, **Charge** membership, and **Markdown** updates.

**Related:** [`../../methodologies/forge/process-and-flows.md`](../../methodologies/forge/process-and-flows.md) · [`../../methodologies/forge/daily/README.md`](../../methodologies/forge/daily/README.md) (`forge/charge.md`) · [`../../methodologies/forge/NAMING-REFERENCE.md`](../../methodologies/forge/NAMING-REFERENCE.md) (Forge Spark vs Product Spark) · [`../../methodologies/markdown-canonical-workspace-policy.md`](../../methodologies/markdown-canonical-workspace-policy.md) · [`../../DOCUMENTATION-STRUCTURE.md`](../../DOCUMENTATION-STRUCTURE.md)

---

## Canonical paths (stock blueprint)

| Concept | Default path (consuming repo root) |
|---------|-------------------------------------|
| **Charge** | **`forge/charge.md`** — today’s selected Forge Sparks (`forge-charge.sh` uses this path) |
| **Day journal** | `forge/journal/YYYY-MM-DD.md` |
| **Archived Charge** | `forge/charge-archive/` |
| **Forge iteration** | Often **implicit** in planning docs (`docs/ROADMAP.md`, `docs/requirements/WBS.md`, `forge/releases/*.md`); there is **no** single required `ITERATION.md` in stock templates |

**Team override:** If `docs/PROJECT.md` documents **`forge/current/CHARGE.md`** and **`forge/current/ITERATION.md`** (or similar), use **those** paths **instead** and state that in the change plan. Do **not** introduce `forge/current/` without recording it in `docs/PROJECT.md`.

---

## How to use

1. Run the **classifier** prompt; confirm **direct execution** (or equivalent) in output **A**.  
2. Copy from **“Act as Forge execution planner…”** through **“F. Risks…”** below.  
3. Paste the **request** into the fence.  
4. Prefer **`forge/charge.md`** unless the repo declares an alias.  
5. **Never** write project history under `blueprints/`.

---

## Prompt body (copy from here)

Act as **Forge execution planner** for this workspace.

Convert this **direct executable** request into **Forge Sparks** and decide whether any item belongs in the **current Forge iteration Charge**.

**Request:**

```
<<<PASTE REQUEST HERE>>>
```

**Workspace rules:**

- **Markdown-only** canonical artifacts (`.md`); **no CSV** / spreadsheet SoT.  
- **Forge Spark** = smallest **delivery** unit (~1–4 h), often WBS **task** id `M{n}E{n}S{n}T{n}`; **not** a **Product Spark** (release slice).  
- **Charge** lists **today’s** committed Forge Sparks — see **`forge/charge.md`** (or team alias documented in `docs/PROJECT.md`).

**Tasks:**

1. Decide whether the request is **one** Forge Spark or **several** (split if multiple PR-sized outcomes, different repos, or non-overlapping acceptance).

2. Identify **prerequisites**, **sequencing**, and **hidden decomposition** (unknowns, discovery work — if the “hidden” work is learning-only, flag as **discipline exploration spike** per [`DISCIPLINE-SPIKE.md`](../../methodologies/forge/versona/DISCIPLINE-SPIKE.md), not a Forge Spark).

3. **Search** for existing same/similar Spark-level items in:
   - `docs/requirements/WBS.md`  
   - Linked **task / Spark** Markdown files (e.g. `docs/requirements/milestones/.../tasks/*-task.md` or team `sparks/*.md`)  
   - **Charge** file: **`forge/charge.md`** *or* team alias **`forge/current/CHARGE.md`** if documented  
   - **Iteration** summary: **`forge/current/ITERATION.md`** *if present*, else `docs/requirements/WBS.md` / `docs/ROADMAP.md` / relevant `forge/releases/*.md`  
   - `docs/requirements/TRACEABILITY.md`

4. For **each** candidate Forge Spark, choose **exactly one** canonicalization action **A–G** from [`markdown-canonical-workspace-policy.md`](../../methodologies/markdown-canonical-workspace-policy.md).

5. Propose or update **Spark records** (front matter and/or body) with:
   - `id`  
   - `title`  
   - `parent` — **Ingot** / story id (`M{n}E{n}S{n}`) and, if known, **Product Spark** / milestone link  
   - `repos` / module affected  
   - **Acceptance criteria** (testable)  
   - `dependencies` (Spark ids or external)  
   - **Owner discipline** / suggested **Versona** (e.g. SE, UX, DevOps)  
   - `estimation` placeholder (`TBD` or team format)  
   - `canonicalization` (action **A–G** + note)

6. **Update or propose** Markdown updates to:
   - `docs/requirements/WBS.md`  
   - Spark / task files under `docs/requirements/...`  
   - `docs/requirements/TRACEABILITY.md`  
   - **Iteration** doc if the repo maintains **`forge/current/ITERATION.md`**; otherwise the **WBS** / **ROADMAP** section that names the active **Forge iteration**  
   - **`forge/charge.md`** (or documented **Charge** alias)

7. **Recommend** which Sparks belong on the **next Charge** (today / next session) vs backlog — respect WIP and dependencies.

8. **Flag** any item **too large** for one Forge Spark (suggest split into multiple `…T{n}` or refinement into an **Ingot** first).

**Execution mode:**

- **High confidence** — apply **direct** Markdown edits.  
- **Lower confidence** — output **exact** file paths and **full** Markdown fragments for review.

**Return (structured output):**

**A. Spark list** — table: id, title, phase prefix if used (`build:`, `verify:`, …), status, parent.  
**B. Sequence and dependencies** — ordered graph or numbered list.  
**C. Charge recommendation** — which ids to add/remove on **today’s** Charge; what to leave in bank/backlog.  
**D. Markdown file changes** — path + create/update + one-line purpose.  
**E. Canonicalization decisions** — per candidate: **A–G**, similarity state, ledger pointer (`TRACEABILITY` / `IMPORT-LEDGER`).  
**F. Risks and hidden decomposition** — bullets: unknowns, spikes, oversized work, cross-repo coupling.

---

## Maintainer notes

- Scripts (`forge-charge.sh`) expect **`forge/charge.md`** — if using **`forge/current/CHARGE.md`**, either **symlink**, **wrap** the script, or **manually mirror**; document in `docs/PROJECT.md`.  
- After Charge update, **daily sync** alignment is per [`ceremonies-prescriptive.md`](../../methodologies/forge/ceremonies-prescriptive.md) (C3).  
- If no **parent Ingot** exists, either **link** Spark to the nearest story in WBS or **trigger** [`forge-meta-request-decomposition.prompt.md`](forge-meta-request-decomposition.prompt.md) to create the **Ingot** row first.
