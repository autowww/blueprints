# Project management (PM)

This describes **generic** project management — the discipline of initiating, planning, executing, monitoring, and closing work to achieve specific objectives within constraints of scope, time, cost, quality, resources, and risk.

**How PM relates to SDLC and PDLC:** SDLC answers "are we building the product right?" — phases, DoD, CI/CD, ceremonies. PDLC answers "are we building the right product?" — problem validation, strategy, outcome measurement. PM answers **"are we delivering on time, on budget, within scope, with acceptable risk?"** — governance, planning, resource management, and control. PM sits **between** PDLC and SDLC as the governance layer. See [`PM-SDLC-PDLC-BRIDGE.md`](PM-SDLC-PDLC-BRIDGE.md) for the full mapping.

**Approaches depth (PMI/PMBOK, PRINCE2, Six Sigma, …):** see [`approaches/README.md`](approaches/README.md) — full guides with external links and adoption notes.

---

## 1. Roles

Project management involves different accountabilities than product strategy (PDLC) or software delivery (SDLC). These roles **can overlap** with PDLC and SDLC roles — a Product Owner may also serve as project sponsor, a Tech Lead may also manage the project — but the **concerns** are distinct.

| Role | Responsibility |
|------|----------------|
| **Project Manager** | Plans, executes, monitors, and closes the project. Manages scope, schedule, budget, risk, quality, and stakeholder expectations. Accountable for **delivery** within constraints. |
| **Project Sponsor** | Provides **authority** and **funding**. Makes go/no-go decisions at major gates. Removes organizational blockers that exceed the PM's authority. |
| **PMO (Project Management Office)** | Sets PM **standards**, provides governance, portfolio visibility, resource allocation, and methodology guidance across projects. Not always present — common in enterprise, rare in startups. |
| **Steering Committee** | Senior stakeholders who provide **strategic direction**, resolve escalations, and approve major scope or budget changes. |
| **Team Members** | Execute project work. In software projects, these are the SDLC roles (Owner, Implementer) and PDLC roles (Product Trio) operating under PM governance. |

**Agile context:** In Scrum, the Project Manager role is **not prescribed**. PM responsibilities are distributed: the Product Owner handles scope and value, the Scrum Master handles process and impediments, and the Development Team self-manages execution. In enterprise Agile (SAFe), a Release Train Engineer (RTE) absorbs many PM functions. The PM role becomes explicit again when projects span multiple teams, have fixed-price contracts, or require formal reporting to external stakeholders.

**PDLC handoff:** The Project Sponsor often maps to the executive who approves PDLC Gate G3 (invest in building). The Project Manager takes over governance of the funded initiative as it enters SDLC delivery.

---

## 2. Process groups

Project management work falls into five **process groups** — not sequential phases, but overlapping sets of activities that recur throughout the project.

```blueprint-diagram
key: linear
alt: Diagram
```

### Initiating

**Goal:** Establish the project's existence, define high-level scope, secure authorization and funding.

| Activity | Output |
|----------|--------|
| Develop project charter | Charter: objectives, high-level scope, constraints, assumptions, sponsor, PM assignment |
| Identify stakeholders | Stakeholder register: interests, influence, engagement strategy |
| Define success criteria | Measurable criteria that determine project completion |

**PDLC connection:** Initiating receives the funded initiative from PDLC Phase P3 (Strategize). The project charter references the validated problem, solution concept, and success metrics from P1–P3.

### Planning

**Goal:** Define the detailed roadmap: scope, schedule, budget, quality plan, resource plan, risk plan, communications plan.

| Activity | Output |
|----------|--------|
| Define scope (WBS) | Work breakdown structure — deliverables decomposed into manageable work packages |
| Develop schedule | Timeline with milestones, dependencies, critical path |
| Estimate costs / budget | Cost baseline with contingency reserves |
| Plan quality | Quality standards, metrics, review processes |
| Plan resources | Team composition, availability, skill requirements |
| Plan risk management | Risk register, risk response strategies, contingency plans |
| Plan communications | Who gets what information, when, and how |
| Plan procurement | Make-or-buy decisions, vendor selection criteria (when applicable) |

**SDLC connection:** The WBS and schedule integrate with SDLC phases A–F. In Agile, "planning" is continuous (Sprint Planning, backlog refinement) rather than upfront. The PM plan sets the envelope (budget, timeline, milestones) within which Agile iterations operate.

### Executing

**Goal:** Perform the work defined in the plan. Coordinate people and resources, manage stakeholder engagement, ensure quality.

