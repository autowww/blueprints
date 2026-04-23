---
# Template — copy to consuming repo as forge/estimation/ESTIMATION-RULES.md (create folder if needed).
# Do not store project-specific calibration numbers in blueprints; tune tables below per repo.
---

# Estimation rules — Forge SDLC (markdown-canonical)

**Purpose:** Single **method standard** for sizing **meta-requests**, **Forge Sparks**, **Ingots**, **Product Sparks**, and **defects** using **Fibonacci story points**, **t-shirt sizes**, **estimated LLM token bands**, and **calibration** from historical Markdown ledgers.

**Related:** `docs/requirements/ESTIMATES.md` · `docs/requirements/WBS.md` · [`blueprints/sdlc/methodologies/forge/NAMING-REFERENCE.md`](../../blueprints/sdlc/methodologies/forge/NAMING-REFERENCE.md) · [`blueprints/sdlc/methodologies/markdown-canonical-workspace-policy.md`](../../blueprints/sdlc/methodologies/markdown-canonical-workspace-policy.md)

*Paths assume `forge/estimation/` at repo root next to `blueprints/` submodule.*

---

## 1. Complexity → Fibonacci → t-shirt → token band

**Interpretation**

| Complexity (delivery + coordination) | Fibonacci (`est_fib`) | T-shirt (`est_tshirt`) | Estimated tool tokens (`est_tokens`) — **indicative band** |
|-------------------------------------|----------------------|-------------------------|------------------------------------------------------------|
| Trivial, single file, known pattern | 1 | XS | 8k–40k |
| Small change, one module | 2 | S | 40k–120k |
| Multi-file, local tests | 3 | S–M | 120k–250k |
| Cross-module, integration | 5 | M | 250k–500k |
| Subsystem or unfamiliar surface | 8 | L | 500k–1M |
| Large refactor / broad blast radius | 13 | XL | 1M–2.5M |
| Program-level / multiple repos (split first) | 21+ | XXL | 2.5M+ (strong signal to **decompose**) |

**Notes**

- **Fibonacci** is the **primary** roll-up number for WBS math.  
- **T-shirt** is for **human scan** in roadmaps and non-technical readers.  
- **Tokens** are **rough capacity** signals for AI-assisted work (input+output across the task), **not** a billing truth. Log **`actual_tokens`** when the tool provides usage for the session that closed the Spark.  
- If **Fibonacci** and **token band** disagree, trust **Fibonacci** for planning; **widen** the token band or **split** the Spark.

---

## 2. Front matter and ledger fields

**Per-item YAML** (stories, tasks, defects, meta-requests when filed as Markdown):

| Field | Meaning |
|-------|---------|
| `est_fib` | Fibonacci points for **this** item |
| `est_tshirt` | XS, S, M, L, XL, XXL |
| `est_tokens` | Single number **midpoint** or string band e.g. `120k–250k` |
| `actual_tokens` | After completion, if known |
| `uncertainty` | `low` \| `medium` \| `high` |
| `coordination_factor` | `1.0` default; >1 when multiple reviewers/repos |
| `risk_multiplier` | `1.0` default; >1 when defect/RCA/regression risk (see §5) |

**Roll-up fields** (optional on parents, or only in `ESTIMATES.md`):

| Field | Meaning |
|-------|---------|
| `est_fib_rollup` | Sum or **ceiling of sum** of children (team choice; document here) |
| `est_note` | Assumptions, links to §5 sessions |

---

## 3. Roll-up: Forge Spark → Ingot → Product Spark

| Level | Rule |
|-------|------|
| **Forge Spark** (`…T{n}`) | **Point estimate** (`est_fib`); smallest grain for **actual_tokens** capture. |
| **Ingot** (story `…S{n}`) | **Default:** `est_fib_rollup` = sum of child Spark Fibonacci, capped at **21** unless epic explicitly allows higher (then **split** story). |
| **Product Spark** / milestone | **Sum** of Ingots (or epic roll-ups) with **explicit risk buffer** (e.g. +20% for integration) documented in `ESTIMATES.md`. **Product Spark** uses **release-slice** narrative; numbers live in **`ESTIMATES.md`** and milestone headers. |

**Meta-request** (not yet decomposed): provisional **`est_fib`** on a **draft** row in `ESTIMATES.md` with `uncertainty: high`; replace after decomposition.

---

## 4. Defect handling

| Factor | Multiplier (apply to `est_fib` before roll-up) | When |
|--------|-----------------------------------------------|------|
| **Ambiguity** | ×1.0–×2.0 | Repro unclear, environment unknown, “sometimes” |
| **Blast radius** | ×1.0–×2.0 | Shared library, security, data migration, API contract |
| **RCA uncertainty** | ×1.0–×1.5 | Root cause not found; spike may be needed first |

**Combine** multiplicatively with a **ceiling** (e.g. max ×4) or use **`risk_multiplier`** as the single combined field—pick one convention and state it in `docs/PROJECT.md`.

**Discipline:** If fix requires **learning** before delivery, open a **discipline exploration spike** (not a Forge Spark) per [`DISCIPLINE-SPIKE.md`](../../blueprints/sdlc/methodologies/forge/versona/DISCIPLINE-SPIKE.md); size spike separately with **`est_fib`** capped low (e.g. ≤5) and time-box.

---

## 5. Calibration (consuming repo)

1. Maintain **`docs/requirements/ESTIMATES.md`** with columns: `id`, `est_fib`, `actual_tokens`, `completed_at`, `variance_note`.  
2. Each **Forge iteration** boundary, compute **median** `actual_tokens / est_fib` for closed Sparks; adjust **token bands** in §1 if systematically off.  
3. Never overwrite **historical** rows; **append** calibration notes to this file’s **Revision** section.

*(The **blueprints** repo does not store your project’s calibration history.)*

---

## 6. Canonicalization

Before replacing an existing estimation scheme: compare to **`ESTIMATES.md`**, **`WBS.md`**, and any **`STRUCTURE-PROPOSAL.md`**. Prefer **B** (update rules in place) or **C** (merge tables) per [`markdown-canonical-workspace-policy.md`](../../blueprints/sdlc/methodologies/markdown-canonical-workspace-policy.md). **PM Versona** owns **commitments**; **Estimation Versona** owns **method** (`versona-estimation` template).

---

*Template — copy to `forge/estimation/ESTIMATION-RULES.md` and tune bands for your team.*
