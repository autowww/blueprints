# Forge & planning — naming reference

Quick map of **terms**, **plain meaning**, and **where each is defined** in this blueprint (`blueprints/` repo). Paths are repo-relative from the **blueprints** root.

| Term | Meaning (short) | Where stored / documented |
|------|------------------|---------------------------|
| **Product Spark** | Potentially shippable **product** slice: PoC, MVP, or phased increment — **not** the same as a Forge **Spark** (task). **Aliases** (same meaning, contextual): **release slice**, **product increment**. | [`planning/PLANNING-FLOW.md`](planning/PLANNING-FLOW.md) · [`process-and-flows.md`](process-and-flows.md) · [`product-manager/forge-product-manager.mdc.template`](product-manager/forge-product-manager.mdc.template) (§ Forge vocabulary) |
| **Meeting** | Scheduled, accountable **team** collaboration (daily sync, refinement, planning, review, retro, Assay Gate). Preferred **public** label for Forge events in prescriptive docs. | [`ceremonies-prescriptive.md`](ceremonies-prescriptive.md) · [`foundation-connection.md`](foundation-connection.md) |
| **Ceremony** | Blueprint **foundation** term: recurring collaboration mapped to **intent types C1–C6** in [`SDLC.md`](../../SDLC.md). Names the **same** events as **meetings** when describing foundation fit. | [`../ceremonies/ceremony-foundation.md`](../ceremonies/ceremony-foundation.md) · [`ceremonies-prescriptive.md`](ceremonies-prescriptive.md) |
| **Why** (vs **For what**) | **Why** = rationale, motivation, problem framing. **For what** = beneficiary, outcome, target decision, or practical purpose. Keep both distinct in meeting design—do not merge into one vague field. | [`ceremonies-prescriptive.md`](ceremonies-prescriptive.md) (preamble) |
| **Forge iteration** | Delivery cycle (often 1–2 weeks) **inside** a Product Spark; scope and evidence assessed at the boundary. | [`planning/PLANNING-FLOW.md`](planning/PLANNING-FLOW.md) · [`process-and-flows.md`](process-and-flows.md) |
| **Ore** | Raw, unrefined intake — ideas, problems, opportunities — **before** refinement. | [`process-and-flows.md`](process-and-flows.md) · [`planning/PLANNING-FLOW.md`](planning/PLANNING-FLOW.md) · [`planning/README.md`](planning/README.md) |
| **Ingot** | Refined, **plannable** work (often story-level) with acceptance criteria. | [`process-and-flows.md`](process-and-flows.md) · [`planning/PLANNING-FLOW.md`](planning/PLANNING-FLOW.md) |
| **Forge Spark** | Smallest **delivery** unit: executable task (~1–4 h), often **phase-prefixed** (`discover:`, `specify:`, …). Maps to WBS **task**. **Not** an exploration spike. | [`process-and-flows.md`](process-and-flows.md) (§ Spark = Task, exploration spike contrast) · [`planning/PLANNING-FLOW.md`](planning/PLANNING-FLOW.md) · [`README.md`](README.md) · [`foundation-connection.md`](foundation-connection.md) |
| **Charge** | **Today’s** selected Forge Sparks (daily commitment). | [`process-and-flows.md`](process-and-flows.md) · [`daily/README.md`](daily/README.md) · [`daily/charge.template.md`](daily/charge.template.md) |
| **Assay Gate** | Evidence-based **release** decision (market-ready vs code-only, etc.). | [`planning/PLANNING-FLOW.md`](planning/PLANNING-FLOW.md) · [`product-manager/forge-product-manager.mdc.template`](product-manager/forge-product-manager.mdc.template) · [`../../templates/forge/assay-gate.template.md`](../../templates/forge/assay-gate.template.md) |
| **Ember Log** | **Decision** journal — trade-offs, risk acceptance, scope/priority changes (`ember-logs/YYYY-MM-DD.md`). | [`daily/README.md`](daily/README.md) · [`scripts/forge-ember.sh`](scripts/forge-ember.sh) · [`../../templates/forge/ember-log-entry.template.md`](../../templates/forge/ember-log-entry.template.md) · [`versona/VERSONA-FRAMEWORK.md`](versona/VERSONA-FRAMEWORK.md) |
| **Day journal** | Dated operational log (e.g. `forge/journal/YYYY-MM-DD.md`) — sessions, outcomes. | [`daily/day-journal.template.md`](daily/day-journal.template.md) · [`versona/VERSONA-FRAMEWORK.md`](versona/VERSONA-FRAMEWORK.md) |
| **Exploration spike** / **discipline spike** | Time-boxed **learning**; outcome is evidence + record; **not** a Forge Spark. | [`versona/DISCIPLINE-SPIKE.md`](versona/DISCIPLINE-SPIKE.md) · [`process-and-flows.md`](process-and-flows.md) |
| **Product spike** (informal) | Colloquial: discipline spike on **product/strategy**; use `spike_discipline` + Product Management lens — **not** a fourth official type, **not** a Product Spark. | [`versona/DISCIPLINE-SPIKE.md`](versona/DISCIPLINE-SPIKE.md) §1 |
| **Milestone (`M1`…)** | WBS / roadmap milestone; often aligns with one **Product Spark**. | [`planning/PLANNING-FLOW.md`](planning/PLANNING-FLOW.md) (§ Mapping to WBS) · [`../../../pdlc/templates/WBS.template.md`](../../../pdlc/templates/WBS.template.md) · [`../../templates/ROADMAP.template.md`](../../templates/ROADMAP.template.md) |
| **Theme / Epic / Story / Task** | WBS hierarchy; **Task** ↔ Forge **Spark** when using shared IDs (e.g. `M1E1S1T1`). | [`planning/PLANNING-FLOW.md`](planning/PLANNING-FLOW.md) · [`../../../pdlc/templates/WBS.template.md`](../../../pdlc/templates/WBS.template.md) · [`product-manager/product-bootstrap-flow.md`](product-manager/product-bootstrap-flow.md) |
| **Product hat** (and other hats) | **Product** vs **Engineering** vs **Challenge** vs **Governance** perspective when deciding. | [`roles.md`](roles.md) · [`versona/catalog/discipline/product/versona-product-management.mdc.template`](versona/catalog/discipline/product/versona-product-management.mdc.template) (baseline) |
| **Versona** | Discipline **virtual persona** (§5 structured concern report when used); templates under `versona/catalog/`. | [`versona/README.md`](versona/README.md) · [`versona/VERSONA-CONTRACT.md`](versona/VERSONA-CONTRACT.md) · [`versona/VERSONA-FRAMEWORK.md`](versona/VERSONA-FRAMEWORK.md) |
| **Versona session** | One interaction with a Versona—folder under `forge-logs/versona/<actor>/<session-id>/`; may include several **activities**. | [`versona/VERSONA-FRAMEWORK.md`](versona/VERSONA-FRAMEWORK.md) §1 · [`process-and-flows.md`](process-and-flows.md) |
| **Challenge pass** | Informal name for a **§5-shaped** discipline review (pressure-test); one possible session/activity type—not what “Versona” means globally. | [`versona/VERSONA-FRAMEWORK.md`](versona/VERSONA-FRAMEWORK.md) §1 · [`versona/VERSONA-CONTRACT.md`](versona/VERSONA-CONTRACT.md) §5 |
| **Forge Product Manager** (agent) | Dialog agent: bootstrap, roadmap → WBS → Product Spark → Sparks → Charge (orchestration). Uses **Roadmap Definition of Ready** before WBS; suggests a Product Management Versona session after roadmap draft. | [`product-manager/forge-product-manager.mdc.template`](product-manager/forge-product-manager.mdc.template) · [`product-manager/product-bootstrap-flow.md`](product-manager/product-bootstrap-flow.md) · [`product-manager/README.md`](product-manager/README.md) |
| **Product Management Versona** | **Template scope** (not the global Versona definition): challenge-oriented **product-strategy** pass—strategy, roadmap coherence (incl. roadmap DoR), Product Spark fit, Assay — **not** BA/PM-governance/UX/SE scope. Output adds **Suggested next Versonas** (see [`versona/VERSONA-CONTRACT.md`](versona/VERSONA-CONTRACT.md) §5). | [`versona/catalog/discipline/product/versona-product-management.mdc.template`](versona/catalog/discipline/product/versona-product-management.mdc.template) · [`versona/catalog/workflow/versona-roadmap-gate.mdc.template`](versona/catalog/workflow/versona-roadmap-gate.mdc.template) (optional gate) |
| **`forge-logs/`** | Spark-level notes, DoD, journals; **Versona** sessions under `forge-logs/versona/<actor>/<session-id>/`. | [`process-and-flows.md`](process-and-flows.md) · [`versona/VERSONA-FRAMEWORK.md`](versona/VERSONA-FRAMEWORK.md) |
| **Work item kind** (`work_item_kind`) | Session/manifest: e.g. `spark`, `spike_discipline`, `spike_general`. | [`versona/VERSONA-FRAMEWORK.md`](versona/VERSONA-FRAMEWORK.md) · [`../../templates/forge/versona-session.template.md`](../../templates/forge/versona-session.template.md) · [`../../templates/forge/session.manifest.yaml.template`](../../templates/forge/session.manifest.yaml.template) |
| **Tracking spine** (commits ↔ work units) | Methodology-neutral model: contributors, events, linkage — supports traceability alongside Forge. | [`../../templates/sdlc/TRACKING-FOUNDATION.md`](../../templates/sdlc/TRACKING-FOUNDATION.md) · [`foundation-connection.md`](foundation-connection.md) |

