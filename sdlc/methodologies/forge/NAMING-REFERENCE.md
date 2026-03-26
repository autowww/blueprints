# Forge & planning — naming reference

Quick map of **terms**, **plain meaning**, and **where each is defined** in this blueprint (`blueprints/` repo). Paths are repo-relative from the **blueprints** root.

| Term | Meaning (short) | Where stored / documented |
|------|------------------|---------------------------|
| **Product Spark** | Potentially shippable **product** slice: PoC, MVP, or phased increment — not the same as a Forge **Spark** (task). | [`planning/PLANNING-FLOW.md`](planning/PLANNING-FLOW.md) · [`process-and-flows.md`](process-and-flows.md) · [`product-manager/forge-product-manager.mdc.template`](product-manager/forge-product-manager.mdc.template) (§ Forge vocabulary) |
| **Forge iteration** | Delivery cycle (often 1–2 weeks) **inside** a Product Spark; scope and evidence assessed at the boundary. | [`planning/PLANNING-FLOW.md`](planning/PLANNING-FLOW.md) · [`process-and-flows.md`](process-and-flows.md) |
| **Ore** | Raw, unrefined intake — ideas, problems, opportunities — **before** refinement. | [`process-and-flows.md`](process-and-flows.md) · [`planning/PLANNING-FLOW.md`](planning/PLANNING-FLOW.md) · [`planning/README.md`](planning/README.md) |
| **Ingot** | Refined, **plannable** work (often story-level) with acceptance criteria. | [`process-and-flows.md`](process-and-flows.md) · [`planning/PLANNING-FLOW.md`](planning/PLANNING-FLOW.md) |
| **Forge Spark** | Smallest **delivery** unit: executable task (~1–4 h), often **phase-prefixed** (`discover:`, `specify:`, …). Maps to WBS **task**. **Not** an exploration spike. | [`process-and-flows.md`](process-and-flows.md) (§ Spark = Task, exploration spike contrast) · [`planning/PLANNING-FLOW.md`](planning/PLANNING-FLOW.md) · [`README.md`](README.md) · [`foundation-connection.md`](foundation-connection.md) |
| **Charge** | **Today’s** selected Forge Sparks (daily commitment). | [`process-and-flows.md`](process-and-flows.md) · [`daily/README.md`](daily/README.md) · [`daily/charge.template.md`](daily/charge.template.md) |
| **Assay Gate** | Evidence-based **release** decision (market-ready vs code-only, etc.). | [`planning/PLANNING-FLOW.md`](planning/PLANNING-FLOW.md) · [`product-manager/forge-product-manager.mdc.template`](product-manager/forge-product-manager.mdc.template) · [`../../templates/forge/assay-gate.template.md`](../../templates/forge/assay-gate.template.md) |
| **Ember Log** | **Decision** journal — trade-offs, risk acceptance, scope/priority changes (`ember-logs/YYYY-MM-DD.md`). | [`daily/README.md`](daily/README.md) · [`scripts/forge-ember.sh`](scripts/forge-ember.sh) · [`../../templates/forge/ember-log-entry.template.md`](../../templates/forge/ember-log-entry.template.md) · [`versona/VERSONA-FRAMEWORK.md`](versona/VERSONA-FRAMEWORK.md) |
| **Day journal** | Dated operational log (e.g. `forge/journal/YYYY-MM-DD.md`) — sessions, challenges, outcomes. | [`daily/day-journal.template.md`](daily/day-journal.template.md) · [`versona/VERSONA-FRAMEWORK.md`](versona/VERSONA-FRAMEWORK.md) |
| **Exploration spike** / **discipline spike** | Time-boxed **learning**; outcome is evidence + record; **not** a Forge Spark. | [`versona/DISCIPLINE-SPIKE.md`](versona/DISCIPLINE-SPIKE.md) · [`process-and-flows.md`](process-and-flows.md) |
| **Product spike** (informal) | Colloquial: discipline spike on **product/strategy**; use `spike_discipline` + Product Management lens — **not** a fourth official type, **not** a Product Spark. | [`versona/DISCIPLINE-SPIKE.md`](versona/DISCIPLINE-SPIKE.md) §1 |
| **Milestone (`M1`…)** | WBS / roadmap milestone; often aligns with one **Product Spark**. | [`planning/PLANNING-FLOW.md`](planning/PLANNING-FLOW.md) (§ Mapping to WBS) · [`../../../pdlc/templates/WBS.template.md`](../../../pdlc/templates/WBS.template.md) · [`../../templates/ROADMAP.template.md`](../../templates/ROADMAP.template.md) |
| **Theme / Epic / Story / Task** | WBS hierarchy; **Task** ↔ Forge **Spark** when using shared IDs (e.g. `M1E1S1T1`). | [`planning/PLANNING-FLOW.md`](planning/PLANNING-FLOW.md) · [`../../../pdlc/templates/WBS.template.md`](../../../pdlc/templates/WBS.template.md) · [`product-manager/product-bootstrap-flow.md`](product-manager/product-bootstrap-flow.md) |
| **Product hat** (and other hats) | **Product** vs **Engineering** vs **Challenge** vs **Governance** perspective when deciding. | [`roles.md`](roles.md) · [`versona/catalog/discipline/product/versona-product-management.mdc.template`](versona/catalog/discipline/product/versona-product-management.mdc.template) (baseline) |
| **Versona** | Discipline **challenge** agent (structured concern report); templates under `versona/catalog/`. | [`versona/README.md`](versona/README.md) · [`versona/VERSONA-CONTRACT.md`](versona/VERSONA-CONTRACT.md) · [`versona/VERSONA-FRAMEWORK.md`](versona/VERSONA-FRAMEWORK.md) |
| **Forge Product Manager** (agent) | Dialog agent: bootstrap, roadmap → WBS → Product Spark → Sparks → Charge (orchestration). | [`product-manager/forge-product-manager.mdc.template`](product-manager/forge-product-manager.mdc.template) · [`product-manager/product-bootstrap-flow.md`](product-manager/product-bootstrap-flow.md) · [`product-manager/README.md`](product-manager/README.md) |
| **Product Management Versona** | Challenge-only: strategy, roadmap coherence, Product Spark fit, Assay — **not** BA/PM-governance/UX/SE scope. | [`versona/catalog/discipline/product/versona-product-management.mdc.template`](versona/catalog/discipline/product/versona-product-management.mdc.template) |
| **`forge-logs/`** | Spark-level notes, DoD, journals; **Versona** sessions under `forge-logs/versona/<actor>/<session-id>/`. | [`process-and-flows.md`](process-and-flows.md) · [`versona/VERSONA-FRAMEWORK.md`](versona/VERSONA-FRAMEWORK.md) |
| **Work item kind** (`work_item_kind`) | Session/manifest: e.g. `spark`, `spike_discipline`, `spike_general`. | [`versona/VERSONA-FRAMEWORK.md`](versona/VERSONA-FRAMEWORK.md) · [`../../templates/forge/versona-session.template.md`](../../templates/forge/versona-session.template.md) · [`../../templates/forge/session.manifest.yaml.template`](../../templates/forge/session.manifest.yaml.template) |
| **Tracking spine** (commits ↔ work units) | Methodology-neutral model: contributors, events, linkage — supports traceability alongside Forge. | [`../../templates/sdlc/TRACKING-FOUNDATION.md`](../../templates/sdlc/TRACKING-FOUNDATION.md) · [`foundation-connection.md`](foundation-connection.md) |

## Related

- Lifecycle bridge (Forge ↔ PDLC ↔ SDLC): [`FORGE-SDLC-PDLC-BRIDGE.md`](FORGE-SDLC-PDLC-BRIDGE.md)
- PMI-style phase map (problem → delivery): [`PRODUCT-DELIVERY-FORGE-IPE.md`](PRODUCT-DELIVERY-FORGE-IPE.md)
- Forge package index: [`README.md`](README.md)
- Published overview (external): [forgesdlc.com methodology overview](https://forgesdlc.com/methodology-overview.html)

---

*Blueprint reference — update when planning or Versona contracts change.*
