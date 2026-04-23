---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Forge SDLC orchestration

**Normative hub** for **who routes**, **who orchestrates** end-to-end methodology passes, **who merges** multi-lens output, and **who owns specialist judgment** (discipline §5), across SDLC phases **A–F**.

| Document | Purpose |
|----------|---------|
| [`FORGE-SDLC-ORCHESTRATION.md`](FORGE-SDLC-ORCHESTRATION.md) | Role boundaries, phase-aware contracts, merge/escalation rules, trace outputs, diagrams |
| [`workflows/phases.json`](workflows/phases.json) | Machine-readable phase descriptors (companion to the Markdown) |
| [`schema/workflow-phases-bundle.schema.json`](schema/workflow-phases-bundle.schema.json) | JSON Schema for `phases.json` |

**Cursor rule:** [`../versona/catalog/workflow/versona-forge-sdlc.mdc.template`](../versona/catalog/workflow/versona-forge-sdlc.mdc.template) — install as `versona-forge-sdlc.mdc` (included in **`sync --preset recommended`**).

**Supersession:** [`../standards/precedence.md`](../standards/precedence.md) — external / org controls override orchestration suggestions.

**Related:** [`../foundation-connection.md`](../foundation-connection.md) · [`../planning/README.md`](../planning/README.md) · [`../versona/VERSONA-FRAMEWORK.md`](../versona/VERSONA-FRAMEWORK.md) §6 · [`../versona/catalog/routing/versona-all.mdc.template`](../versona/catalog/routing/versona-all.mdc.template) · [`../versona/VERSONA-SKILL-MATRIX.md`](../versona/VERSONA-SKILL-MATRIX.md) §0

## Product vs project vs routing (short)

| Versona | Lens | Not this lens |
|---------|------|----------------|
| **`versona-product-management`** | **What** to build and **why** (strategy, roadmap, OKRs, market fit) | Delivery **when/who/how much** — that is **`versona-pm`** |
| **`versona-pm`** | **Whether** delivery is feasible (constraints, dependencies, RAID, gates) | Roadmap **prioritization** or vision — **`versona-product-management`** |
| **`versona-ba`** | **Requirements** quality, needs, AC, elicitation | Strategy trade-offs — **product-management**; **plan baselines** — **pm** |
| **`versona-all`** | **Who** to invoke across families | **Phase orchestration** — **`versona-forge-sdlc`**; **domain merge** — **`versona-family-*`** |
