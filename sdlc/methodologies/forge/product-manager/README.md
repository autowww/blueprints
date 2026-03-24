# Product Manager — Forge orchestrating agent

The **Product Manager agent** is a Cursor rule that orchestrates product-level planning within Forge SDLC. It complements the existing Forge workflow agents (`forge-setup`, `forge-planning`, `forge-daily`) by adding a **product strategy layer** — guiding the user from business drivers through product bootstrap, roadmap decomposition, and Product Spark planning.

## When to use

| Scenario | Use this agent |
|----------|---------------|
| **New product / greenfield** | Run the [product bootstrap flow](product-bootstrap-flow.md) to create initial product artifacts, define the first Product Spark, and populate the first Charge |
| **New initiative on existing product** | Decompose a roadmap theme into Product Sparks, WBS, and Forge iterations |
| **Product planning session** | Walk through business drivers → Ore → Ingots → Sparks via dialog |
| **Roadmap refresh** | Re-evaluate priorities, update OKRs, assess competitive landscape |
| **Stage-gate review** | Prepare evidence for PDLC stage gates (G1–G5) |

## Relationship to other Forge agents

| Agent | Role | Scope |
|-------|------|-------|
| **`forge-setup`** | Configure Forge for a project | Team, hats, disciplines, config, directories |
| **`forge-planning`** | Decompose business drivers into Forge work | Business drivers → Ore → Product Sparks → iterations |
| **`forge-product-manager`** (this) | Orchestrate product strategy and bootstrap | Vision → market analysis → roadmap → WBS → first Charge → Spark planning |
| **`forge-daily`** | Daily execution within an iteration | Charge management, hat switching, Ember Log, journal |

The Product Manager agent is **upstream** of `forge-planning` — it creates the strategic inputs (vision, roadmap, business case) that `forge-planning` then decomposes into Forge work units.

## Relationship to Versonas

The **Product Management Versona** (`versona-product-management.mdc.template`) is a **challenge agent** — it questions and stress-tests product decisions. The Product Manager agent is an **orchestrator** — it guides the user through creating product artifacts and planning work. They are complementary:

- The Product Manager agent **creates** artifacts (vision, roadmap, business case, WBS, Charges).
- The Product Management Versona **challenges** those artifacts (is the strategy coherent? are priorities defensible?).

The Product Manager agent will suggest invoking the Product Management Versona at appropriate decision points.

## Files in this package

| File | Purpose |
|------|---------|
| [`forge-product-manager.mdc.template`](forge-product-manager.mdc.template) | Cursor rule template — copy to `.cursor/rules/` in consuming repo |
| [`product-bootstrap-flow.md`](product-bootstrap-flow.md) | Step-by-step guide for bootstrapping a new product through dialog |
| [`first-charge.template.md`](first-charge.template.md) | Pre-defined first Product Charge with bootstrap Sparks |

## Adoption

1. Copy `forge-product-manager.mdc.template` to `.cursor/rules/forge-product-manager.mdc` in your repo.
2. Update `globs:` to match your project's product documentation paths.
3. Use it when starting a new product, launching a new initiative, or refreshing product strategy.
4. Follow the [product bootstrap flow](product-bootstrap-flow.md) for greenfield projects.
5. Use the [first charge template](first-charge.template.md) to populate your first Forge Charge with product bootstrap Sparks.

## References

- [`PRODUCT-MANAGEMENT.md`](../../../../disciplines/product/product-management/PRODUCT-MANAGEMENT.md) — body of knowledge
- [`PRODMGMT-SDLC-PDLC-BRIDGE.md`](../../../../disciplines/product/product-management/PRODMGMT-SDLC-PDLC-BRIDGE.md) — lifecycle bridge
- [`PLANNING-FLOW.md`](../planning/PLANNING-FLOW.md) — Forge planning pipeline
- [`FORGE-SDLC-PDLC-BRIDGE.md`](../FORGE-SDLC-PDLC-BRIDGE.md) — Forge lifecycle bridge
- [`versona-product-management.mdc.template`](../versona/versona-product-management.mdc.template) — Product Management Versona
