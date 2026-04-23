---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Product planning

Templates that connect upstream product planning (PoC / MVP / Phased) to the Forge Ore pipeline. Uses the existing PDLC-SDLC bridge and discipline bridges to show how business drivers flow down to daily Sparks.

## Planning hierarchy

```
Business Driver (PDLC P1–P3)
  └── Product Spark (PoC / MVP / Phase release)
        └── Forge Iteration(s) (1–2 week cycles)
              └── Ingots (refined work items)
                    └── Sparks (executable tasks, 1–4 hours)
                          └── Charge (today's selected Sparks)
```

This maps to the existing WBS hierarchy: Milestone → Epic → Story → Task. Forge terms layer on top without replacing the ID scheme.

**Terminology:** **Product Spark** (coarse product planning slice) is not the same as a **Forge Spark** (smallest delivery task on the WBS). **Discipline exploration spikes** are time-boxed learning, not delivery Sparks — see [`../NAMING-REFERENCE.md`](../NAMING-REFERENCE.md) and [`../versona/DISCIPLINE-SPIKE.md`](../versona/DISCIPLINE-SPIKE.md).

## Documents

| File | Purpose |
|------|---------|
| [`PLANNING-FLOW.md`](https://github.com/autowww/blueprints/blob/main/sdlc/methodologies/forge/planning/PLANNING-FLOW.md) | Full pipeline from vision to daily Sparks |
| [`release-plan.template.md`](https://github.com/autowww/blueprints/blob/main/sdlc/methodologies/forge/planning/release-plan.template.md) | Forge release plan template (Product Spark) |
| [`poc-plan.template.md`](https://github.com/autowww/blueprints/blob/main/sdlc/methodologies/forge/planning/poc-plan.template.md) | PoC planning template |
| [`mvp-plan.template.md`](https://github.com/autowww/blueprints/blob/main/sdlc/methodologies/forge/planning/mvp-plan.template.md) | MVP planning template |
| [`phase-plan.template.md`](https://github.com/autowww/blueprints/blob/main/sdlc/methodologies/forge/planning/phase-plan.template.md) | Phase planning template |
| [`forge-planning.mdc.template`](https://github.com/autowww/blueprints/blob/main/sdlc/methodologies/forge/planning/forge-planning.mdc.template) | Cursor rule for guided planning |
| [`forge-meta-request-decomposition.prompt.md`](https://github.com/autowww/blueprints/blob/main/sdlc/templates/forge/forge-meta-request-decomposition.prompt.md) | AI intake prompt: meta-request → `ROADMAP` / WBS / `TRACEABILITY` / milestone tree (Markdown-only) |
| [`forge-direct-execution-sparks-charge.prompt.md`](https://github.com/autowww/blueprints/blob/main/sdlc/templates/forge/forge-direct-execution-sparks-charge.prompt.md) | AI prompt: direct execution → Forge Sparks, task files, **`forge/charge.md`**, Charge recommendation |
| [`forge/estimation/ESTIMATION-RULES.template.md`](https://github.com/autowww/blueprints/blob/main/sdlc/templates/forge/estimation/ESTIMATION-RULES.template.md) | Copy to `forge/estimation/ESTIMATION-RULES.md` — Fibonacci, t-shirt, tokens, defect multipliers |
| [`requirements/ESTIMATES.template.md`](https://github.com/autowww/blueprints/blob/main/sdlc/templates/requirements/ESTIMATES.template.md) | Copy to `docs/requirements/ESTIMATES.md` |
| [`forge-estimation-bootstrap.prompt.md`](https://github.com/autowww/blueprints/blob/main/sdlc/templates/forge/forge-estimation-bootstrap.prompt.md) | AI prompt: bootstrap estimation + install **`versona-estimation`** |

## Product Spark

A **Product Spark** is a potentially shippable product iteration that may span multiple Forge iterations. It represents the coarsest grain of delivery planning in Forge:

| Product stage | Product Spark type | Assay Gate focus |
|---------------|-------------------|------------------|
| **PoC** | Hypothesis validation | Did we learn what we needed? |
| **MVP** | Core value delivery | Does the minimum viable feature set work? |
| **Phase** | Incremental capability | Is this phase complete and releasable? |

## Product Manager agent

For **product-level** planning (vision, strategy, roadmap, business case, market analysis, WBS, product bootstrap), see the [Product Manager agent package](https://github.com/autowww/blueprints/blob/main/sdlc/methodologies/forge/product-manager/README.md). It provides:

- A Cursor rule (`forge-product-manager.mdc.template`) that orchestrates product strategy and bootstrap through dialog.
- A [product bootstrap flow](https://github.com/autowww/blueprints/blob/main/sdlc/methodologies/forge/product-manager/product-bootstrap-flow.md) for taking a new product from zero to first Charge.
- A [first charge template](https://github.com/autowww/blueprints/blob/main/sdlc/methodologies/forge/product-manager/first-charge.template.md) with pre-defined product bootstrap Sparks.

The Product Manager agent is **upstream** of `forge-planning` — it creates the strategic inputs (vision, roadmap, business case) that `forge-planning` then decomposes into Forge work units.

**Methodology orchestration (delivery lens):** For **phase-aware** Forge SDLC passes (A–F) — who to invoke, parallel vs sequential discipline runs, **merge** ownership, and **trace** outputs — see [`../orchestration/README.md`](../orchestration/README.md) and the Cursor workflow rule **`versona-forge-sdlc`** (not a substitute for **`forge-product-manager`** product authoring).

## PDLC connection

Product planning in Forge connects to PDLC phases:

- **P1–P2** (Discover/Validate) → generates the business drivers that become Ore
- **P3** (Plan & Commit) → defines Product Sparks and their scope
- **P4** (Launch) → Product Spark passes Assay Gate and ships
- **P5** (Grow) → learning feeds new Ore

See [`../FORGE-SDLC-PDLC-BRIDGE.md`](https://github.com/autowww/blueprints/blob/main/sdlc/methodologies/forge/FORGE-SDLC-PDLC-BRIDGE.md) for the full bridge.
