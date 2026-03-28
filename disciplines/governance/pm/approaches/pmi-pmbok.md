# PMI / PMBOK

## What it is

**PMBOK** (Project Management Body of Knowledge) is the **standard** published by the **Project Management Institute (PMI)** — the world's largest PM professional association. It is not a methodology; it is a **body of knowledge** that describes principles, performance domains, and tailoring guidance applicable to any project management approach — predictive, Agile, hybrid, or otherwise.

The **7th edition** (2021) represented a major shift: from 10 knowledge areas and 49 processes (6th ed, 2017) to **12 principles** and **8 performance domains**. This moved PMBOK from a prescriptive process catalog to a principle-based framework that accommodates Agile and hybrid delivery without treating them as exceptions.

PMI also publishes the **Agile Practice Guide** (co-developed with the Agile Alliance) and the **Process Groups Practice Guide** (for teams that want the process-oriented structure from earlier editions). Together, these form a comprehensive PM reference ecosystem.

**When to use:** PMI/PMBOK is the right choice when your organization needs a **standards-based**, **internationally recognized** PM framework — for PMP certification alignment, PMO governance, government/defense contracts, or enterprise PM maturity programs. It is **not** prescriptive about delivery methodology, so it pairs with any SDLC approach.

---

## Authoritative sources (external)

