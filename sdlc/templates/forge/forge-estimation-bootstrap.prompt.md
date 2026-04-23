---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Estimation model bootstrap — prompt

**Purpose:** One-shot (or periodic) prompt to **design, calibrate, and apply** the team’s **Forge estimation method** in a **markdown-canonical** repo. Use after copying templates from **`blueprints/sdlc/templates/forge/estimation/`** and **`blueprints/sdlc/templates/requirements/ESTIMATES.template.md`**.

**Related:** [`estimation/ESTIMATION-RULES.template.md`](estimation/ESTIMATION-RULES.template.md) · [`../requirements/ESTIMATES.template.md`](../requirements/ESTIMATES.template.md) · [`../../methodologies/forge/versona/catalog/discipline/governance/versona-estimation.mdc.template`](../../methodologies/forge/versona/catalog/discipline/governance/versona-estimation.mdc.template) · [`../../methodologies/markdown-canonical-workspace-policy.md`](../../methodologies/markdown-canonical-workspace-policy.md)

---

## Prompt body (copy from here)

Act as **Estimation Versona designer** and **estimator** for this Forge SDLC workspace.

Design and apply an estimation method for **meta-requests**, **Forge Sparks**, and **defects** using:

- **Fibonacci** sizing  
- **t-shirt** sizes  
- **estimated token consumption** (bands)  
- **Calibration** against historical repo data in Markdown ledgers  

**Workspace:** **Markdown-only** canonical artifacts (no CSV SoT).

**Tasks**

1. Propose a **mapping** between: estimated work **complexity** · **Fibonacci bucket** · **t-shirt size** · **estimated token range** (use or tune [`forge/estimation/ESTIMATION-RULES.md`](estimation/ESTIMATION-RULES.template.md) seed).

2. Define **estimation fields** for YAML **front matter** and/or **`docs/requirements/ESTIMATES.md`** (e.g. `est_fib`, `est_tshirt`, `est_tokens`, `actual_tokens`, `uncertainty`, `coordination_factor`, `risk_multiplier`).

3. Define how estimates **roll up** from **Forge Spark** → **Ingot** → **Product Spark** / milestone.

4. Define **defect** handling: **ambiguity multiplier**, **blast-radius multiplier**, **RCA uncertainty** (combined `risk_multiplier` or explicit factors).

5. **Analyze** historical items already in **this repo** (`ESTIMATES.md`, closed tasks in `docs/requirements/**`, `WBS.md`, `IMPORT-LEDGER.md` if present) and infer **initial calibration** heuristics; if no history, state **defaults** and first **iteration** collection plan.

6. **Create or update** Markdown:  
   - `forge/estimation/ESTIMATION-RULES.md` (copy from `blueprints/sdlc/templates/forge/estimation/ESTIMATION-RULES.template.md`)  
   - `docs/requirements/ESTIMATES.md` (copy from `blueprints/sdlc/templates/requirements/ESTIMATES.template.md`)  
   - `docs/requirements/WBS.md` (estimation summary column or pointer to `ESTIMATES.md`)

7. Recommend **front matter** on per-item files (`est_fib`, `est_tshirt`, `est_tokens`, `actual_tokens`, `uncertainty`, `coordination_factor`, `risk_multiplier`).

8. If **`versona-estimation`** is not installed, copy [`versona-estimation.mdc.template`](../../methodologies/forge/versona/catalog/discipline/governance/versona-estimation.mdc.template) to `.cursor/rules/` per [`CURSOR-RULES-QUICKSTART.md`](../../methodologies/forge/setup/CURSOR-RULES-QUICKSTART.md).

9. **Search** for overlapping estimation guidance (`STRUCTURE-PROPOSAL`, `WBS.md`, `PROJECT.md`, PM docs). Choose **one** canonicalization action **A–G** from the markdown-canonical policy before replacing a standard.

**Execution mode:** Apply edits **directly** when confident; else output **exact** Markdown for each file.

**Return:** **A.** Estimation model · **B.** Token/Fibonacci/t-shirt correlation · **C.** Markdown files to add/update · **D.** Calibration approach · **E.** Draft Estimation Versona summary (or “use shipped `versona-estimation`”) · **F.** Canonicalization decision for estimation standards

---

## Maintainer notes

- **Canonicalization:** **`versona-pm`** owns **commitments**; **`versona-estimation`** owns **method** — prefer **D** (distinct, cross-link) vs merging into PM.  
- Register **`versona-estimation`** in [`versona-standards-matrix.yaml`](../../methodologies/forge/standards/versona-standards-matrix.yaml) after install for standards profile parity.
