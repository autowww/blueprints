---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Customer Success ↔ SDLC ↔ PDLC bridge

## Purpose

This document maps **Customer Success (CS)** to the two lifecycle frameworks:

- **PDLC** — "Are we building the **right product** (and sustaining the right outcomes in market)?"
- **SDLC** — "Are we building the product **right** (including the systems that scale customer experience)?"
- **Customer Success** — "Are **customers achieving their goals** with the product, and are we **reducing preventable churn**?"

CS is **PDLC-heavy** in **P4–P6**: onboarding and launch readiness (**P4**), retention, growth, and ongoing value realization (**P5**), migration, sunset, and offboarding (**P6**). It also reaches back into **P1–P3** when VoC and outcome evidence reshape discovery and strategy.

The **SDLC** connection is essential: CS at scale depends on **support tooling**, **in-app guidance**, **integrations** (CRM, billing, data warehouse), and **analytics instrumentation** that engineering delivers and operates.

**Canonical sources:** [`CUSTOMER-SUCCESS.md`](CUSTOMER-SUCCESS.md) (this package) · [`PDLC.md`](../../../pdlc/PDLC.md) · [`SDLC.md`](../../../sdlc/SDLC.md) · [`PDLC-SDLC-BRIDGE.md`](../../../pdlc/PDLC-SDLC-BRIDGE.md).

---

## Document map