| Resource | Executive summary (why it's linked here) |
|----------|------------------------------------------|
| [PMI — PMBOK Guide](https://www.pmi.org/pmbok-guide-standards/foundational/pmbok) | **Official** PMBOK standard — principles, performance domains, tailoring. The canonical source for PMI-based PM. Purchase required for full text. |
| [PMI — Agile Practice Guide](https://www.pmi.org/pmbok-guide-standards/practice-guides/agile) | **Official** PMI guidance on Agile delivery within a PM governance context — co-developed with the Agile Alliance. Bridges PMI and Agile communities. |
| [PMI — Process Groups Practice Guide](https://www.pmi.org/pmbok-guide-standards/practice-guides/process-groups) | **Companion** to PMBOK 7th ed for teams wanting the traditional **process-oriented** structure (Initiating → Planning → Executing → M&C → Closing) from earlier editions. |
| [Wikipedia — PMBOK](https://en.wikipedia.org/wiki/Project_Management_Body_of_Knowledge) | **Stable overview** of PMBOK history, editions, and relationship to PMP certification — entry point before the full standard. |
| [PMI — What is Project Management?](https://www.pmi.org/about/what-is-project-management) | **Introductory** definition of PM from PMI's perspective — shared vocabulary and framing. |

**Certification:** PMP (Project Management Professional) is the primary PMI certification. CAPM (Certified Associate in Project Management) is the entry-level equivalent. PMI-ACP (Agile Certified Practitioner) covers Agile contexts. This document summarizes concepts for adoption, not certification prep.

---

## Core structure — PMBOK 7th edition

### 12 Principles of project management

Principles are **foundational guidelines** for behavior and strategy, not prescriptive rules.

| # | Principle | Essence |
|---|-----------|---------|
| 1 | **Be a diligent, respectful, and caring steward** | Stewardship: act responsibly with resources, authority, and trust. |
| 2 | **Create a collaborative project team environment** | Build trust, shared understanding, and collective ownership. |
| 3 | **Effectively engage with stakeholders** | Proactively identify, analyze, and engage those affected by or affecting the project. |
| 4 | **Focus on value** | Align activities with business objectives and stakeholder value; remove non-value work. |
| 5 | **Recognize, evaluate, and respond to system interactions** | Projects exist within systems; understand dependencies, constraints, and feedback loops. |
| 6 | **Demonstrate leadership behaviors** | Motivate, influence, and enable the team regardless of formal authority. |
| 7 | **Tailor based on context** | Adapt the PM approach to the project's unique environment, constraints, and needs. |
| 8 | **Build quality into processes and deliverables** | Prevention over inspection; quality is designed in, not tested in. |
| 9 | **Navigate complexity** | Recognize and respond to uncertainty, ambiguity, interdependencies, and emergence. |
| 10 | **Optimize risk responses** | Continuously identify and address threats and opportunities proportionally. |
| 11 | **Embrace adaptability and resiliency** | Build the ability to respond to change and recover from setbacks. |
| 12 | **Enable change to achieve the envisioned future state** | Projects create change; manage both technical delivery and organizational adoption. |

### 8 Performance domains

Performance domains are **areas of focus** that interact and operate throughout the project — not sequential phases.

```blueprint-diagram
key: linear
alt: Diagram
```

| Domain | Focus | Key activities |
|--------|-------|----------------|
| **Stakeholders** | Engaging people who affect or are affected by the project | Identification, analysis, engagement strategies, satisfaction measurement |
| **Team** | Building and leading the project team | Acquisition, development, motivation, conflict resolution, distributed teams |
| **Development Approach & Life Cycle** | Choosing and adapting the delivery approach | Predictive vs adaptive vs hybrid selection, cadence, phase structure |
| **Planning** | Organizing and elaborating the work | Scope, schedule, cost, resource, quality, procurement, communications planning |
| **Project Work** | Executing and managing the planned work | Work authorization, knowledge management, process improvement |
| **Delivery** | Producing the project outputs and outcomes | Requirements management, scope validation, quality control |
| **Measurement** | Assessing performance and ensuring appropriate response | KPIs, dashboards, earned value, forecasting, variance analysis |
| **Uncertainty** | Addressing risk, ambiguity, and complexity | Risk identification, analysis, response planning, opportunity exploitation |

### PMBOK 6th vs 7th edition (key differences)

| Aspect | 6th edition (2017) | 7th edition (2021) |
|--------|--------------------|--------------------|
| **Structure** | 10 knowledge areas, 5 process groups, 49 processes | 12 principles, 8 performance domains |
| **Orientation** | Process-driven: inputs → tools & techniques → outputs | Principle-driven: outcome-focused guidance |
| **Delivery approach** | Primarily predictive; Agile as extension | Delivery-approach neutral; predictive, adaptive, hybrid treated equally |
| **Tailoring** | Implicit (you decide what to apply) | Explicit tailoring section: assess context, choose approach, adapt |
| **Companion** | Agile Practice Guide (appendix) | Process Groups Practice Guide (separate book for process-oriented teams) |

---

## Mapping to PM.md

| PMBOK 7th domain | PM.md process group | PM.md knowledge area |
|------------------|---------------------|---------------------|
| **Stakeholders** | Initiating (identify) + Executing (manage engagement) | Stakeholders |
| **Team** | Planning (resource plan) + Executing (team management) | Resources |
| **Development Approach & Life Cycle** | Planning (select approach) | Integration |
| **Planning** | Planning (all sub-activities) | Scope, Schedule, Cost, Quality, Risk, Communications, Procurement |
| **Project Work** | Executing (direct work) | Integration |
| **Delivery** | Executing + Monitoring | Scope, Quality |
| **Measurement** | Monitoring & Controlling | All (via metrics) |
| **Uncertainty** | Planning (risk plan) + Monitoring (risk monitor) | Risk |

---

## Mapping to SDLC and PDLC

### PMBOK ↔ SDLC

| PMBOK domain | SDLC connection |
|--------------|-----------------|
| **Development Approach & Life Cycle** | This is where PMBOK explicitly connects to SDLC. The PM selects whether delivery is predictive (phased/waterfall), adaptive (Scrum/Kanban/XP), or hybrid. The SDLC methodology **is** the delivery approach. |
| **Planning** | PMBOK planning wraps SDLC Phase A (Discover) — WBS, schedule, and budget envelope contain the backlog and sprint plan. |
| **Project Work + Delivery** | PMBOK execution governs SDLC Phases B–F. PM tracks progress, manages changes, reports to stakeholders while the engineering team delivers. |
| **Measurement** | PMBOK measurement (EVM, KPIs) consumes SDLC metrics (velocity, cycle time, defect rate) as inputs and adds project-level metrics (SPI, CPI, milestone variance). |
| **Uncertainty** | PMBOK risk management complements SDLC technical risk. PM tracks schedule/budget/dependency risks; SDLC tracks technical/security/performance risks. |

### PMBOK ↔ PDLC

| PMBOK domain | PDLC connection |
|--------------|-----------------|
| **Stakeholders** | Maps to PDLC's product trio and stakeholder engagement. PM stakeholder management extends PDLC's user-centric discovery to include sponsors, governance, and organizational stakeholders. |
| **Planning** | PM planning receives PDLC P3 (Strategize) outputs: validated problem, solution concept, success metrics. These become the project's objectives and scope. |
| **Delivery** | PMBOK delivery produces the increment that crosses into PDLC P4 (Launch). PM ensures the deliverable meets the quality and scope criteria before handoff to market activation. |
| **Measurement** | PMBOK tracks project metrics (on time, on budget). PDLC P5 (Grow) tracks outcome metrics (adoption, retention). Both are needed; neither substitutes for the other. |

---

## Anti-patterns

| Anti-pattern | Fix |
|-------------|-----|
| **PMBOK as bureaucracy** | PMBOK 7th edition explicitly advocates tailoring. Do not apply all 49 processes from the 6th edition to a 3-person team. Use the 12 principles as a lens; scale processes to fit. |
| **PMP certification as PM ability** | PMP tests knowledge of the standard, not project leadership ability. Certification is a starting point, not proof of competence. |
| **Predictive-only PMBOK** | PMBOK 7th ed is delivery-approach neutral. If your PMO mandates waterfall "because PMBOK says so," they are citing a version that no longer exists. |
| **PMBOK without SDLC discipline** | PMBOK provides governance, not delivery methodology. You still need CI/CD, testing, DoD, and engineering practices. PMBOK + no SDLC = managed chaos. |
| **Ignoring the Development Approach domain** | If the PM selects the delivery approach without engineering input, you get methodology mismatch. The Dev Approach domain should be a **joint decision** between PM, PO, and Tech Lead. |

---

## Further reading

- [PMI — Standards Library](https://www.pmi.org/pmbok-guide-standards) — Full catalog of PMI standards and practice guides.
- [PMBOK-SDLC-PDLC Bridge](../PM-SDLC-PDLC-BRIDGE.md) — Three-domain relationship
- Companion: [PRINCE2](prince2.md), [Six Sigma](six-sigma.md)
- SDLC methodologies: [Scrum](../../../../sdlc/methodologies/scrum.md), [Kanban](../../../../sdlc/methodologies/kanban.md), [Phased delivery](../../../../sdlc/methodologies/phased-delivery.md)
- PDLC approaches: [Stage-Gate](../../../../pdlc/approaches/stage-gate.md), [Dual-Track Agile](../../../../pdlc/approaches/dual-track-agile.md)