## Why vs For what

**Why** = rationale, motivation, problem framing. **For what** = beneficiary, outcome, target decision, practical purpose. In prescriptive meeting design, keep both explicit—do not collapse into one vague “purpose” field. (Summary also appears in the table above.)

## Meetings vs ceremonies vs Versona sessions

These are **not** three competing “object types.” **Meetings** are what goes on the team calendar and carries human accountability. **Ceremonies** are how this blueprint ties those same events to **C1–C6** intents. **Versona sessions** are bounded discipline work (folder under `forge-logs/versona/`, one or more activities)—including challenge passes, drafting, and spikes—not a replacement for daily sync, retro, or gates.

## Seven-phase benchmark vs Forge PDLC (P1–P6)

External literature often uses a **seven-phase** product-development **benchmark** (e.g. discovery → scoping → business case → design/prototype → development → test/validate → launch/learn). Forge **does not** claim a universal seven-phase standard; it publishes **P1–P6** in [`PDLC.md`](../../../pdlc/PDLC.md), with **SDLC** (Discover / Prioritize → … → Release) as the **Build & release engine** nested after P3—see the **SDLC — Build & release** subsection there. Use this table when **comparing** to seven-phase models; avoid implying Forge has exactly seven **public** PDLC phases.

| Benchmark (7-phase style) | Nearest Forge anchor |
|---------------------------|----------------------|
| Discovery | **P1** Discover problem; overlaps **SDLC** Discover / Prioritize when validated work enters the delivery backlog |
| Scoping / screening | **P1** exit / **P2** Validate solution entry |
| Business case / planning | **P3** Plan & Commit |
| Design / prototype | **P2** (prototypes, experiments) + **SDLC** Design (C) |
| Development | **SDLC** Build (D) |
| Test and validate | **SDLC** Verify (E); **P2** evidence for solution fit |
| Launch and learn | **SDLC** Release (F) → **P4** Launch → **P5** Grow |

**Note:** **P6** Sunset, dual-track overlap, and full obligations live in [`PDLC.md`](../../../pdlc/PDLC.md).

## Related

- Lifecycle bridge (Forge ↔ PDLC ↔ SDLC): [`FORGE-SDLC-PDLC-BRIDGE.md`](FORGE-SDLC-PDLC-BRIDGE.md)
- PMI-style phase map (problem → delivery): [`PRODUCT-DELIVERY-FORGE-IPE.md`](PRODUCT-DELIVERY-FORGE-IPE.md)
- Forge package index: [`README.md`](README.md)
- Published overview (external): [forgesdlc.com methodology overview](https://forgesdlc.com/methodology-overview.html)

---

*Blueprint reference — update when planning or Versona contracts change.*
