---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
content_id: forge.docs.blueprints.forge.sdlc-pdlc-bridge
canonical_owner: blueprints
primary_persona: engineering_leader
reader_stage: adopt
maturity: defined
evidence_level: canonical_doc
refresh_policy: on_claim_change
last_reviewed: '2026-07-03'
---

# Forge ↔ SDLC ↔ PDLC bridge

**Purpose:** Map how **Forge SDLC** connects to both the software delivery lifecycle (SDLC phases A–F) and the product development lifecycle (PDLC phases P1–P6). This bridge closes the gap between product discovery and daily execution.

For the **full** PDLC ↔ SDLC lifecycle bridge (plain-language comparisons, nested-loop view, artifact handoffs, metrics, and a worked example without Forge-specific mechanics), see **[PDLC ↔ SDLC bridge](https://forgesdlc.com/pdlc-sdlc-bridge.html)** on forgesdlc.com.

## 1. Canonical sources

| Domain | Source |
|--------|--------|
| **Forge** | [`https://forgesdlc.com/methodology-overview.html`](https://forgesdlc.com/methodology-overview.html), this package |
| **SDLC** | [`../../SDLC.md`](../../SDLC.md) — phases A–F, DoD, ceremonies |
| **PDLC** | [`../../../pdlc/PDLC.md`](../../../pdlc/PDLC.md) — phases P1–P6, stage gates |
| **PDLC ↔ SDLC** | [`../../../pdlc/PDLC-SDLC-BRIDGE.md`](../../../pdlc/PDLC-SDLC-BRIDGE.md) — cross-lifecycle alignment |

---

## 2. Comparison table

| Dimension | Forge SDLC | SDLC (phases A–F) | PDLC (phases P1–P6) |
|-----------|-----------|-------------------|---------------------|
| **Core question** | Is this idea refined, reviewed, evidenced, and releasable? | Are we building the product right? | Are we building the right product? |
| **Scope** | Iteration-level delivery methodology | Lifecycle-wide delivery phases | Product-wide discovery through sunset |
| **Primary owner** | Delivery team (all hats) | Engineering + delivery | Product + strategy |
| **Timeline** | 1–2 week iterations | Phase-gated (variable) | Months to years |
| **Success metric** | Spark throughput, Assay Gate pass rate, decision quality | Phase completion, DoD adherence | Product-market fit, adoption, revenue |
| **Risk focus** | Decision blind spots, premature commitment, release confidence | Technical debt, quality, schedule | Market risk, user adoption, viability |
| **Artifacts** | Ore, Ingots, Sparks, Charge, Ember Log, Assay evidence | Specs, ADRs, test plans, release notes | Vision, experiments, GTM, metrics |
| **Failure mode** | Unrefined Ore in execution; evidence-free releases | Phases skipped; DoD ignored | Building without validation; no learning loop |

---

## 3. When one is missing

| Scenario | Consequence |
|----------|-------------|
| Forge without SDLC awareness | Sparks lack phase context; quality gates are ad hoc; no lifecycle traceability |
| Forge without PDLC awareness | Ore pipeline disconnected from validated product needs; building the wrong thing precisely |
| SDLC without Forge | Standard delivery without discipline Versonas, decision memory, or evidence-based release rigor |
| PDLC without Forge | Product strategy exists but execution lacks the Ore→Spark refinement pipeline and daily focus |

---

## 4. Phase alignment

### Forge → SDLC phases A–F

In reader-facing ForgeSDLC copy, **meeting** is the preferred label for these events; the **Forge meetings** and mechanics in the middle column are the same events detailed in [`ceremonies-prescriptive.md`](ceremonies-prescriptive.md). See [`NAMING-REFERENCE.md`](NAMING-REFERENCE.md).

| SDLC Phase | Forge ceremony/mechanics | Forge artifacts |
|------------|--------------------------|-----------------|
| **A Discover** | Ore intake; `discover:` Sparks | Ore items, stakeholder notes |
| **B Specify** | Refinement (Ore → Ingot); `specify:` Sparks | Ingots with acceptance criteria |
| **C Design** | Planning (Ingot → Sparks); `design:` Sparks | Spark decomposition, ADRs |
| **D Build** | Charge execution; `build:` Sparks | Completed Sparks, PRs |
| **E Verify** | Assay Gate preparation; `verify:` Sparks | Test results, evidence package |
| **F Release** | Assay Gate pass → release; `release:` Sparks | Release notes, Assay evidence |

### Forge → PDLC phases P1–P6

| PDLC Phase | Forge touchpoint | Direction |
|------------|-----------------|-----------|
| **P1 Discover problem** | Feeds Ore pipeline with validated problems | PDLC → Forge |
| **P2 Validate solution** | Discipline Versona sessions validate feasibility; PoC planning | PDLC ↔ Forge |
| **P3 Plan & Commit** | Product Sparks (PoC/MVP/Phase) defined; Ingots scoped | PDLC → Forge |
| **P4 Launch** | Assay Gate ensures launch readiness; `release:` Sparks | Forge → PDLC |
| **P5 Grow** | Learning from released work feeds new Ore; metrics feed Versonas | Forge ↔ PDLC |
| **P6 Sunset** | Deprecation Sparks; migration Ore | Forge → PDLC |

---

## 5. Role mapping across domains

| Forge hat | SDLC role | PDLC role |
|-----------|-----------|-----------|
| **Product** | Phase A–B owner (backlog, specs) | P1–P3 primary; P5 feedback owner |
| **Engineering** | Phase C–E owner (build, verify) | P4 launch support; P5 scaling |
| **Challenge** | Cross-phase quality advocate | P2 feasibility validation |
| **Governance** | Phase E–F gatekeeper (verify, release) | P4 launch readiness; P6 compliance |

---

## 6. Artifact flow

```blueprint-diagram
key: swimlane
alt: Artifact flow
title: Forge cross-lifecycle artifacts
summary: How PDLC-validated intent flows through Forge artifacts into releases, with governed feedback reopening product learning.
node: Artifact flow
detail: Frames how Forge artifacts move between PDLC and SDLC on this bridge.
more: Ore, Ingots, Sparks, Charge, Ember Log, and Assay evidence are the Forge-side carriers that connect product strategy to daily delivery.
node: Lane A ──► handoff ──► shared outcome
detail: PDLC outputs enter the Ore pipeline and emerge as traceable, evidenced releases.
more: P1–P3 validated problems and P3 commitment artifacts hand off at Ore intake; Refinement, Planning, and Assay Gate produce Ingots, Sparks, and release evidence aligned to PDLC success criteria.
node: Lane B ──► inspect / adapt ──► feedback
detail: Forge inspects delivery and feeds learnings back into product work.
more: Review meetings, Ember Log decisions, and P5 adoption metrics reopen Ore intake and Versona sessions so teams adjust without losing decision memory.
fallback_ascii: |
  Artifact flow

  Lane A ──► handoff ──► shared outcome
  Lane B ──► inspect / adapt ──► feedback
```

---

## 7. Calibration / decision framework

| Signal | Invest more in Forge discipline | Lighten Forge discipline |
|--------|---------------------------------|--------------------------|
| Releases frequently have quality issues | Strengthen Assay Gate evidence; add Versonas | — |
| Decisions are revisited without context | Expand Ember Log practice | — |
| Team is slow despite clear requirements | — | Reduce ceremony overhead; shorter iterations |
| Stakeholder surprises at review | Strengthen Refinement and Versona sessions | — |
| Solo developer with stable product | — | Minimal ceremonies; AI Versonas; self-Assay |

---

## 8. Anti-patterns

| Anti-pattern | Bridge failure | Fix |
|--------------|---------------|-----|
| Ore pipeline disconnected from PDLC | Building features no one validated | Link Ore intake to PDLC P1–P3 outputs |
| Assay Gate ignores PDLC success metrics | Technically correct but product-wrong releases | Include PDLC P3 metrics in Assay Gate criteria |
| Versonas only check engineering concerns | Product and governance blind spots | Activate Product and Governance family Versonas |
| Ember Log not reviewed in PDLC retrospectives | Strategic decisions lost | Feed Ember Log insights to PDLC P5 learning loops |
| Forge iterations misaligned with PDLC milestones | Delivery cadence fights product cadence | Align Product Sparks with PDLC phase gates |

---

## 9. Worked example

**Scenario:** A team needs to add push notifications (PDLC P3 validated the need; P1–P2 confirmed user demand).

1. **Ore intake:** "Users want push notifications" enters as Ore (from PDLC P3 output).
2. **Refinement:** Product hat shapes Ore into Ingot: "Push notification system for engagement reminders" with acceptance criteria, constraints (FCM, APNs), and evidence-of-done.
3. **Versona session:** Architecture Versona flags scalability concern; Security Versona flags token storage risk. Both captured in Ember Log.
4. **Planning:** Ingot decomposed into Sparks:
   - `design: notification service architecture + ADR` (C phase)
   - `build: implement FCM integration` (D phase)
   - `build: implement APNs integration` (D phase)
   - `verify: integration tests for notification delivery` (E phase)
   - `specify: user preference settings` (B phase)
   - `release: changelog, feature flag rollout` (F phase)
5. **Daily execution:** Team works through Charge, completing 2–3 Sparks per day.
6. **Review:** Increment demonstrated; stakeholder feedback captured.
7. **Assay Gate:** Tests pass, acceptance met, security review done, rollback plan confirmed → PASS.
8. **Release:** Feature shipped; learning feeds PDLC P5 (adoption metrics, engagement data) → new Ore for improvements.

---

## 10. Related reading

| Doc | Why |
|-----|-----|
| [`forge.md`](https://forgesdlc.com/methodology-overview.html) | Forge methodology summary |
| [`../../SDLC.md`](../../SDLC.md) | Delivery phases A–F |
| [`../../../pdlc/PDLC.md`](../../../pdlc/PDLC.md) | Product phases P1–P6 |
| [`../../../pdlc/PDLC-SDLC-BRIDGE.md`](../../../pdlc/PDLC-SDLC-BRIDGE.md) | Cross-lifecycle bridge |
| [`../../../disciplines/README.md`](../../../disciplines/README.md) | Discipline hub (Versonas knowledge bases) |
| [`versona/README.md`](versona/README.md) | Versonas — discipline virtual personas |
| [`planning/README.md`](planning/README.md) | Product planning (PoC/MVP/Phased) |

## Executive capsule

**Purpose:** Map how **Forge SDLC** connects to both the software delivery lifecycle (SDLC phases A–F) and the product development lifecycle (PDLC phases P1–P6). This bridge closes the gap between product discovery and daily execution. Maturity: **defined**.

## Who this is for

Engineering leaders at the **adopt** stage. Skim the executive capsule first; agents should respect the page frontmatter contract.

## Evidence and maturity

Maturity: **defined**. Statements here reflect the owning repo (`blueprints`) at `last_reviewed`; treat anything not explicitly marked as demonstrated as design direction rather than a shipped guarantee.

## Trust boundary

Forge keeps humans in charge of promotion, approval, and release decisions; automation proposes and executes only within approved boundaries described here.

## How to use this page

Read top-to-bottom at your depth: capsule for the decision, mechanism for design, links below for the next step in your journey.

## The problem this solves

Teams adopting AI-assisted delivery need structure they can trust before they scale it. This page addresses that gap for its topic: it explains the situation the reader is in, the failure mode without the mechanism described here, and the outcome when it is applied.
