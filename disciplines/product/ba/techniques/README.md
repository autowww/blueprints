# BA techniques catalog

Master catalog of business analysis techniques from the [BABOK Guide v3](https://www.iiba.org/babok-guide/), mapped to knowledge areas and lifecycle phases. Use this as a **selection guide** — pick techniques that fit your initiative's context, formality level, and team capability.

**How to use this catalog:**
1. Identify which **lifecycle phase** you are in (PDLC P1–P6 or SDLC A–F)
2. Find techniques that apply to that phase in the table below
3. Select based on your **BA calibration** — see [`BA-SDLC-PDLC-BRIDGE.md`](../BA-SDLC-PDLC-BRIDGE.md) §6 for when to go lightweight vs heavyweight
4. Refer to the technique detail section for guidance on each technique

---

## 1. Technique matrix

Each technique is mapped to the knowledge areas where it is primarily used and the lifecycle phases where it is most applicable.

**Knowledge area abbreviations:** BAPM = BA Planning & Monitoring, SA = Strategy Analysis, EC = Elicitation & Collaboration, RLCM = Requirements Life Cycle Management, RADD = Requirements Analysis & Design Definition, SE = Solution Evaluation.

### Elicitation techniques

| Technique | Knowledge Areas | PDLC Phases | SDLC Phases | Description |
|-----------|----------------|-------------|-------------|-------------|
| **Interviews** | EC, SA | P1, P2 | A | One-on-one or small-group structured/semi-structured conversations to gather detailed stakeholder perspectives |
| **Workshops / facilitated sessions** | EC, SA, RADD | P1, P2, P3 | A, B | Structured group sessions to build consensus, explore problems, or define requirements collaboratively |
| **Focus groups** | EC, SA | P1, P2 | — | Moderated group discussions with representative stakeholders to explore attitudes and reactions |
| **Observation / job shadowing** | EC, SA | P1 | A | Watching users in their natural environment to understand actual workflows and pain points |
| **Surveys / questionnaires** | EC, SE | P1, P5 | — | Structured instruments for gathering data from large groups; useful for quantifying patterns |
| **Document analysis** | EC, SA | P1 | A | Systematic review of existing documentation, contracts, regulations, and system artifacts |
| **Interface analysis** | EC, RADD | — | A, B | Examination of interfaces between systems, users, and processes to identify integration requirements |
| **Prototyping** | EC, RADD | P2 | B, C | Building simplified representations of a solution to validate concepts and surface implicit requirements |
| **Brainstorming** | EC, RADD | P2 | A | Unconstrained idea generation to explore solution possibilities; quantity over quality initially |

### Analysis techniques

| Technique | Knowledge Areas | PDLC Phases | SDLC Phases | Description |
|-----------|----------------|-------------|-------------|-------------|
| **SWOT analysis** | SA, SE | P1, P3 | — | Assess Strengths, Weaknesses, Opportunities, and Threats for an initiative or solution |
| **PESTLE analysis** | SA | P1 | — | Assess Political, Economic, Social, Technological, Legal, and Environmental external factors |
| **Root cause analysis** | SA, SE | P1, P5 | E | Systematically investigate the underlying cause of a problem, not just symptoms |
| **Gap analysis** | SA, SE | P1, P5 | — | Compare current state to desired future state; identify what must change |
| **Benchmarking** | SA, EC, SE | P1, P5 | — | Compare capabilities, processes, or performance against industry standards or competitors |
| **Feasibility analysis** | SA, RADD | P2, P3 | C | Assess whether a proposed solution is technically, financially, and organizationally achievable |
| **Risk analysis** | SA, BAPM | P2, P3 | A | Identify threats and opportunities; assess probability and impact; define mitigation strategies |
| **Cost-benefit analysis** | SA, SE | P3, P5 | — | Quantify expected costs and benefits to justify investment or evaluate returns |
| **Decision analysis** | SA, RADD, SE | P3 | C | Structured evaluation of alternatives using defined criteria and weights |
| **Business model canvas** | SA | P3 | — | Visual framework for articulating value proposition, customers, channels, revenue, and cost structure |

### Specification techniques

| Technique | Knowledge Areas | PDLC Phases | SDLC Phases | Description |
|-----------|----------------|-------------|-------------|-------------|
| **User story writing** | RADD, RLCM | P2 | A, B | Short narratives: "As a [role], I want [capability], so that [benefit]" — core agile specification format |
| **Use case modeling** | RADD | P2 | B | Detailed step-by-step interaction between actors and the system; includes alternate and exception flows |
| **Acceptance criteria (Given/When/Then)** | RADD | — | B | Verifiable conditions for requirement completion; Gherkin format for automated testing |
| **Business rules analysis** | RADD | — | B | Identify, document, and validate the business rules that constrain or govern solution behavior |
| **Data modeling** | RADD | — | B, C | Define entities, attributes, relationships, and constraints — ER diagrams, data dictionaries |
| **Process modeling (BPMN)** | RADD, SA | P1 | B | Visual representation of workflows using Business Process Model and Notation |
| **State modeling** | RADD | — | B | Define valid states and transitions for lifecycle-driven entities (state machine diagrams) |
| **Non-functional requirements analysis** | RADD | — | B, C | Systematically identify and specify quality attributes: performance, security, scalability, accessibility |
| **Scope modeling** | SA, RLCM | P3 | A | Define solution boundaries — what is in scope, out of scope, and deferred |

### Prioritization techniques

| Technique | Knowledge Areas | PDLC Phases | SDLC Phases | Description |
|-----------|----------------|-------------|-------------|-------------|
| **MoSCoW prioritization** | RLCM | P3 | A | Classify requirements as Must have, Should have, Could have, Won't have (this time) |
| **Value/effort matrix** | RLCM, SA | P3 | A | Plot requirements on a 2x2 matrix of business value vs implementation effort |
| **Kano model** | RLCM | P3 | — | Classify requirements as basic (expected), performance (linear), or delighter (surprising) |
| **Weighted scoring** | RLCM, SA | P3 | A | Score alternatives against multiple criteria with assigned weights |
| **Story mapping** | RLCM, RADD | — | A | Organize user stories along a journey backbone; slice horizontally for release planning |
| **Cost of delay** | RLCM | P3 | A | Quantify the economic cost of not implementing a requirement now vs later |
| **Estimation** | BAPM, RLCM | P3 | A | Size requirements for planning — story points, t-shirt sizes, ideal days, or parametric methods |

### Governance and management techniques

| Technique | Knowledge Areas | PDLC Phases | SDLC Phases | Description |
|-----------|----------------|-------------|-------------|-------------|
| **Stakeholder analysis** | BAPM, EC | P1 | A | Identify stakeholders, assess influence/interest, plan engagement strategies |
| **RACI matrix** | BAPM | P3 | A | Clarify Responsible, Accountable, Consulted, Informed roles per decision or artifact |
| **Traceability matrix** | RLCM | P3 | A, B | Link requirements to objectives, tests, and design elements; detect gaps and orphans |
| **Impact analysis** | RLCM | P5 | A | Assess the effect of proposed changes on scope, schedule, quality, and other requirements |
| **Reviews and walkthroughs** | RADD, RLCM | P2, P3 | B | Structured examination of requirements with stakeholders to verify quality and completeness |
| **Lessons learned** | BAPM, SE | P5, P6 | F | Capture what worked and what did not for future BA initiatives |
| **Metrics and KPIs** | BAPM, SE | P5 | E | Define and track measurable indicators of BA effectiveness and solution performance |
| **Configuration management** | RLCM | — | A–F | Version control and change tracking for requirements artifacts (git-native in this ecosystem) |

---

## 2. Technique selection by lifecycle phase

Quick reference — which techniques to reach for at each phase:

| Phase | Recommended Techniques |
|-------|------------------------|
| **P1 Discover Problem** | Interviews, observation, document analysis, SWOT, PESTLE, benchmarking, stakeholder analysis, root cause analysis, process modeling |
| **P2 Validate Solution** | Prototyping, workshops, use case modeling, user stories, feasibility analysis, risk analysis, reviews, acceptance criteria |
| **P3 Strategize** | Decision analysis, business model canvas, cost-benefit analysis, MoSCoW, scope modeling, RACI, estimation, weighted scoring, traceability matrix |
| **A Discover** | Story mapping, user stories, scope modeling, stakeholder analysis, estimation, backlog management |
| **B Specify** | Acceptance criteria, use cases, data modeling, state modeling, business rules, NFR analysis, interface analysis, reviews |
| **C Design** | Decision analysis, feasibility analysis, prototyping, NFR analysis |
| **D Build** | Impact analysis (for mid-sprint changes), acceptance criteria clarification |
| **E Verify** | Metrics and KPIs, root cause analysis (defects), traceability matrix (coverage check) |
| **F Release** | Reviews, lessons learned, configuration management |
| **P4 Launch** | Reviews, stakeholder analysis (support/operations readiness) |
| **P5 Grow** | Gap analysis, root cause analysis, surveys, benchmarking, impact analysis, lessons learned, metrics and KPIs |
| **P6 Mature / Sunset** | Cost-benefit analysis, decision analysis, lessons learned, SWOT |

---

## 3. Technique selection by BA calibration

| Calibration | Techniques to Use | Techniques to Skip |
|-------------|-------------------|--------------------|
| **Lightweight** (bug fix, small feature) | User stories, acceptance criteria, backlog management | Use case modeling, BPMN, SWOT, PESTLE, business model canvas |
| **Medium** (feature on mature product) | User stories, acceptance criteria, interviews, MoSCoW, traceability matrix, data modeling | PESTLE, business model canvas, formal RACI |
| **Heavyweight** (greenfield, enterprise) | All of the above + use case modeling, process modeling, SWOT, business case, RACI, scope modeling, formal reviews | — (use everything that applies) |

See [`BA-SDLC-PDLC-BRIDGE.md`](../BA-SDLC-PDLC-BRIDGE.md) §6 for detailed calibration guidance.
