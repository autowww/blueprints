---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Requirements Life Cycle Management

Ensures requirements are **traced** to business objectives, **maintained** as understanding evolves, **prioritized** for delivery, and formally **approved** by stakeholders. This knowledge area governs the requirements themselves — not what they say (that is Requirements Analysis & Design Definition), but how they are managed over time.

**BABOK alignment:** Knowledge Area 5 (Requirements Life Cycle Management).

**Lifecycle mapping:** Primarily **PDLC P3** (scope definition, prioritization) and **SDLC A–B** (backlog management, specification approval), with ongoing maintenance through delivery and post-launch iteration.

---

## 1. Tasks

### 1.1 Trace requirements

Establish and maintain relationships between requirements at different levels and between requirements and other artifacts (tests, designs, business objectives).

| Input | Output |
|-------|--------|
| Requirements, business objectives, design elements, test cases | Traceability matrix |

**Traceability relationships:**

| From | To | Purpose |
|------|----|---------|
| Business requirement | Stakeholder requirement | Confirms stakeholder needs serve business objectives |
| Stakeholder requirement | Solution requirement (functional) | Confirms solution capabilities address stakeholder needs |
| Functional requirement | Test case | Confirms every requirement is verified |
| Functional requirement | Design element | Confirms every requirement is implemented |
| Non-functional requirement | Architecture decision | Confirms quality attributes drive design choices |

**Project mapping:** Traceability artifacts live in `docs/requirements/traceability/` — the existing `themes-matrix.csv` and `tests-matrix.csv` implement this task. The ID scheme in [`docs/requirements/STRUCTURE-PROPOSAL.md`](../../../../docs/requirements/STRUCTURE-PROPOSAL.md) (M{n}E{n}S{n}T{n}) provides the structural backbone.

### 1.2 Maintain requirements

Keep requirements current as understanding evolves through elicitation, design, build, and feedback.

| Input | Output |
|-------|--------|
| Change requests, new information, elicitation results | Updated requirements, change log |

**Maintenance triggers:**
- New information from elicitation (confirmed results that modify existing requirements)
- Design discoveries (architectural constraints that change solution requirements)
- Build feedback (implementation reveals requirement ambiguity or infeasibility)
- Testing feedback (defects that trace to requirement gaps)
- Post-launch feedback (P5 usage data that reveals unmet or changed needs)

**In agile contexts:** Requirements maintenance happens continuously through backlog refinement. User stories are elaborated just ahead of delivery sprints. Acceptance criteria are refined during sprint planning.

### 1.3 Prioritize requirements

Rank requirements by business value, risk, cost, dependencies, and regulatory obligation to guide delivery sequencing.

| Input | Output |
|-------|--------|
| Requirements, business objectives, constraints, stakeholder preferences | Prioritized requirements |

**Prioritization techniques:**

| Technique | Best For | Approach |
|-----------|----------|----------|
| **MoSCoW** | Scope negotiation, release planning | Classify as Must/Should/Could/Won't |
| **Value/effort matrix** | Feature comparison, sprint planning | Plot value vs implementation effort |
| **Kano model** | Product differentiation, UX prioritization | Classify as basic/performance/delighter |
| **Weighted scoring** | Complex multi-criteria decisions | Score against multiple weighted factors |
| **Story mapping** | User journey-based prioritization | Organize by user activity, then slice horizontally |
| **Cost of delay** | Time-sensitive decisions | Quantify the cost of not implementing now |

**PDLC connection:** Prioritization at P3 determines what enters SDLC; at P5, usage data informs re-prioritization for iteration.

### 1.4 Assess requirements changes

Evaluate the impact of proposed changes on scope, schedule, quality, and other requirements.

| Input | Output |
|-------|--------|
| Change request, current requirements baseline, project constraints | Impact assessment (scope, effort, risk, dependencies affected) |

**Change assessment checklist:**
- What requirements are affected (direct and indirect via traceability)?
- What is the effort to implement the change?
- What is the risk of implementing vs not implementing?
- What is the impact on the delivery timeline?
- What other requirements or components are affected?
- Does this change require re-validation with stakeholders?

### 1.5 Approve requirements

Obtain formal stakeholder agreement that requirements are complete, correct, and ready to be acted upon.

| Input | Output |
|-------|--------|
| Requirements package, stakeholder feedback | Approved requirements (baselined) |

**Approval approaches by methodology:**

| Methodology | Approval Style |
|-------------|----------------|
| **Phased / waterfall** | Formal sign-off document; baselined requirements; change control board |
| **Scrum** | Product Owner approval during sprint planning; acceptance criteria agreement |
| **Kanban** | Pull-based; requirements approved when team pulls work item |
| **SAFe** | PI Planning alignment; ART-level approval for features; team-level for stories |

---

## 2. Techniques commonly used

| Technique | Usage in This Knowledge Area |
|-----------|------------------------------|
| Traceability matrix | Establish and maintain requirement relationships (§1.1) |
| Impact analysis | Assess effects of proposed changes (§1.4) |
| MoSCoW prioritization | Classify requirements by necessity (§1.3) |
| Value/effort matrix | Compare requirements by return and cost (§1.3) |
| Kano model | Classify requirements by stakeholder delight impact (§1.3) |
| Story mapping | Organize requirements by user journey (§1.3) |
| Backlog management | Maintain requirements in agile contexts (§1.2) |
| Configuration management | Version control for requirements artifacts (§1.2) |
| Reviews and walkthroughs | Validate requirements with stakeholders (§1.5) |
| Decision analysis | Resolve conflicting prioritization inputs (§1.3) |

Full technique catalog: [`techniques/README.md`](../techniques/README.md).

---

## 3. Relationship to PDLC and SDLC

| RLCM Task | PDLC Mapping | SDLC Mapping |
|-----------|--------------|--------------|
| Trace requirements | P3: link requirements to business objectives and success metrics | A–B: link requirements to WBS items, tests, design elements |
| Maintain requirements | P5: update requirements based on usage data and feedback | A–F: refine stories during sprints, update specs after design decisions |
| Prioritize requirements | P3: prioritize for roadmap and release planning | A: prioritize for sprint backlog |
| Assess changes | P5: evaluate new feature requests against current strategy | A (iteration): assess impact of mid-sprint scope changes |
| Approve requirements | P3/G3: stakeholder approval for initiative scope | B: acceptance criteria approval per story |

### Connection to spec-driven development

The requirements management practices in this knowledge area complement the **spec-driven development** methodology in [`blueprints/sdlc/methodologies/spec-driven-development.md`](../../../../sdlc/methodologies/spec-driven-development.md). Spec-driven development emphasizes **intent-first** specification — writing clear, verifiable specifications before implementation. Requirements Life Cycle Management adds the **governance layer**: tracing, prioritizing, and maintaining those specifications across their lifetime.