| Activity | Output |
|----------|--------|
| Direct and manage project work | Deliverables, work performance data |
| Manage quality | Quality audits, test results |
| Acquire and develop the team | Staffed team, training, team-building |
| Manage communications | Status reports, stakeholder updates |
| Manage stakeholder engagement | Issue resolution, expectation management |
| Conduct procurements | Vendor contracts, SLAs (when applicable) |

**SDLC connection:** Executing **is** SDLC Phases A–F in software projects. The PM layer adds budget tracking, stakeholder reporting, and cross-team coordination that SDLC methodology alone does not prescribe.

### Monitoring & controlling

**Goal:** Track progress against the plan. Identify variances and take corrective action. Manage changes.

| Activity | Output |
|----------|--------|
| Monitor scope, schedule, cost | Variance analysis (SPI, CPI), forecasts |
| Monitor risks | Risk reassessment, trigger evaluation |
| Control quality | Defect tracking, quality metrics |
| Control changes | Change requests evaluated, approved/rejected, implemented |
| Report performance | Dashboards, earned value reports, milestone tracking |

**SDLC connection:** Monitoring consumes SDLC delivery metrics (velocity, cycle time, DORA) as inputs. It adds project-level metrics (earned value, budget burn, milestone adherence) that SDLC does not track.

### Closing

**Goal:** Formally complete the project. Archive artifacts, release resources, capture lessons learned.

| Activity | Output |
|----------|--------|
| Obtain formal acceptance | Sign-off from sponsor/stakeholders |
| Archive project artifacts | Searchable project repository |
| Release resources | Team members returned to resource pool |
| Conduct lessons learned | Retrospective document: what worked, what didn't, recommendations |
| Close procurements | Vendor contracts closed, final payments |

**PDLC connection:** Project closing often overlaps with PDLC Phase P4 (Launch). The project is "done" when the deliverable is handed over; the **product** continues through P5 (Grow) and P6 (Mature/Sunset) — managed by product roles, not the project manager.

---

## 3. Governance model

PM governance defines **decision rights**, **escalation paths**, and **reporting cadences**. The level of governance should match the project's size, risk, and organizational context.

### Governance spectrum

| Context | PM governance level | What it looks like |
|---------|--------------------|--------------------|
| **Solo developer / small team** | Minimal | No formal PM role. Backlog is the plan. Burn rate is the budget. Slack is the status report. |
| **Single Agile team** | Light | PM concerns absorbed into PO (scope/value) and SM (process/impediments). Sprint metrics serve as project tracking. |
| **Multi-team program** | Moderate | Dedicated PM or RTE. Cross-team dependency management. Program-level milestones and budget tracking. |
| **Enterprise / regulated** | Heavy | PMO governance. Formal gates, earned value, change control boards, compliance documentation. |
| **Fixed-price contract** | Heavy | Contractual scope baseline. Formal change orders. Acceptance criteria tied to payment milestones. |

### Decision framework

| Decision type | Who decides | Escalation |
|---------------|-------------|------------|
| Day-to-day technical | Team (SDLC Implementer) | Tech Lead → PM |
| Scope within sprint/iteration | Product Owner / SDLC Owner | PM → Sponsor |
| Scope change (project-level) | Change control process | PM → Steering Committee |
| Budget reallocation (within reserve) | Project Manager | PM → Sponsor |
| Budget increase | Sponsor / Steering Committee | Steering Committee → Executive |
| Schedule extension | Project Manager + Sponsor | Steering Committee |
| Risk acceptance | Risk owner (varies) | PM → Sponsor → Steering Committee |
| Project cancellation | Sponsor / Steering Committee | — |

---

## 4. Knowledge areas

PM knowledge areas represent the **competency domains** a project manager must navigate. Different approaches emphasize different areas — PMI/PMBOK defines 10 (6th ed) or reframes them as 8 performance domains (7th ed); PRINCE2 calls them "themes"; the concepts recur regardless of framework.

| Knowledge area | Core question | Key tools |
|----------------|---------------|-----------|
| **Scope** | What is included and excluded? | WBS, requirements traceability, scope baseline |
| **Schedule** | When will things be done? | Gantt charts, critical path, sprint/iteration planning |
| **Cost** | How much will it cost? | Budget baseline, earned value, cost forecasting |
| **Quality** | How good is good enough? | Quality metrics, audits, testing, Definition of Done |
| **Resources** | Who does the work? | Resource planning, team development, capacity management |
| **Risk** | What could go wrong (or right)? | Risk register, qualitative/quantitative analysis, response planning |
| **Communications** | Who needs to know what? | Communication plan, status reports, stakeholder updates |
| **Stakeholders** | Who cares and how do we engage them? | Stakeholder register, engagement assessment, influence mapping |
| **Procurement** | Do we make or buy? | Vendor evaluation, contracts, SLAs |
| **Integration** | How does it all fit together? | Project charter, change control, lessons learned |

