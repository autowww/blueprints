# BA ↔ SDLC ↔ PDLC bridge

## Purpose

This document closes the **understanding gap** between business analysis (BA) and the two lifecycle frameworks it serves:

- **PDLC** (Product Development Life Cycle) — "Are we building the **right product**?"
- **SDLC** (Software Development Life Cycle) — "Are we building the product **right**?"
- **BA** — "Do we **understand the needs** and will the solution **satisfy** them?"

BA is the discipline that feeds both lifecycles with structured understanding of needs, constraints, and value — and evaluates whether the delivered solution meets those needs.

**Canonical sources:** [`BABOK.md`](https://forgesdlc.com/discipline-business-analysis.html) (this package) · [`PDLC.md`](../../../pdlc/PDLC.md) · [`SDLC.md`](../../../sdlc/SDLC.md) · [`PDLC-SDLC-BRIDGE.md`](../../../pdlc/PDLC-SDLC-BRIDGE.md).

---

## Document map

| Section | Contents |
|---------|----------|
| [1. The three-discipline model](#1-the-three-discipline-model) | How BA, PDLC, and SDLC relate — scope, ownership, overlap |
| [2. Knowledge area alignment](#2-knowledge-area-alignment) | Each BABOK knowledge area mapped to PDLC P1–P6 and SDLC A–F |
| [3. Role mapping](#3-role-mapping) | BA roles vs PM, Owner, Implementer, Architect |
| [4. Technique selection by phase](#4-technique-selection-by-phase) | Which BA techniques to use at each lifecycle stage |
| [5. Artifact flow](#5-artifact-flow) | What BA produces and where it goes |
| [6. Calibration — when to invest in BA](#6-calibration--when-to-invest-in-ba) | Lightweight vs heavyweight BA by context |
| [7. Anti-patterns](#7-anti-patterns) | Common failures when BA is missing or misapplied |
| [8. Worked example](#8-worked-example) | End-to-end scenario showing BA across PDLC and SDLC |

---

## 1. The three-discipline model

```blueprint-diagram
key: swimlane
alt: Diagram
```

| Dimension | BA | PDLC | SDLC |
|-----------|----|----- |------|
| **Core question** | What do stakeholders need? Does the solution satisfy those needs? | Should we build this? Is it the right product? | How do we build this correctly? |
| **Scope** | Needs analysis → requirements → solution evaluation | Problem validation → strategy → launch → growth → sunset | Requirements → design → build → test → deploy |
| **Primary owner** | Business analyst / product analyst | Product manager / product trio | Engineering / delivery team |
| **Timeline** | Initiative lifetime (may span multiple PDLC and SDLC cycles) | Product lifetime (months to years) | Sprint / iteration / release cycle |
| **Success metric** | Requirements quality, stakeholder satisfaction, solution value realization | Adoption, retention, NPS, revenue | Velocity, defect rate, DORA, CI pass rate |
| **Key artifacts** | Stakeholder register, requirements package, business case, traceability matrix | Research synthesis, experiments, vision, metrics dashboards | Specs, code, tests, release notes |
| **Risk focus** | Misunderstood needs, incomplete requirements, scope creep | Market risk (desirability, viability) | Technical risk (bugs, performance, security) |

### When one is missing

| Scenario | What Happens |
|----------|-------------|
| **BA without PDLC** | Requirements are well-structured but may solve the wrong problem — no market validation, no outcome measurement |
| **BA without SDLC** | Needs are understood and documented but delivery is unreliable — great specs, broken execution |
| **PDLC without BA** | Product direction is validated but requirements are vague — validated idea, ambiguous specifications |
| **SDLC without BA** | Team ships efficiently but requirements emerge ad-hoc — fast delivery, frequent rework |
| **All three practiced** | Validated problems become well-specified, well-built solutions that deliver measurable outcomes |

---

## 2. Knowledge area alignment

### BA Planning & Monitoring

| Activity | PDLC Phase | SDLC Phase | Description |
|----------|------------|------------|-------------|
| Plan BA approach | P1 start | A start | Decide formality level, techniques, stakeholder engagement strategy |
| Identify stakeholders | P1 | A | Map all affected parties, their influence, and their information needs |
| Plan BA governance | P3 | A–B | Define approval processes, change control, communication cadence |
| Monitor BA work | Across all | Across all | Track whether BA activities are delivering value; adjust approach |

### Strategy Analysis

| Activity | PDLC Phase | SDLC Phase | Description |
|----------|------------|------------|-------------|
| Analyze current state | P1 (Discover) | — | Document existing capabilities, processes, pain points, organizational context |
| Define future state | P1–P2 | — | Articulate desired outcomes, capability gaps, opportunity definition |
| Assess risks | P2–P3 | — | Identify risks to change success (organizational, technical, market) |
| Define change strategy | P3 (Strategize) | — | Recommend solution approach, scope boundaries, transition needs |
| Define solution scope | P3 | A (Discover) | Delineate what is in/out of scope for the delivery team |

### Elicitation & Collaboration

| Activity | PDLC Phase | SDLC Phase | Description |
|----------|------------|------------|-------------|
| Prepare for elicitation | P1 | A | Select techniques, identify participants, prepare materials |
| Conduct elicitation | P1–P2 | A–B | Interviews, workshops, observation, prototyping, document analysis |
| Confirm elicitation results | P2 | B | Validate understanding with stakeholders; resolve conflicts |
| Communicate BA information | Across all | Across all | Ensure stakeholders have the right information at the right time |
| Manage stakeholder collaboration | Across all | Across all | Maintain engagement, resolve disagreements, build shared understanding |

### Requirements Life Cycle Management

| Activity | PDLC Phase | SDLC Phase | Description |
|----------|------------|------------|-------------|
| Trace requirements | P3 | A–B | Link requirements to business objectives, design elements, tests |
| Maintain requirements | P3–P5 | A–F | Keep requirements current as understanding evolves |
| Prioritize requirements | P3 | A | Rank by business value, risk, dependencies, feasibility |
| Assess requirements changes | P5 (Grow) | A (iteration) | Evaluate impact of proposed changes on scope, schedule, quality |
| Approve requirements | P3 | B | Obtain stakeholder sign-off on baseline requirements |

### Requirements Analysis & Design Definition

| Activity | PDLC Phase | SDLC Phase | Description |
|----------|------------|------------|-------------|
| Specify and model requirements | P2 | B (Specify) | Use cases, user stories, data models, state diagrams, process models |
| Verify requirements | — | B | Check completeness, consistency, correctness, feasibility |
| Validate requirements | P2 | B–C | Confirm requirements deliver business value if implemented |
| Define requirements architecture | — | B–C | Organize requirements into a coherent structure; identify gaps |
| Define design options | P2 | C (Design) | Propose solution approaches; evaluate trade-offs |
| Analyze potential value | P2–P3 | — | Estimate expected benefits of proposed solutions |

### Solution Evaluation

| Activity | PDLC Phase | SDLC Phase | Description |
|----------|------------|------------|-------------|
| Measure solution performance | P5 (Grow) | E (Verify) | Assess actual vs expected value delivery |
| Analyze performance measures | P5 | — | Identify root causes of gaps between expected and actual value |
| Assess solution limitations | P5–P6 | — | Document constraints preventing full value realization |
| Assess enterprise limitations | P6 (Sunset) | — | Identify organizational barriers to solution value |
| Recommend actions | P5–P6 | — | Propose: do nothing, improve, replace, or retire |

---

## 3. Role mapping

### Across the lifecycle

| Phase(s) | BA Role | PDLC Role | SDLC Role | Archetype |
|----------|---------|-----------|-----------|-----------|
| **P1–P2** (Discovery) | Elicitation lead, stakeholder analyst | PM, UX Researcher | — (upstream) | Demand & value |
| **P3** (Strategize) | Requirements owner, scope definer | PM, GTM Lead | Owner (entering SDLC) | Demand & value + Steer & govern |
| **A–B** (Discover, Specify) | Requirements analyst, modeler | — | Owner (priorities), Implementer (specs) | Build & integrate |
| **C** (Design) | Design option evaluator | — | Implementer (architecture) | Build & integrate |
| **D–E** (Build, Verify) | Acceptance criteria verifier | — | Implementer, QA | Assure & ship |
| **P4** (Launch) | Transition requirements owner | GTM Lead | — (downstream) | Demand & value |
| **P5** (Grow) | Solution evaluator, change assessor | PM, Data/Analytics | Owner (iteration) | Demand & value |
| **P6** (Sunset) | Enterprise limitation assessor | PM, Exec sponsor | — | Steer & govern |

### BA vs Product Manager

| Dimension | Business Analyst | Product Manager |
|-----------|-----------------|-----------------|
| **Primary focus** | Solution requirements quality, stakeholder needs completeness | Market opportunity, user value, business viability |
| **Key question** | "Are requirements complete, consistent, and traceable?" | "Is this the right thing to build for the market?" |
| **Techniques** | Use cases, data modeling, process modeling, decision analysis | User interviews, A/B tests, OKRs, roadmap prioritization |
| **Output** | Requirements package, traceability matrix, business case | Product vision, success metrics, experiment log |
| **Overlap** | Stakeholder interviews, workshop facilitation, prioritization | Both elicit information and synthesize stakeholder input |

In small teams, one person often fills both roles. In larger organizations, they are distinct: the PM owns the **what and why** (market-facing); the BA owns the **detailed what** (specification-facing).

---

## 4. Technique selection by phase

This table maps commonly used BA techniques to lifecycle phases. The full catalog is in [`techniques/README.md`](techniques/README.md).

| Lifecycle Phase | Recommended BA Techniques |
|-----------------|---------------------------|
| **P1 Discover Problem** | Stakeholder analysis, interviews, observation, document analysis, SWOT analysis, benchmarking, focus groups |
| **P2 Validate Solution** | Prototyping, use case modeling, user stories, process modeling, acceptance criteria definition, MoSCoW prioritization |
| **P3 Strategize** | Business case development, decision analysis, scope modeling, risk analysis, estimation, stakeholder mapping |
| **A Discover** | Backlog refinement, user story mapping, story decomposition, acceptance criteria writing |
| **B Specify** | Use cases, data modeling, state diagrams, business rules analysis, interface analysis, non-functional requirements analysis |
| **C Design** | Design option evaluation, trade-off analysis, architectural constraint analysis, feasibility assessment |
| **D Build** | Acceptance criteria clarification (just-in-time), requirements change assessment |
| **E Verify** | Acceptance testing support, requirements validation, defect analysis |
| **F Release** | Transition requirements verification, readiness assessment |
| **P4 Launch** | Transition requirements sign-off, training needs analysis, support documentation review |
| **P5 Grow** | Solution performance measurement, root cause analysis, lessons learned, change impact analysis |
| **P6 Mature / Sunset** | Enterprise limitation assessment, replacement analysis, sunset criteria evaluation |

---

## 5. Artifact flow

### BA → PDLC

| BA Artifact | Destination (PDLC) | Usage |
|-------------|---------------------|-------|
| Current state assessment | P1: research synthesis | Evidence base for problem validation |
| Stakeholder analysis | P1–P3: stakeholder engagement | Identifies who to include in discovery and strategy |
| Business case | P3: stage-gate review | Quantified justification for investment decision |
| Solution scope | P3 → SDLC handoff | Defines boundaries of what enters delivery |

### BA → SDLC

| BA Artifact | Destination (SDLC) | Usage |
|-------------|---------------------|-------|
| Requirements package | Phase A–B: backlog items, story specs | Detailed functional and non-functional requirements |
| Traceability matrix | Phase B: `docs/requirements/traceability/` | Links requirements to tests, design elements, business objectives |
| Acceptance criteria | Phase B: story acceptance criteria | Verifiable conditions for story completion |
| Data models / process models | Phase C: design inputs | Inform architectural decisions |
| Non-functional requirements | Phase B–C: quality attribute specs | Performance, security, scalability constraints |

### PDLC / SDLC → BA (feedback)

| Source | BA Usage |
|--------|----------|
| PDLC P5 usage analytics | Input to solution evaluation — assess actual vs expected value |
| SDLC Phase E test results | Verification that requirements are correctly implemented |
| PDLC P5 user feedback | Input to requirements change assessment — new needs identified |
| SDLC Phase F release notes | Confirm which requirements were delivered; update traceability |

---

## 6. Calibration — when to invest in BA

Not every initiative needs the same level of BA rigor. Calibrate based on context:

### By initiative type

| Situation | BA Investment | Reasoning |
|-----------|---------------|-----------|
| **Greenfield product** (new market) | **Heavy** — full strategy analysis, formal elicitation, detailed requirements | High uncertainty; incomplete requirements cause expensive rework |
| **Feature on mature product** | **Medium** — focused elicitation, incremental requirements, lightweight traceability | Partial context exists from P5 data; BA fills gaps, not everything |
| **Technical infrastructure** | **Light** — internal stakeholder analysis, non-functional requirements focus | Users are engineers; needs are more knowable; technical specs dominate |
| **Bug fix / maintenance** | **Minimal** — defect analysis, root cause investigation | Problem is manifest; fix scope is small |
| **Enterprise transformation** | **Heavy** — full BABOK, enterprise architecture perspective, formal governance | Cross-organizational impact; many stakeholder groups; regulatory concerns |

### By team size

| Context | BA Approach |
|---------|------------|
| **Solo developer / tiny startup** | BA is implicit in the developer's head; formalize only what is needed to communicate with stakeholders |
| **Small agile team (3–8)** | BA embedded in product owner or team; use agile perspective — user stories, acceptance criteria, just-in-time elaboration |
| **Medium team (8–25)** | Dedicated BA role or shared BA/PM; formal requirements structure; traceability to WBS |
| **Large / multi-team** | BA team or chapter; formal requirements management; cross-team dependency analysis; SAFe perspective may apply |

---

## 7. Anti-patterns

| Anti-pattern | Description | Symptom | Fix |
|-------------|-------------|---------|-----|
| **Requirements vacuum** | No BA discipline; requirements emerge from ad-hoc conversations, Slack messages, verbal agreements | Frequent rework, scope creep, "that's not what I meant" | Introduce structured elicitation; document requirements in `docs/requirements/`; trace to business objectives |
| **Analysis paralysis** | Over-investment in BA upfront; trying to specify everything before any delivery begins | Months of requirements workshops before a line of code; specifications go stale | Time-box elicitation; use agile perspective — elaborate just ahead of delivery; validate through prototypes |
| **BA theater** | Requirements documents are produced but never read, never traced, never updated | Heavy SRS documents that gather dust; developers work from conversations anyway | Connect requirements to acceptance criteria; automate traceability; kill documents nobody reads |
| **Invisible BA** | BA work happens but is not documented — knowledge lives only in the analyst's head | Key-person dependency; onboarding takes months; handoffs lose information | Externalize BA artifacts into `docs/requirements/` and `docs/product/`; link from WBS |
| **BA as gatekeeper** | BA role blocks progress by requiring sign-off on everything; "you can't build until I approve" | Engineering bottlenecked on BA availability; BA becomes a process overhead rather than an enabler | Shift to collaborative model; BA embeds with delivery team; approval is asynchronous; acceptance criteria replace formal sign-off |
| **Copy-paste requirements** | Requirements from one project copied wholesale to another without validation of fit | Solution doesn't match new context; stakeholders not consulted; assumptions from old project propagate | Treat requirements as hypotheses; validate with current stakeholders; adapt scope to current context |

---

## 8. Worked example

**Scenario:** An enterprise SaaS company decides to add a multi-tenant audit logging feature after receiving recurring compliance requests from enterprise customers. The initiative flows through BA, PDLC, and SDLC.

### BA Planning & Monitoring

The BA lead assesses the initiative: enterprise compliance context, multiple stakeholder groups (security team, product team, enterprise customers, support), regulatory constraints (SOC 2, GDPR). Decision: **medium-heavy BA** — formal stakeholder analysis, structured elicitation, requirements traceability.

**Stakeholder register created:** Security Lead, VP Engineering, 3 enterprise customer representatives, Compliance Officer, Support Lead.

### Strategy Analysis (aligns with PDLC P1–P3)

**Current state:** Audit events are logged to application logs; no structured query interface; customers must request log exports via support tickets. Average turnaround: 3 business days.

**Future state:** Self-service audit log with real-time search, filtering by user/action/resource, configurable retention periods, export to SIEM tools.

**Change strategy:** Build audit log as a platform capability (not per-customer); expose via API and UI; retention policies configurable per tenant.

**Solution scope:** In scope — event capture, storage, search API, UI viewer, SIEM export. Out of scope — real-time alerting (deferred to next initiative), historical log backfill.

### Elicitation & Collaboration (aligns with PDLC P1–P2)

**Techniques used:** Stakeholder interviews (3 customers, Security Lead, Compliance Officer), document analysis (SOC 2 control objectives, GDPR Article 30), observation (current support ticket workflow), prototyping (Figma wireframes for audit log UI).

**Key findings confirmed:**
- Customers need query by: user, action type, resource, time range
- Minimum retention: 90 days (SOC 2); some customers need 1 year
- Export formats needed: CSV, JSON, SIEM webhook (Splunk, Datadog)
- Access control: tenant admins only; audit of the audit log itself required

### Requirements Analysis & Design Definition (aligns with SDLC B–C)

**Requirements package produced:**

| ID | Type | Requirement |
|----|------|-------------|
| AUD-FR-01 | Functional | System shall capture audit events for all user actions on tenant resources |
| AUD-FR-02 | Functional | Tenant admins shall search audit logs by user, action, resource, and time range |
| AUD-FR-03 | Functional | System shall support configurable retention periods per tenant (90 days–2 years) |
| AUD-FR-04 | Functional | System shall export audit logs in CSV, JSON, and SIEM webhook formats |
| AUD-NFR-01 | Non-functional | Audit log queries shall return results within 3 seconds for up to 10M events |
| AUD-NFR-02 | Non-functional | Audit event capture shall not increase API response latency by more than 5ms (P99) |
| AUD-TR-01 | Transition | Existing application logs from the last 90 days shall be migrated to the new audit system |

**Traceability:** Requirements traced to SOC 2 control CC7.2, GDPR Article 30(1), and business objective "reduce support ticket volume for audit requests by 80%."

**Design options evaluated:** (1) Append-only Postgres table with partitioning, (2) Elasticsearch cluster, (3) Managed cloud audit service (AWS CloudTrail-style). Recommendation: Option 1 for MVP (simpler, sufficient for 10M events), with migration path to Option 2 if volume exceeds 100M.

### Requirements Life Cycle Management (aligns with SDLC A–B)

Requirements baselined after stakeholder review. Change control: any addition requires impact assessment against 3-sprint delivery target. One change accepted during build: AUD-FR-05 — "Audit log shall record access to the audit log itself" (discovered during security review in SDLC Phase C).

### Solution Evaluation (aligns with PDLC P5)

**Post-launch measurement (8 weeks):**

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Support tickets for audit requests | -80% | -73% | Approaching target |
| Query response time (P95, 10M events) | <3s | 1.8s | Met |
| Tenant admin adoption (% using self-service) | 60% | 72% | Exceeded |
| API latency impact (P99) | <5ms | 3.2ms | Met |

**Assessment:** Solution delivers expected value. Gap in support ticket reduction traced to customers needing SIEM webhook documentation — documentation improvement recommended (not a requirements gap).

**Recommendation:** Continue current solution; defer Elasticsearch migration until event volume approaches 50M per tenant.

---

## Related reading

| Doc | Why |
|-----|-----|
| [`BABOK.md`](https://forgesdlc.com/discipline-business-analysis.html) | Knowledge areas, competencies, perspectives overview |
| [`PDLC-SDLC-BRIDGE.md`](../../../pdlc/PDLC-SDLC-BRIDGE.md) | How PDLC and SDLC relate without the BA lens |
| [`SDLC.md`](../../../sdlc/SDLC.md) | Delivery phases A–F, DoD |
| [`PDLC.md`](../../../pdlc/PDLC.md) | Product phases P1–P6, stage gates |
| [`techniques/README.md`](techniques/README.md) | Full BA technique catalog |
| [`perspectives/README.md`](perspectives/README.md) | Context-specific BA guidance |
| [`roles-archetypes.md`](../../../sdlc/methodologies/roles-archetypes.md) | Delivery role archetypes |
