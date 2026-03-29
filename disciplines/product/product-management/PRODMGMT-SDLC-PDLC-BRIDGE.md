# Product Management ↔ SDLC ↔ PDLC bridge

## Purpose

This document closes the **strategy-execution gap** between product management and the two lifecycle frameworks it operates across:

- **PDLC** (Product Development Life Cycle) — "Are we building the **right product**?"
- **SDLC** (Software Development Life Cycle) — "Are we building the product **right**?"
- **Product Management** — "Is our **strategy coherent**, our **priorities defensible**, and our **market position** sound?"

Product management is the discipline that owns the "what and why" across the full product lifetime. It operates primarily in PDLC (P1–P3 strategy, P5 growth) and guides SDLC delivery through prioritization, outcome definition, and stakeholder alignment.

**Canonical sources:** [`PRODUCT-MANAGEMENT.md`](PRODUCT-MANAGEMENT.md) (this package) · [`PDLC.md`](../../../pdlc/PDLC.md) · [`SDLC.md`](../../../sdlc/SDLC.md) · [`PDLC-SDLC-BRIDGE.md`](../../../pdlc/PDLC-SDLC-BRIDGE.md).

---

## Document map

| Section | Contents |
|---------|----------|
| [1. Comparison table](#1-comparison-table) | Product Management vs SDLC vs PDLC — scope, ownership, metrics, risks |
| [2. When one is missing](#2-when-one-is-missing) | Consequences of practicing one domain without the others |
| [3. Product management across the lifecycle](#3-product-management-across-the-lifecycle) | Activities and outputs mapped to PDLC P1–P6 and SDLC A–F |
| [4. Role mapping](#4-role-mapping) | Who owns what at each phase |
| [5. Artifact flow](#5-artifact-flow) | Handoffs between product management, SDLC, and PDLC |
| [6. Calibration](#6-calibration) | When to invest more or less in product management rigor |
| [7. Anti-patterns](#7-anti-patterns) | Common failures when product management is missing or misapplied |
| [8. Worked example](#8-worked-example) | End-to-end scenario |
| [9. Related reading](#9-related-reading) | Authoritative docs across packages |

---

## 1. Comparison table

| Dimension | Product Management | SDLC | PDLC |
|-----------|-------------------|------|------|
| **Core question** | Is our strategy coherent? Are priorities defensible? Is the market position sound? | How do we build this correctly? | Should we build this? Does it create the right outcomes? |
| **Scope** | Vision → strategy → roadmap → prioritization → market positioning → discovery → growth metrics | Requirements → design → implementation → verification → release (A–F) | Problem discovery → validation → strategy → launch → growth → sunset (P1–P6) |
| **Primary owner** | Product manager / CPO / product trio | Delivery team; Owner and Implementer per SDLC | Product manager / product trio; overlaps with PM ownership |
| **Timeline** | Product lifetime; continuous re-evaluation | Sprint, iteration, or release cycle | Product lifetime (months to years) |
| **Success metric** | Product-market fit signals, North Star metric, OKR attainment, NRR, roadmap outcome delivery | Velocity, defect rate, DORA metrics, CI pass rate | Adoption, retention, NPS, revenue, outcome KPIs |
| **Key artifacts** | Product vision, roadmap, OKRs, market analysis, competitive analysis, business case, experiment log, stakeholder updates | Specs, code, tests, release notes | Research synthesis, experiments, stage-gate reviews, GTM plan |
| **Risk focus** | Strategic risk — wrong market, wrong positioning, wrong priorities, missed timing | Technical risk — bugs, performance, security | Market and outcome risk — desirability, viability, fit |
| **Failure mode** | Incoherent strategy; feature factory without outcome connection; priorities that shift without rationale | Late or low-quality delivery | Right product invisible; launch without strategy |

---

## 2. When one is missing

| Scenario | What happens |
|----------|-------------|
| **Product Management without PDLC** | PM makes strategic decisions without structured discovery or stage gates — gut-feel roadmaps, no experiment discipline, investment without evidence |
| **Product Management without SDLC** | Strategy is sound but execution is chaotic — priorities ship late, quality is inconsistent, no DoD or traceability |
| **PDLC without Product Management** | Lifecycle stages exist but nobody owns strategy, prioritization, or stakeholder alignment — committees decide, roadmap drifts, outcomes unmeasured |
| **SDLC without Product Management** | Engineering delivers efficiently but builds whatever is asked — feature factory, no outcome connection, no market awareness |
| **PDLC + SDLC, weak Product Management** | Discovery and delivery processes exist but priorities are politically driven, roadmap is a wish list, metrics aren't connected to strategy |
| **All three practiced** | Validated problems become strategically prioritized work, built with quality, measured against outcomes, and iterated based on evidence |

---

## 3. Product management across the lifecycle

| Phase | PM role | Key activities | Outputs |
|-------|---------|----------------|---------|
| **P1 Discover** | **Problem space owner** | Customer interviews, market analysis, competitive scanning, opportunity identification, JTBD analysis | Problem statement, market analysis, competitive landscape, opportunity assessment |
| **P2 Validate** | **Hypothesis driver** | Solution ideation, experiment design, prototype-driven validation, feasibility triage with Engineering | Experiment log, validated hypotheses, PMF early signals, feasibility assessment |
| **P3 Plan & Commit** | **Strategy owner** | Vision articulation, roadmap creation, OKR definition, business case, pricing/positioning, GTM strategy, stakeholder alignment | Product vision, roadmap, OKRs, business case, GTM plan, stage-gate evidence |
| **A Discover** | **Priority setter** | Feed validated Ore into backlog, provide context and rationale, define outcome goals for iteration | Prioritized backlog, outcome goals, acceptance criteria context |
| **B Specify** | **Trade-off arbiter** | Resolve scope questions, clarify priorities when requirements conflict, review specs for strategic alignment | Scope decisions, priority rationale, strategic alignment sign-off |
| **C Design** | **Value guardian** | Ensure design decisions serve product strategy; challenge over-engineering or under-investment | Design trade-off decisions, value-alignment reviews |
| **D Build** | **Context provider** | Answer "why" questions; unblock decisions that require product judgment | Just-in-time context, priority adjustments |
| **E Verify** | **Acceptance owner** | Validate that delivered work meets product intent (not just spec compliance) | Acceptance decisions, gap identification |
| **F Release** | **Release decision maker** | Go/no-go based on product readiness (not just technical readiness); coordinate with GTM | Release authorization, launch coordination |
| **P4 Launch** | **Launch orchestrator** | Coordinate GTM execution, sales enablement, support readiness, customer communication | Launch report, initial metrics baseline |
| **P5 Grow** | **Growth strategist** | Analyze metrics, run experiments, iterate roadmap, manage expansion and retention | Metric dashboards, experiment outcomes, roadmap updates, churn analysis |
| **P6 Sunset** | **Lifecycle steward** | Assess lifecycle stage, plan migration/retirement, communicate transparently | Sunset plan, migration guide, stakeholder comms |

---

## 4. Role mapping

| Phase(s) | Product Management stance | PDLC accountability | SDLC accountability | Archetype |
|----------|--------------------------|---------------------|---------------------|-----------|
| **P1–P2** | **Discovery lead** | PM, UX Researcher, data | — (upstream of formal SDLC) | Demand & value |
| **P3** | **Strategy and commitment** | PM, executive sponsor | Owner (entering SDLC with priorities) | Steer & govern; Demand & value |
| **A–B** | **Priority and context** | — | Owner (acceptance); Implementer (specs) | Build & integrate |
| **C–D** | **Value guardrail** | — | Implementer (architecture, code) | Build & integrate |
| **E–F** | **Acceptance and release** | — | Implementer (tests); Owner (go/no-go) | Assure & ship |
| **P4** | **Launch owner** | PM, GTM, Sales | Overlaps F | Demand & value |
| **P5** | **Growth and iteration** | PM, Analytics, CS | Owner (iteration A–F) | Flow & improvement |
| **P6** | **Sunset steward** | PM, Executive, Legal | Implementer (migration, decommission) | Steer & govern |

### Product Management vs adjacent roles

| Dimension | Product Management | Business Analysis | Project Management |
|-----------|-------------------|-------------------|--------------------|
| **Primary focus** | Market opportunity, product strategy, user value, outcomes | Requirements quality, stakeholder needs completeness, solution fit | Delivery within constraints (time, cost, scope, risk) |
| **Key question** | "Is this the right thing for the market?" | "Are requirements complete and traceable?" | "Will we deliver on time and budget?" |
| **Techniques** | User interviews, OKRs, roadmap prioritization, A/B tests, competitive analysis | Use cases, data modeling, elicitation, traceability | WBS, Gantt, EVM, risk register, RACI |
| **Output** | Vision, roadmap, success metrics, experiment log | Requirements package, traceability matrix, business case | Project plan, schedule, budget, status reports |
| **Overlap** | All three share stakeholder management, prioritization, and communication | BA and PM both elicit stakeholder input | PM and ProjMgr both manage scope — but from different perspectives |

---

## 5. Artifact flow

### Product Management → PDLC

| PM artifact | PDLC destination | Usage |
|-------------|-------------------|-------|
| Market analysis | P1: evidence base | Validates problem is worth solving |
| Competitive analysis | P1–P3: positioning | Informs strategy and differentiation |
| Business case | P3: stage-gate review (G3) | Justifies investment decision |
| Product vision and OKRs | P3: strategy artifacts | Aligns team and stakeholders |
| Roadmap | P3–P5: planning horizon | Sequences initiatives against strategy |
| Experiment outcomes | P5: iteration decisions | Evidence for continue/pivot/kill |

### Product Management → SDLC

| PM artifact | SDLC destination | Usage |
|-------------|-------------------|-------|
| Prioritized backlog | Phase A: discovery input | What to build next and why |
| Outcome goals | Phase A–B: acceptance context | Why this work matters; what success looks like |
| Scope decisions | Phase B: specification boundaries | What is in/out of scope |
| Release authorization | Phase F: go/no-go | Product readiness (beyond technical readiness) |
| Competitive context | Phase B–C: design constraints | "Must match competitor X on Y" or "differentiate via Z" |

### PDLC / SDLC → Product Management (feedback)

| Source | PM usage |
|--------|----------|
| P1 customer research | Informs problem framing and opportunity identification |
| P2 experiment results | Validates or invalidates hypotheses; shapes strategy |
| SDLC Phase E test results | Confirms delivery matches intent |
| P5 usage analytics | Drives roadmap iteration, churn analysis, growth decisions |
| P5 customer feedback / CS signals | New opportunities, retention insights, satisfaction trends |
| P6 lifecycle assessment | Triggers sunset planning or reinvention |

---

## 6. Calibration

### By product stage

| Stage | PM investment | Emphasis |
|-------|---------------|----------|
| **Pre-PMF (PoC/MVP)** | **High on discovery, moderate on process** | Problem validation, rapid experimentation, PMF signal detection; lightweight roadmap; avoid premature process |
| **Post-PMF (Growth)** | **High across the board** | Outcome-driven roadmap, OKRs, competitive positioning, pricing optimization, growth experiments, retention analysis |
| **Mature** | **High on efficiency, moderate on discovery** | Optimization, margin improvement, platform investments, sunset planning; selective discovery for adjacent opportunities |
| **Sunset** | **Focused on transition** | Migration planning, customer communication, regulatory compliance, knowledge preservation |

### By team size

| Context | PM approach |
|---------|------------|
| **Solo / tiny startup** | Founder is PM; formalize only what's needed for investor/stakeholder communication; focus on discovery and PMF signals |
| **Small team (3–8)** | Dedicated or part-time PM; lightweight roadmap; weekly discovery; RICE or ICE for prioritization |
| **Medium team (8–25)** | Full-time PM; outcome-driven roadmap; OKRs; regular competitive analysis; formal stakeholder updates |
| **Large / multi-team** | PM team or product org; portfolio management; cross-team prioritization; strategic planning cycles; product operations |

### By market context

| Context | PM emphasis |
|---------|------------|
| **New category** | Heavy discovery; positioning from scratch; education-heavy GTM |
| **Established category** | Competitive differentiation; feature parity decisions; switching cost strategy |
| **Regulated market** | Compliance as product constraint; regulatory landscape monitoring; longer validation cycles |
| **Platform / ecosystem** | Developer experience; API strategy; partner management; network effect cultivation |

---

## 7. Anti-patterns

| Anti-pattern | Description | Symptom | Fix |
|--------------|-------------|---------|-----|
| **Feature factory** | PM is a ticket router, not a strategist; roadmap is a wish list of stakeholder requests | No outcome metrics; backlog grows faster than it shrinks; NPS flat despite shipping velocity | Connect every initiative to an OKR; require outcome evidence at review |
| **Ivory tower PM** | PM defines strategy in isolation without customer contact or engineering partnership | Strategy sounds good but doesn't survive contact with reality; engineering builds the wrong thing | Weekly customer interviews; embed PM in delivery ceremonies; dual-track discovery |
| **HiPPO-driven roadmap** | Highest-Paid Person's Opinion overrides evidence | Frequent priority whiplash; roadmap credibility erodes; team morale drops | Require evidence for priority changes; use transparent prioritization framework |
| **Premature scaling** | Heavy PM process (OKRs, quarterly planning, portfolio management) before PMF | Process overhead without product traction; false precision in metrics; team spends time in meetings, not learning | Match PM rigor to product stage; at pre-PMF, optimize for learning speed |
| **Strategy amnesia** | Vision and strategy exist on paper but aren't referenced in daily decisions | Engineering makes trade-offs without strategic context; features ship that contradict positioning | Reference strategy in planning and refinement; make vision visible and alive |
| **Metrics theater** | Dashboards exist but nobody acts on them; OKRs are set and forgotten | "We track everything" but retention declines unnoticed; experiments run without clear success criteria | Tie metrics to decisions; review OKRs mid-cycle; kill metrics nobody acts on |
| **PM as blocker** | PM inserts approval gates that slow delivery without adding value | Engineers wait for PM sign-off on trivial decisions; PM becomes a bottleneck | Delegate decisions by impact/reversibility; define which decisions need PM and which don't |

---

## 8. Worked example

**Scenario:** A B2B SaaS startup has achieved early PMF with a project management tool for small agencies. The PM is planning the next growth phase.

### P1 — Discover

The PM runs **weekly customer interviews** and identifies a recurring theme: agencies want to share project status with their clients without giving full tool access. Competitive analysis shows two competitors offer "client portals" but with poor reviews for setup complexity.

**Outputs:** Problem statement ("agencies lose 3 hrs/week on manual status reports"), market analysis (3,200 agencies in SAM use the tool category), competitive landscape (2 competitors, both weak on this feature).

### P2 — Validate

The PM designs a **fake door test** — a "Client Portal" button in the nav that leads to a signup-for-beta form. 23% of active users click; 14% sign up. A **concierge MVP** with 5 agencies confirms the value: agencies save 2+ hrs/week; clients report higher satisfaction.

**Outputs:** Experiment log with evidence, feasibility assessment from Engineering (low complexity — read-only views of existing data).

### P3 — Plan & Commit

The PM creates a **product vision update** ("the agency tool that keeps clients in the loop without the overhead"), defines **OKRs** (O: "Agencies share project status effortlessly"; KR1: "40% of paid accounts activate client portal in 90 days"; KR2: "NPS increases by 10 points"), and drafts a **business case** (expected impact on retention: +5% logo retention; expected impact on expansion: upsell to higher tier).

**Roadmap:** Client Portal as an **MVP Product Spark** — 3 Forge iterations (6 weeks).

### SDLC A–F

The PM feeds the **prioritized backlog** to the team (Phase A). During **specification** (Phase B), the PM resolves a scope question: "Do we support custom branding per client?" — answer: "Not in MVP; park as future Ore." During **build** (Phase D), the PM answers a "why" question: "Why read-only? Clients might want to leave comments" — answer: "Comments add complexity; validate demand after launch." At **release** (Phase F), the PM authorizes the launch and coordinates with Marketing for the announcement.

### P4 — Launch

Coordinated launch: in-app announcement, email campaign to paid accounts, blog post, sales one-pager.

### P5 — Grow

**90-day review:** 38% activation (close to KR1 target), NPS +8 (below KR2). PM identifies that agencies with 5+ active projects activate at 52% but agencies with 1–2 projects don't see the value. Decision: **focus P5 on multi-project agencies** (segment the activation target); add lightweight "portfolio view" to the portal based on interview feedback.

**Roadmap update:** Portfolio view as a new Product Spark; "client comments" remains parked Ore pending further evidence.

---

## 9. Related reading

| Doc | Why |
|-----|-----|
| [`PRODUCT-MANAGEMENT.md`](PRODUCT-MANAGEMENT.md) | Full body of knowledge |
| [`PDLC.md`](../../../pdlc/PDLC.md) | Product phases P1–P6, stage gates |
| [`SDLC.md`](../../../sdlc/SDLC.md) | Delivery phases A–F, DoD |
| [`PDLC-SDLC-BRIDGE.md`](../../../pdlc/PDLC-SDLC-BRIDGE.md) | Cross-lifecycle bridge |
| [`BA-SDLC-PDLC-BRIDGE.md`](../ba/BA-SDLC-PDLC-BRIDGE.md) | Sibling discipline bridge — requirements and solution validation |
| [`PM-SDLC-PDLC-BRIDGE.md`](../../governance/pm/PM-SDLC-PDLC-BRIDGE.md) | Governance counterpart — delivery constraints |
| [`MKT-SDLC-PDLC-BRIDGE.md`](../marketing/MKT-SDLC-PDLC-BRIDGE.md) | Marketing — GTM and growth |
| [`CS-SDLC-PDLC-BRIDGE.md`](../customer-success/CS-SDLC-PDLC-BRIDGE.md) | Customer Success — retention and health signals |
| [`roles-archetypes.md`](../../../sdlc/methodologies/roles-archetypes.md) | Delivery role archetypes |

---

*Keep project-specific product management artifacts in `docs/product/`, not in this file.*
