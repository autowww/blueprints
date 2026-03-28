---
name: run-product-versona-session
description: >
  Run a Forge Product family Versona session (or Sampling demo) using blueprint
  templates: invokes the Product family aggregator or Product Management Versona
  for a §5-shaped review or shallow triage before deeper work.
---

# Run Product Versona session (Forge)

## When to use

- User asks for **product review**, **multi-lens pass**, **assumption / risk pass**, or **which Versona to invoke**.
- Before heavy WBS or commitment, when a **Product** discipline lens is needed.

## Steps

1. Confirm the work item (Ore / Ingot / Spark / pasted artifact) and phase.
2. Prefer **`versona-family-product`** when several product lenses may apply; otherwise **`versona-product-management`** or route with **`versona-all`**.
3. Ask the user to `@` the chosen `.mdc` rule (or apply the equivalent prompt). Follow **Suggested next Versonas** when present.
4. For a **quick demo only**, optionally use **Sampling** (`versona-sampling`) per [`tasklets/README.md`](../../../../methodologies/forge/tasklets/README.md).

## Install

Copy this folder to the project’s **`.cursor/skills/run-product-versona-session/`** (or merge into your skills library) so the agent can discover it when relevant.

## References

- [`versona/README.md`](../../../../methodologies/forge/versona/README.md)
- [`VERSONA-CONTRACT.md`](../../../../methodologies/forge/versona/VERSONA-CONTRACT.md) §5
- Product family: [`versona-family-product.mdc.template`](../../../../methodologies/forge/versona/catalog/discipline/product/family/versona-family-product.mdc.template)
