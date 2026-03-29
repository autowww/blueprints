# PM ↔ SDLC ↔ PDLC bridge

## Purpose

This document closes the **understanding gap** between three complementary disciplines:

- **PDLC** (Product Development Life Cycle) — "Are we building the **right product**?"
- **PM** (Project Management) — "Are we delivering **on time, on budget, within scope**?"
- **SDLC** (Software Development Life Cycle) — "Are we building the product **right**?"

All three are necessary in non-trivial software delivery. None is sufficient alone. This bridge explains how they relate, where they overlap, where they are distinct, and what happens when any layer is missing.

**Canonical sources:** [`PM.md`](PM.md) (this package) · [`PDLC.md`](../../../pdlc/PDLC.md) (sibling package) · [`SDLC.md`](../../../sdlc/SDLC.md) (sibling package) · [`PDLC-SDLC-BRIDGE.md`](../../../pdlc/PDLC-SDLC-BRIDGE.md) (two-domain bridge).

---

## Document map

| Section | Contents |
|---------|----------|
| [1. Three questions, three domains](#1-three-questions-three-domains) | Side-by-side comparison: scope, ownership, metrics, risk, failure modes |
| [2. Nesting model](#2-nesting-model) | How the three domains layer — and when layers collapse |
| [3. Phase alignment](#3-phase-alignment) | How PM process groups map to PDLC phases and SDLC phases |
| [4. Role mapping](#4-role-mapping) | Who owns what across all three domains |
| [5. When PM is explicit vs implicit](#5-when-pm-is-explicit-vs-implicit) | The governance spectrum by team size and organizational context |
| [6. Methodology compatibility](#6-methodology-compatibility) | How PM approaches combine with SDLC methodologies and PDLC approaches |
| [7. Anti-patterns](#7-anti-patterns) | Common failures when domains are missing or misaligned |
| [8. Worked example](#8-worked-example) | End-to-end scenario through all three domains |

---

## 1. Three questions, three domains

```blueprint-diagram
key: swimlane
alt: Diagram
```

### Comparison table

| Dimension | PDLC | PM | SDLC |
|-----------|------|----|------|
| **Core question** | Should we build this at all? | Can we deliver it within constraints? | How do we build this correctly? |
| **Scope** | Problem → strategy → launch → grow → sunset | Charter → plan → execute → monitor → close | Requirements → design → code → test → deploy |
| **Primary owner** | Product Manager / product trio | Project Manager / PMO | Engineering / delivery team |
| **Timeline** | Product lifetime (months to years) | Project duration (weeks to months) | Sprint / iteration / release cycle |
| **Success metric** | Adoption, retention, NPS, revenue, LTV | On time, on budget, within scope, stakeholder satisfaction | Velocity, defect rate, DORA, CI pass rate |
| **Risk focus** | Market risk (desirability, viability) | Execution risk (schedule, budget, resources, dependencies) | Technical risk (bugs, performance, security) |
| **Input** | Market signal, user pain, business opportunity | Funded initiative, defined scope, allocated resources | Validated requirements / backlog items |
| **Output** | Validated product delivering measurable outcomes | Completed project deliverables within constraints | Shippable software increment |
| **Failure mode** | Ship the wrong thing | Ship late, over budget, or with unmanaged risk | Ship buggy or fragile |
| **Governance** | Stage gates (go/kill/pivot), outcome reviews | Change control, earned value, milestone gates | DoD, CI gates, code review, phase exits |
| **Artifacts** | Research, experiments, vision, metrics dashboards | Charter, WBS, schedule, budget, risk register, status reports | Specs, code, tests, release notes |
| **End state** | Product retired or repositioned | Project closed, resources released | Deployed to production |

### When one is missing

| Scenario | What happens |
|----------|-------------|
| **PDLC + PM, no SDLC** | Great strategy and governance, but software is built poorly — buggy releases, no CI, fragile architecture. Managed chaos. |
| **PDLC + SDLC, no PM** | Product validated, engineering excellent, but nobody tracks budget, timeline, or cross-team dependencies. Works for small teams; fails at scale. |
| **PM + SDLC, no PDLC** | Delivered on time and built well, but nobody validated whether users need it. Successful project, failed product. The **build trap** with a Gantt chart. |
| **PM only** | Governance without substance. Schedule and budget tracked for work that is neither validated (no PDLC) nor well-built (no SDLC). |
| **SDLC only** | Engineering in a vacuum. Good code, no business context, no delivery governance. Common in early-stage startups; breaks when stakes rise. |
| **PDLC only** | Endless discovery and strategy without execution. Analysis paralysis with beautiful personas. |
| **All three practiced** | Validated problems become well-governed, well-built products that deliver measurable outcomes within predictable constraints. |

---

## 2. Nesting model

The default relationship is **nesting**: PDLC wraps PM wraps SDLC.

```
┌─────────────────────────────────────────────────────────┐
│  PDLC: Product Development Life Cycle                   │
│  P1 Discover → P2 Validate → P3 Plan & Commit             │
│  ┌───────────────────────────────────────────────────┐  │
│  │  PM: Project Management                           │  │
│  │  Initiate → Plan → Execute → Monitor → Close      │  │
│  │  ┌─────────────────────────────────────────────┐  │  │
│  │  │  SDLC: Software Development Life Cycle      │  │  │
│  │  │  A Discover → B Specify → C Design →        │  │  │
│  │  │  D Build → E Verify → F Release             │  │  │
│  │  └─────────────────────────────────────────────┘  │  │
│  └───────────────────────────────────────────────────┘  │
│  P4 Launch → P5 Grow → P6 Mature/Sunset                 │
└─────────────────────────────────────────────────────────┘
```

### When layers collapse

The three-layer model is the **general case**. In practice, layers often collapse:

| Context | What collapses | Why it works |
|---------|---------------|-------------|
| **Solo developer / small startup** | PM absorbed into the team; PDLC and SDLC may also merge | Low overhead; one person holds all context. Breaks at ~5 people. |
| **Single Scrum team** | PM absorbed into PO (scope) + SM (process) | Scrum ceremonies cover planning, monitoring, and retrospective. No separate PM reporting needed. |
| **Internal tool / infrastructure** | PDLC collapses (users are known, problem is operational) | PM + SDLC sufficient when "product discovery" is replaced by requirements from internal stakeholders. |
| **Fixed-price contract** | PM dominates; PDLC minimal (scope is contractual) | Discovery happened pre-contract. PM governance ensures contractual delivery. SDLC executes. |
| **Enterprise portfolio** | All three layers are explicit and may have dedicated teams | Scale, regulatory, and multi-stakeholder complexity demand separation of concerns. |
| **Maintenance / bug fix** | All three collapse to "just fix it" | No discovery, no project charter — just SDLC D–F with lightweight tracking. |

---

## 3. Phase alignment

### The full three-domain lifecycle

```blueprint-diagram
key: swimlane
alt: Diagram
```

### Phase-by-phase alignment

| PDLC | PM | SDLC | Relationship |
|------|----|----- |--------------|
| **P1 Discover Problem** | — | — | Upstream of both PM and SDLC. No project exists yet. |
| **P2 Validate Solution** | — | — | Still upstream. Feasibility spikes may involve engineering, but no formal project. |
| **P3 Plan & Commit** | **Initiate** | — | PDLC gates the decision to invest. PM Initiation creates the project charter from P3 outputs. |
| — | **Plan** | **A Discover** | PM creates the WBS, schedule, budget. SDLC Phase A decomposes scope into backlog items. These overlap: scope definition serves both. |
| — | **Execute + Monitor** | **A–F** | PM governs while SDLC delivers. PM tracks schedule/budget/risk; SDLC tracks velocity/quality/CI. |
| — | **Close** | **F Release** | SDLC releases the increment. PM obtains formal acceptance and closes the project. |
| **P4 Launch** | **Close** (partial overlap) | **F Release** (partial overlap) | Project closes. Product launches. The PM is done; the Product Manager continues. |
| **P5 Grow** | — | — | Post-project. Product team measures outcomes and iterates. May spawn **new** projects (each with its own PM lifecycle). |
| **P6 Mature / Sunset** | — (or new project) | — (or new project) | Sunset may require a dedicated project (migration tooling, customer comms). |

---

## 4. Role mapping

### Across all three domains

| Phase(s) | PDLC role | PM role | SDLC role |
|----------|-----------|---------|-----------|
| **P1–P2** (Discovery) | Product Manager, UX Researcher, Designer, Tech Lead | — | — |
| **P3** (Plan & Commit) → **PM Initiate** | Product Manager (requests investment) | Sponsor (authorizes), PM (assigned) | — |
| **PM Plan** → **SDLC A–B** | Product Manager (acceptance criteria) | PM (WBS, schedule, budget) | Owner (backlog), Implementer (estimates) |
| **PM Execute** → **SDLC C–F** | Product trio (engaged via ceremonies) | PM (tracks, reports, manages risk) | Owner + Implementer (build, verify, release) |
| **PM Close** → **P4 Launch** | Product Manager (GTM) | PM (formal acceptance, lessons learned) | — (deployment done) |
| **P5 Grow** | Product Manager, Data/Analytics | — (project closed) | Owner (for iteration backlog) |
| **P6 Sunset** | Product Manager, Exec sponsor | PM (if sunset is a project) | — (or minimal SDLC for migration) |

### Role confusion to avoid

| Confusion | Clarification |
|-----------|---------------|
| Project Manager vs Product Manager | **Project** Manager delivers within constraints (time, cost, scope). **Product** Manager maximizes product value and outcomes. Different goals, different timelines, different success metrics. |
| Sponsor vs Product Owner | **Sponsor** provides authority and funding (PM domain). **Product Owner** maximizes value from the backlog (SDLC domain). In some orgs, the same person holds both — but the concerns remain distinct. |
| PMO vs Scrum Master | **PMO** governs portfolio-level standards and reporting (PM domain). **Scrum Master** serves a single team's process effectiveness (SDLC domain). PMO is organizational; SM is team-level. |
| Steering Committee vs Product Trio | **Steering Committee** governs project execution (PM domain). **Product Trio** co-owns discovery (PDLC domain). Steering committees ask "is the project on track?"; product trios ask "are we solving the right problem?" |

---

## 5. When PM is explicit vs implicit

PM governance exists on a **spectrum**. The right level depends on context, not ideology.

| Signal | PM should be **implicit** (absorbed) | PM should be **explicit** (dedicated) |
|--------|--------------------------------------|---------------------------------------|
| **Team size** | 1–8 people, single team | Multiple teams, cross-functional dependencies |
| **Budget** | Internal, no formal budget tracking | Formal budget with approval thresholds |
| **Contract** | Internal product, no external commitments | Fixed-price, time-and-materials, or regulated |
| **Stakeholders** | Few, accessible, low-ceremony | Many, distributed, require formal reporting |
| **Duration** | Weeks to a few months | Months to years |
| **Risk** | Low (known technology, proven approach) | High (new technology, regulatory, dependencies) |
| **Compliance** | None or lightweight | SOX, HIPAA, government procurement, ISO |
| **Organizational culture** | Flat, autonomous teams | Hierarchical, PMO-driven |

### The Agile PM question

A common debate: "Do Agile teams need project managers?"

| Position | When it's right |
|----------|-----------------|
| **No PM needed** | Single Scrum team, internal product, PO and SM cover governance, team is empowered and co-located. |
| **PM as servant-leader** | Multi-team coordination, dependency management, stakeholder reporting — but PM does not direct daily work. Aligns with SAFe RTE or Agile PM. |
| **Traditional PM** | Fixed-price contract, regulatory environment, large program with formal gates and earned value reporting. |
| **Hybrid** | PM handles governance envelope (budget, timeline, risk, stakeholders); Agile team self-manages within that envelope. Most common in enterprise. |

---

## 6. Methodology compatibility

PM approaches, SDLC methodologies, and PDLC approaches are **independently selectable** and **composable**.

### Common combinations

| PM approach | SDLC methodology | PDLC approach | When to use |
|-------------|------------------|---------------|-------------|
| **PMI/PMBOK (predictive)** | Phased delivery / Waterfall | Stage-Gate | Regulated, contractual, low-uncertainty projects |
| **PMI/PMBOK (Agile)** | Scrum | Dual-Track Agile | Enterprise Agile with PMI governance standards |
| **PMI/PMBOK (hybrid)** | Scrum + Phased gates | Stage-Gate + Lean Startup | Enterprise with Agile execution and formal milestones |
| **PRINCE2** | Phased delivery | Stage-Gate | UK/EU government, AXELOS-aligned organizations |
| **PRINCE2 Agile** | Scrum / Kanban | Dual-Track Agile | Organizations that want PRINCE2 governance with Agile execution |
| **Lightweight (no formal PM)** | Scrum / Kanban / XP | Lean Startup + OSTs | Startups, small product teams, low-ceremony contexts |
| **SAFe (as PM + SDLC)** | SAFe (Scrum/Kanban at team level) | Lean Portfolio Management | Large enterprise, multi-team, portfolio level |
| **Six Sigma (DMAIC)** | Any (applied to process improvement) | Any | Improving an existing SDLC or PM process |

### How PM approaches relate to SDLC methodologies

| PM concern | Scrum addresses it via | Kanban addresses it via | Phased addresses it via |
|------------|----------------------|------------------------|------------------------|
| **Scope** | Product Backlog + Sprint Goal | Backlog + WIP limits | Requirements baseline + change control |
| **Schedule** | Sprint time-box (fixed cadence) | Flow metrics (cycle time, throughput) | Gantt chart + critical path |
| **Budget** | Not addressed (PM adds this) | Not addressed (PM adds this) | Phase-level budget allocation |
| **Risk** | Sprint Review (inspect) + Retro (adapt) | Explicit policies, service classes | Risk register + gate reviews |
| **Quality** | Definition of Done + Sprint Review | Explicit policies + WIP limits | Phase-exit quality gates |
| **Stakeholders** | Sprint Review (transparency) | Board visibility | Milestone reports + gate reviews |
| **Reporting** | Sprint velocity + burn-down | Cumulative flow + cycle time | Earned value + milestone tracking |

---

## 7. Anti-patterns

| Anti-pattern | Domain gap | Symptom | Fix |
|--------------|-----------|---------|-----|
| **Successful project, failed product** | PM without PDLC | Delivered on time and on budget. Nobody uses it. High fives at project closure, flat adoption at P5. | Add PDLC discovery (P1–P2) before project initiation. Validate the problem before governing its delivery. |
| **Beautiful strategy, broken delivery** | PDLC without PM or SDLC | Validated problem, compelling vision, funded initiative. Engineering is chaotic, timeline missed by 3x, budget overrun. | Add PM governance (schedule, budget, risk) and SDLC discipline (CI, testing, DoD). |
| **Governance theater** | PM without SDLC or PDLC | Elaborate project plans, weekly status reports, color-coded dashboards. The software is brittle and the product is unvalidated. | Ensure PM governance wraps around actual delivery discipline (SDLC) driven by validated intent (PDLC). |
| **PM as overhead** | PM misaligned with team | Project manager demands weekly status reports from a 3-person Agile team that already has Sprint Reviews. Ceremony duplication. Zero value added. | Right-size PM governance to team context (see §5). Absorb PM concerns into Agile ceremonies when the team is small enough. |
| **PM as Product Manager** | PM absorbing PDLC | Project manager decides what to build (scope = features they chose). No product discovery, no user research, no outcome measurement. | Separate PM (delivery governance) from PDLC (product strategy). PM governs **how** delivery happens; PDLC decides **what** to deliver. |
| **The eternal project** | PM without closing | Project has no defined end state. Scope keeps expanding. Budget keeps growing. "We're 80% done" for 18 months. | Define clear acceptance criteria at project initiation. Enforce change control. Close the project; start a new one for new scope. |
| **Shadow PM** | SDLC without acknowledged PM | Tech lead or senior developer informally tracks schedule, manages dependencies, reports to leadership — without the title, authority, or time allocation. Burnout risk. | Acknowledge the PM function. Either assign it formally or explicitly distribute it across PO + SM + team with clear ownership. |

---

## 8. Worked example

**Scenario:** A fintech company's product team has validated (PDLC P1–P2) that small-business customers need automated invoice reconciliation. PDLC P3 has defined success metrics (60% reconciliation automation rate, 40% reduction in time-to-close, $2M ARR within 12 months) and the executive team has approved funding for a 6-month initiative with a $500K budget and a team of 8 engineers.

### PDLC → PM handoff (P3 → Initiate)

The **Product Manager** delivers to the **Project Sponsor** (VP Engineering):
- Validated problem statement with evidence (12 interviews, competitive analysis)
- Solution concept (ML-based matching engine + rule editor)
- Success metrics and GTM plan
- Requested resources: 8 engineers, 6 months, $500K

The Sponsor assigns a **Project Manager** and authorizes the project.

### PM Initiation

The PM creates the **project charter**:
- Objectives: automated invoice reconciliation feature, 60% automation rate
- Scope: ML matching engine, rule editor UI, QuickBooks/Xero integrations
- Constraints: $500K budget, 6-month timeline, existing platform architecture
- Assumptions: ML training data available from existing customers (with consent)
- Stakeholders: VP Eng (sponsor), Product Manager, Head of Sales, Compliance Lead
- Risks: ML model accuracy may require multiple training iterations; integration APIs may change

### PM Planning + SDLC Phase A

**PM** creates the WBS:
- Work package 1: ML matching engine (M3E1)
- Work package 2: Rule editor UI (M3E2)
- Work package 3: QuickBooks integration (M3E3)
- Work package 4: Xero integration (M3E4)

**SDLC Phase A** decomposes into stories with the Product Owner:
- M3E1S1: Training data pipeline
- M3E1S2: Matching model v1
- M3E2S1: Rule editor UI scaffold
- (and so on)

**PM** develops: schedule (3 sprints for ML, 2 sprints for UI, 2 sprints for integrations, 1 sprint buffer), budget allocation ($300K engineering, $100K infrastructure, $100K contingency), risk register (ML accuracy risk: high impact, medium probability; API change risk: medium impact, low probability).

### PM Execute + Monitor → SDLC B–F

Sprint 1–3: ML matching engine development.
- **SDLC:** Phases B–D for M3E1 stories. CI green. Code reviewed.
- **PM:** Week 2 status: SPI = 1.0, CPI = 1.05 (slightly under budget). Risk: training data quality lower than expected — response: add data cleaning sprint.

Sprint 4–5: Rule editor UI + ML model iteration.
- **SDLC:** Phases B–D for M3E2 stories. Sprint Review with stakeholders.
- **PM:** Week 6 status: SPI = 0.9 (data cleaning sprint added), CPI = 0.95. Reforecast: timeline may extend 2 weeks. PM escalates to Sponsor — approved from buffer.

Sprint 6–7: Integrations.
- **SDLC:** M3E3, M3E4. Phase E: integration tests, UAT.
- **PM:** Week 10: SPI = 0.95 (recovering), CPI = 0.92. Budget on track with contingency.

Sprint 8: Hardening, Phase E–F.
- **SDLC:** Phase F release: feature-flagged to beta customers.
- **PM:** Milestone review: all deliverables complete. Quality metrics met. Budget: $480K of $500K.

### PM Close → PDLC P4–P5

**PM closes the project:**
- Formal acceptance from Sponsor
- Lessons learned: data quality assessment should happen during P2 feasibility, not during delivery
- Resources released: 6 of 8 engineers return to other projects; 2 remain for P5 iteration support
- Final budget: $480K (4% under budget)
- Final timeline: 6.5 months (2-week overrun, within buffer)

**PDLC P4 (Launch):**
- Beta results: 52% automation rate (target 60%). Good but below target.
- GA rollout after rule-tuning iteration.

**PDLC P5 (Grow):**
- Month 2 post-launch: automation rate reaches 63% after customer-specific rule optimization.
- New iteration backlog items flow into a **new project** — each with its own (lightweight) PM lifecycle.

### Summary: who governed what

| Domain | What they governed | Key artifacts |
|--------|-------------------|---------------|
| **PDLC** | Problem validity, solution viability, outcome measurement | Research synthesis, experiment log, success metrics, GTM plan |
| **PM** | Schedule, budget, risk, stakeholder reporting | Charter, WBS, schedule, risk register, status reports, lessons learned |
| **SDLC** | Technical delivery quality, CI/CD, testing | Stories, code, tests, CI pipeline, release notes |

---

## Related reading (this blueprint)

| Doc | Why |
|-----|-----|
| [`PM.md`](PM.md) | Process groups, knowledge areas, governance, metrics |
| [`SDLC.md`](../../../sdlc/SDLC.md) | Delivery phases A–F, DoD, CI/CD |
| [`PDLC.md`](../../../pdlc/PDLC.md) | Product phases P1–P6, artifacts, exit criteria |
| [`PDLC-SDLC-BRIDGE.md`](../../../pdlc/PDLC-SDLC-BRIDGE.md) | Two-domain bridge (product ↔ delivery) |
| [`approaches/README.md`](approaches/README.md) | PM approach guides (PMI/PMBOK, PRINCE2, Six Sigma) |
| [`roles-archetypes.md`](../../../sdlc/methodologies/roles-archetypes.md) | Five delivery archetypes and methodology mapping |
