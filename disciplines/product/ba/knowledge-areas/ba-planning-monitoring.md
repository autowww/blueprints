# BA Planning & Monitoring

The governance knowledge area — defines **how** business analysis work is planned, organized, and monitored for a given initiative. It sets the foundation for all other knowledge areas.

**BABOK alignment:** Knowledge Area 2 (BA Planning and Monitoring).

**Lifecycle mapping:** Applies across **all** PDLC and SDLC phases as a governance layer. Heaviest at initiative start (P1/A), revisited when context changes.

---

## 1. Tasks

### 1.1 Plan BA approach

Determine the methodology, techniques, timing, and deliverables for BA work on this initiative.

| Input | Output |
|-------|--------|
| Business need, organizational context, project constraints | BA approach (formality level, technique selection, delivery cadence) |

**Considerations:**
- Predictive (waterfall) vs adaptive (agile) vs hybrid — match the delivery methodology in [`blueprints/sdlc/methodologies/`](../../../../sdlc/methodologies/README.md)
- Regulatory and compliance requirements that mandate documentation rigor
- Team experience with BA techniques
- Stakeholder availability and geographic distribution

### 1.2 Plan stakeholder engagement

Identify all stakeholders, understand their interests and influence, and define how to engage them throughout the initiative.

| Input | Output |
|-------|--------|
| Business need, organizational structure | Stakeholder register, engagement plan |

**Stakeholder categories:**
- **Domain SMEs** — deep knowledge of current state and business rules
- **End users** — experience the solution daily; source of usability and workflow requirements
- **Sponsors** — fund and authorize the initiative; gate decision makers
- **Regulators** — impose constraints that become non-functional requirements
- **Implementation team** — consumes requirements; provides feasibility feedback
- **Support / operations** — impacted by transition; source of post-launch requirements

Use [`templates/stakeholder-register.template.md`](../templates/stakeholder-register.template.md) to document stakeholder analysis.

### 1.3 Plan BA governance

Define how requirements will be reviewed, approved, changed, and communicated.

| Input | Output |
|-------|--------|
| BA approach, stakeholder engagement plan, organizational standards | Governance framework (approval process, change control, communication plan) |

**Governance elements:**
- Requirements review cadence (maps to SDLC ceremonies — C1 Align, C4 Inspect in [`ceremonies/`](../../../../sdlc/methodologies/ceremonies/))
- Change control process (who approves scope changes, what impact assessment is required)
- Communication plan (who gets what information, when, in what format)
- Decision authority matrix (who can approve/reject/defer requirements)

### 1.4 Plan BA information management

Determine how BA artifacts will be stored, organized, versioned, and accessed.

| Input | Output |
|-------|--------|
| BA approach, organizational standards, tool landscape | Information management approach |

In this blueprint ecosystem, BA artifacts live in:
- **`docs/requirements/`** — formal requirements, WBS, traceability matrices
- **`docs/product/`** — product-functional prose (vision, personas, journeys, features)
- **`docs/product/discovery/`** — research synthesis, experiment logs (PDLC P1–P2)
- **`docs/adr/`** — architectural decisions influenced by BA analysis

### 1.5 Identify BA performance improvements

Assess the effectiveness of BA work and adjust the approach.

| Input | Output |
|-------|--------|
| BA work results, stakeholder feedback, delivery outcomes | Performance assessment, improvement actions |

**Metrics for BA effectiveness:**
- Requirements defect rate (requirements-related bugs found during/after build)
- Requirements stability (change rate after baseline)
- Stakeholder satisfaction with BA process
- Time from elicitation to approved requirement
- Traceability coverage (% of requirements linked to tests and business objectives)

---

## 2. Techniques commonly used

| Technique | Usage in This Knowledge Area |
|-----------|------------------------------|
| Stakeholder analysis | Identify and classify stakeholders (§1.2) |
| RACI matrix | Clarify decision authority (§1.3) |
| Estimation | Plan BA effort and timeline (§1.1) |
| Interviews | Gather organizational context and constraints (§1.1) |
| Lessons learned | Identify BA process improvements (§1.5) |
| Metrics and KPIs | Measure BA performance (§1.5) |
| Risk analysis | Assess risks to BA approach success (§1.1) |

Full technique catalog: [`techniques/README.md`](../techniques/README.md).

---

## 3. Relationship to PDLC and SDLC

| BA Planning Activity | PDLC Mapping | SDLC Mapping |
|---------------------|--------------|--------------|
| Plan BA approach | Informed by PDLC phase (P1 discovery needs different BA than P5 evaluation) | Informed by delivery methodology (agile BA for Scrum, formal BA for phased) |
| Plan stakeholder engagement | Stakeholders from PDLC roles (PM, UX Researcher, GTM Lead) | Stakeholders from SDLC roles (Owner, Implementer, QA) |
| Plan BA governance | Aligns with PDLC stage gates (G1–G5) | Aligns with SDLC phase exits and DoD |
| Monitor BA performance | PDLC outcome metrics inform solution evaluation quality | SDLC defect metrics inform requirements quality |
