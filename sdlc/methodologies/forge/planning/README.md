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

## Documents

| File | Purpose |
|------|---------|
| [`PLANNING-FLOW.md`](PLANNING-FLOW.md) | Full pipeline from vision to daily Sparks |
| [`release-plan.template.md`](release-plan.template.md) | Forge release plan template (Product Spark) |
| [`poc-plan.template.md`](poc-plan.template.md) | PoC planning template |
| [`mvp-plan.template.md`](mvp-plan.template.md) | MVP planning template |
| [`phase-plan.template.md`](phase-plan.template.md) | Phase planning template |
| [`forge-planning.mdc.template`](forge-planning.mdc.template) | Cursor rule for guided planning |

## Product Spark

A **Product Spark** is a potentially shippable product iteration that may span multiple Forge iterations. It represents the coarsest grain of delivery planning in Forge:

| Product stage | Product Spark type | Assay Gate focus |
|---------------|-------------------|------------------|
| **PoC** | Hypothesis validation | Did we learn what we needed? |
| **MVP** | Core value delivery | Does the minimum viable feature set work? |
| **Phase** | Incremental capability | Is this phase complete and releasable? |

## Product Manager agent

For **product-level** planning (vision, strategy, roadmap, business case, market analysis, WBS, product bootstrap), see the [Product Manager agent package](../product-manager/README.md). It provides:

- A Cursor rule (`forge-product-manager.mdc.template`) that orchestrates product strategy and bootstrap through dialog.
- A [product bootstrap flow](../product-manager/product-bootstrap-flow.md) for taking a new product from zero to first Charge.
- A [first charge template](../product-manager/first-charge.template.md) with pre-defined product bootstrap Sparks.

The Product Manager agent is **upstream** of `forge-planning` — it creates the strategic inputs (vision, roadmap, business case) that `forge-planning` then decomposes into Forge work units.

## PDLC connection

Product planning in Forge connects to PDLC phases:

- **P1–P2** (Discover/Validate) → generates the business drivers that become Ore
- **P3** (Strategize) → defines Product Sparks and their scope
- **P4** (Launch) → Product Spark passes Assay Gate and ships
- **P5** (Grow) → learning feeds new Ore

See [`../FORGE-SDLC-PDLC-BRIDGE.md`](../FORGE-SDLC-PDLC-BRIDGE.md) for the full bridge.