| Section | Contents |
|---------|----------|
| [Purpose](#purpose) | Why this bridge exists; CS vs PDLC vs SDLC |
| [Comparison table](#comparison-table) | Scope, ownership, metrics, failure modes |
| [When one is missing](#when-one-is-missing) | Isolated lifecycles — what breaks |
| [CS across the lifecycle](#cs-across-the-lifecycle) | P1–P6 and SDLC A–F activities and outputs |
| [Role mapping](#role-mapping) | CS vs PM, Owner, Implementer, Support, Data |
| [Artifact flow](#artifact-flow) | Handoffs between CS, product, and engineering |
| [Calibration](#calibration) | By business model — B2B SaaS, B2C, internal tools |
| [Anti-patterns](#anti-patterns) | Common failures |
| [Worked example](#worked-example) | Reducing churn for a B2B SaaS product |
| [Related reading](#related-reading) | Authoritative docs in this repo |

---

## Comparison table

| Dimension | Customer Success | SDLC | PDLC |
|-----------|------------------|------|------|
| **Core question** | Are customers achieving outcomes; is churn preventable and understood? | How do we deliver working software with quality and predictability? | Should we build/continue this; does it create sustainable value? |
| **Scope** | Onboarding, health, support ops, self-service, feedback, retention, expansion, success planning | Discover → specify → design → build → verify → release (**A**–**F**) | Problem → validation → strategy → launch → grow → sunset (**P1**–**P6**) |
| **Primary owner** | CS leadership / CSMs / digital CS / support leadership (model-dependent) | Delivery team; **Owner** and **Implementer** per [`SDLC.md`](../../../sdlc/SDLC.md) | Product leadership / product trio; GTM alignment |
| **Timeline** | Continuous — account and cohort lifecycles | Sprint, iteration, or release cadence | Product and portfolio lifetime |
| **Success metric** | Activation, retention, NRR/GRR, CSAT/CES, support cost-to-serve, expansion pipeline quality | Velocity, quality, DORA, gate pass rates | Adoption, revenue, strategic outcomes, market fit |
| **Key artifacts** | Success plans, health models, playbooks, QBR decks, VoC themes, SLA definitions | Specs, code, tests, runbooks | Research, roadmap, experiments, launch metrics |
| **Risk focus** | Adoption failure, silent churn, broken promises, support economics, renewal compression | Technical and operational risk | Market and strategy risk |
| **Failure mode** | High touch without impact; churn surprises; tool-driven theater without outcomes | Features ship but customers still fail in production | Winning deals customers cannot succeed with |

---

## When one is missing

| Scenario | What happens |
|----------|--------------|
| **CS without PDLC grounding** | Excellent service on a product that should not exist or needs strategic pivot — high effort, flat retention. |
| **CS without SDLC capability** | Manual, heroic CS; health scores wrong or stale; no in-product guidance; integrations fragile — **does not scale**. |
| **PDLC without CS feedback** | Roadmap optimizes for acquisition or feature count; recurring post-sale failure modes hide in support noise until renewal cliff. |
| **SDLC without CS requirements** | Engineering ships "working" software without observability for onboarding funnels, admin workflows, or support-deflection surfaces. |
| **All three practiced** | Strategy (PDLC) selects and sequences bets; delivery (SDLC) implements reliable customer systems; CS **closes the loop** with measurable outcomes and retention economics. |

---

## CS across the lifecycle

| Phase | CS role | Key activities | Outputs |
|-------|---------|----------------|---------|
| **P1 Discover** | **VoC partner** | Mine support themes, churn interviews, community signals; frame outcome hypotheses | Problem themes, jobs-to-be-done evidence, segment pain inventory |
| **P2 Validate** | **Pilot success designer** | Define pilot success criteria with design partners; measure TTV in controlled cohorts | Pilot scorecards, onboarding requirements for MVP |
| **P3 Plan & Commit** | **Coverage & economics partner** | Model CS coverage (high/low touch), support SLAs by tier, success KPIs in business case | Operating model proposal, entitlements vs. promises alignment |
| **A Discover** | **Requirements stakeholder** | Specify needs for health telemetry, admin tools, in-app help, integrations | CS epics / FRs for instrumentation and tooling |
| **B Specify** | **Workflow co-owner** | Ticket taxonomy, escalation rules, CRM/CS platform fields, success-plan templates | Specs for support and CS workflows; data contracts |
| **C Design** | **UX partner for help surfaces** | Help center IA, in-app guidance flows, error messages that reduce tickets | Designs for self-service and recovery paths |
| **D Build** | **Integration tester** | UAT on CS tools, billing hooks, dunning, data pipelines to warehouse | UAT results, go-live readiness checklist |
| **E Verify** | **Operational QA** | Verify deflection metrics pipelines, alert routing, SLA timers in staging | Verification notes, monitoring dashboards |
| **F Release** | **Launch readiness** | Enablement for support/CS; known issues comms; first-touch playbooks | Release comms pack, support briefing |
| **P4 Launch** | **Onboarding owner** | Run onboarding programs; track activation; tighten feedback loop with product | Activation dashboards, onboarding retro, backlog of friction |
| **P5 Grow** | **Retention & expansion owner** | Health scoring, QBRs, playbooks, VoC routing, community programs | Renewals forecast quality, expansion pipeline, themed insights |
| **P6 Sunset** | **Transition owner** | Migration comms, export assistance, offboarding experience, knowledge capture | Migration runbooks, sunset FAQs, churn reason coding |

---

## Role mapping

| Phase(s) | CS stance | PDLC accountability | SDLC accountability | Typical archetypes |
|----------|-----------|---------------------|-------------------|-------------------|
| **P1–P2** | Insight provider from market friction | PM, UX research | — (upstream) | Demand & value |
| **P3** | Operating model and promise alignment | PM, GTM, finance | Owner (feasibility) | Steer & govern; Demand & value |
| **A–F** | Internal customer for platforms | PM prioritization | Owner / Implementer | Build & integrate; Assure & ship |
| **P4** | Onboarding and launch success | PM, GTM | Iterative A–F fixes | Demand & value |
| **P5** | Account outcomes and retention | PM, sales (expansion) | Continuous improvement cycles | Flow & improvement |
| **P6** | Orderly exit and learning | PM, legal, finance | Migration delivery | Steer & govern |

### CS vs adjacent roles (summary)

| Role | Emphasis |
|------|----------|
| **Product Manager** | What to build and why; portfolio outcomes — **not** day-to-day account coverage |
| **CSM / digital CS** | Account-level orchestration, success planning, adoption plays — **customer outcome accountability** |
| **Support** | Break/fix and how-to at scale — **case-level SLAs**; feeds taxonomy and KB |
| **Professional Services / Onboarding specialists** | Time-bound implementation — **project delivery** vs. ongoing success (often handoff to CS) |
| **Data science / analytics** | Models and metrics — **does not own** account relationship |

---

## Artifact flow

### PDLC / strategy → CS (inputs)

| Source | CS usage |
|--------|----------|
| Positioning and ICP (**P3**, GTM) | Sets expectations CS must **fulfill or correct** in onboarding |
| Pricing/packaging | Drives **entitlement** truth in success plans and support policy |
| Roadmap themes | Align QBR narratives and **commitment boundaries** |

### SDLC → CS (outputs)

| Engineering / delivery output | CS usage |
|------------------------------|----------|
| Product analytics events | Funnels, health scores, adoption milestones |
| Admin and billing UX | Fewer "how do I…?" tickets; cleaner dunning |
| In-app guidance | Faster TTV; measurable step completion |
| Support integrations | Single customer record, SLA reporting |

### CS → SDLC / PDLC (feedback)

| CS signal | Consumption |
|-----------|-------------|
| Top ticket drivers | Backlog prioritization (**P5**, **A–B**) |
| Churn and save reasons | Strategy and packaging (**P3**, **P5**) |
| QBR asks | Roadmap input; **NFRs** for scale/permissions |
| Health model false positives/negatives | Data science iteration; feature engineering |

---

## Calibration

### B2B SaaS

| Aspect | Typical calibration |
|--------|---------------------|
| **Coverage** | Named CSMs for mid-market/enterprise; pooled digital for long tail |
| **Motion** | Land-and-expand; **QBRs** for strategic accounts; success plans standard |
| **Metrics** | NRR, GRR, logo churn, expansion pipeline, **health → renewal** correlation |
| **Systems** | CRM + CS platform + product analytics + support suite; **strong integrations** |

### B2C / prosumer

| Aspect | Typical calibration |
|--------|---------------------|
| **Coverage** | Mostly digital; human assist for edge cases and trust/safety |
| **Motion** | Funnel optimization; **lifecycle email/push**; community |
| **Metrics** | Activation, cohort retention, payment recovery, **CES** on key flows |
| **Systems** | Self-service first; AI support with strict guardrails |

### Internal tools

| Aspect | Typical calibration |
|--------|---------------------|
| **Coverage** | Super-users, IT help desk, **product owner as pseudo-CSM** |
| **Motion** | Change management and training; **SLAs** tied to employee productivity |
| **Metrics** | Task time saved, error rate, support volume per user, **compliance adoption** |
| **Systems** | Integrate with corporate IdP, ticketing, and learning platforms |

---

## Anti-patterns

| Anti-pattern | Description | Fix |
|--------------|-------------|-----|
| **Vanity health scores** | Green/red dashboards with no predictive validation or owner | Back-test against churn/renewal; document lineage; tune by segment |
| **CS as unpaid sales** | CSMs carry quota without authority on product or commercial levers | Clarify expansion **RACI** with sales; protect success outcomes |
| **Throw-it-over-the-wall onboarding** | Sales promises custom workflows CS cannot implement | Stage-gated **handoff** with documented success criteria |
| **Support as infinite buffer** | Product quality issues absorbed forever in L1 | Root-cause **problem management**; product SLAs for defect burn-down |
| **VoC black hole** | Surveys collected; themes never reach roadmap | Named PM intake, SLA for response themes, public changelog linkage |
| **Manual orchestration at scale** | Spreadsheets and heroics instead of instrumentation | Prioritize SDLC backlog for events, in-app guidance, and integrations |

---

## Worked example

**Scenario:** A B2B SaaS analytics product sees **logo churn** rising in the **SMB segment**; NRR is stable only because enterprise expansion masks the problem.

| Step | Lifecycle | What happens |
|------|-----------|--------------|
| 1 | **P5** | CS leadership segments churned accounts: **48%** cite "never got reliable data into the product" vs. **18%** price — hypothesis: onboarding/integration failure, not value pricing. |
| 2 | **P1** | VoC program runs **structured exit and save interviews**; product analytics shows **70%** of churned SMB never completed the **primary integration milestone** within 14 days. |
| 3 | **A–B** | PM and CS jointly file requirements: **integration health checks**, **step-level onboarding events**, **error catalog** surfacing in UI, **CS-visible integration status** in admin. |
| 4 | **C–D** | Engineering ships guided connector setup, retries with backoff, and **actionable error messages**; adds **in-app checklist** with persistence. |
| 5 | **E–F** | CS runs UAT with pilot customers; support updates KB; **release notes** highlight setup improvements. |
| 6 | **P4** | Digital onboarding campaign: email + in-app nudges tied to **checklist state**; CSMs focus only on accounts breaching **risk thresholds**. |
| 7 | **P5** | Data science rebuilds SMB health model with **integration milestones** weighted heavily; **playbook** triggers CS outreach at day 7 if milestone incomplete. |
| 8 | **P5** | Twelve-week readout: **14-day activation** for SMB up from **41% → 67%**; SMB logo churn down **2.1 pts**; support tickets for "connection errors" down **35%**. |

---

## Related reading

| Doc | Why |
|-----|-----|
| [`CUSTOMER-SUCCESS.md`](CUSTOMER-SUCCESS.md) | Full discipline body of knowledge |
| [`practices/README.md`](practices/README.md) | Practice guide index |
| [`PDLC.md`](../../../pdlc/PDLC.md) | Product phases P1–P6 |
| [`SDLC.md`](../../../sdlc/SDLC.md) | Delivery phases A–F |
| [`PDLC-SDLC-BRIDGE.md`](../../../pdlc/PDLC-SDLC-BRIDGE.md) | Product ↔ delivery alignment |
| [`UX-SDLC-PDLC-BRIDGE.md`](../ux-design/UX-SDLC-PDLC-BRIDGE.md) | Onboarding and in-product guidance design alignment |
| [`BA-SDLC-PDLC-BRIDGE.md`](../ba/BA-SDLC-PDLC-BRIDGE.md) | Requirements and solution evaluation ↔ lifecycles |
| [`BRIDGES.md`](../../../BRIDGES.md) | Index of bridge documents |
| [`roles-archetypes.md`](../../../sdlc/methodologies/roles-archetypes.md) | SDLC role archetypes |

---

*Keep project-specific customer success documentation in `docs/product/customer-success/` and support playbooks in `docs/operations/`, not in this file.*