**Agile note:** In Agile contexts, many knowledge areas are addressed through ceremonies and artifacts rather than dedicated PM plans — Sprint Planning (scope + schedule), Retrospectives (quality + improvement), Daily Standup (communications + risk). The knowledge **areas** still apply; the **mechanisms** differ.

---

## 5. Metrics framework

PM metrics focus on **project health** — are we on track to deliver within constraints? This complements SDLC metrics (delivery efficiency) and PDLC metrics (product outcomes).

| Category | Metrics | Measured when | Owner |
|----------|---------|---------------|-------|
| **Schedule** | Schedule Performance Index (SPI), milestone variance, critical path slack | Throughout execution | PM |
| **Cost** | Cost Performance Index (CPI), budget burn rate, Estimate at Completion (EAC) | Throughout execution | PM |
| **Scope** | Requirements stability, scope creep rate, change request volume | Throughout execution | PM + PO |
| **Quality** | Defect density, rework rate, acceptance criteria pass rate | Execution + monitoring | PM + QA |
| **Risk** | Open risk count, risk exposure (probability × impact), risk burn-down | Throughout | PM |
| **Stakeholder** | Stakeholder satisfaction, escalation frequency, engagement score | Periodic | PM |
| **Team** | Utilization, morale (eNPS), turnover during project | Periodic | PM + HR |

### Earned value management (EVM)

EVM integrates scope, schedule, and cost into a single measurement framework. Three base measurements, everything else derived:

| Measure | Definition |
|---------|------------|
| **Planned Value (PV)** | Budgeted cost of work **scheduled** to date |
| **Earned Value (EV)** | Budgeted cost of work **completed** to date |
| **Actual Cost (AC)** | Actual cost **spent** to date |

| Derived metric | Formula | Interpretation |
|----------------|---------|----------------|
| **SPI** | EV / PV | > 1 = ahead of schedule |
| **CPI** | EV / AC | > 1 = under budget |
| **EAC** | BAC / CPI | Forecast total cost at current efficiency |
| **TCPI** | (BAC − EV) / (BAC − AC) | Required future efficiency to finish on budget |

**Agile alternative:** Teams that do not use EVM can substitute burn-down/burn-up charts, velocity trends, and release forecasting. The underlying question ("are we on track?") is the same.

---

## 6. Review cadence (suggested)

| Cadence | Activity |
|---------|----------|
| **Daily** | Standup / sync: blockers, progress, impediments (often shared with SDLC Daily Scrum). |
| **Weekly** | PM status update: schedule, budget, risk, stakeholder issues. |
| **Per milestone / stage gate** | Formal review: deliverables inspected, go/no-go decision, budget and schedule reforecast. |
| **Monthly** | Steering committee update: project health dashboard, escalations, strategic alignment. |
| **Per phase transition** | Phase gate review: planning → execution, execution → closing. |
| **At closing** | Lessons learned, formal acceptance, resource release. |

---

## 7. Project lifecycle phases

While process groups describe **what** PM does, lifecycle phases describe **when** work flows through the project. The generic project lifecycle:

```blueprint-diagram
key: linear
alt: Diagram
```

| Phase | PM focus | PDLC overlap | SDLC overlap |
|-------|----------|--------------|--------------|
| **Feasibility** | Is this project worth doing? Business case, high-level estimates. | P1–P3 (Discover, Validate, Strategize) | — |
| **Initiation** | Charter, stakeholder register, PM assignment, authorization. | P3 (Strategize) output triggers initiation. | — |
| **Planning** | Detailed scope, schedule, budget, risk, quality, comms plans. | — | Phase A (Discover) overlaps for scope decomposition. |
| **Execution** | Direct work, manage team, coordinate deliverables. | — | Phases A–F (full SDLC delivery). |
| **Closing** | Formal acceptance, lessons learned, resource release. | P4 (Launch) — project closes, product continues. | Phase F (Release) — technical release precedes or coincides with project closure. |

**Iterative/Agile adjustment:** In Agile projects, planning and execution blend into repeated iterations. The "phase" boundaries become less distinct, but the governance concerns (budget tracking, risk management, stakeholder reporting) persist across iterations.

---

*Keep project-specific governance artifacts in project folders (e.g. `docs/development/`), not in this file.*
