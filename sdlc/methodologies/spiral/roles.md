# Spiral Model — roles (prescriptive)

The Spiral Model defines roles around **risk management** and **stakeholder commitment**. Teams are typically more structured than in lightweight Agile but share accountability for risk-informed decisions.

## 1. Project manager

| Aspect | Guidance |
|--------|----------|
| **Accountable for** | Spiral planning, schedule, resource allocation, stakeholder communication |
| **Archetypes** | **Orchestrator** (primary) |
| **Key outputs** | Spiral plans, milestone evidence packages, status reports, risk register coordination |

Drives the cadence of spirals and ensures anchor-point milestones receive proper stakeholder attention.

## 2. Risk analyst / chief engineer

| Aspect | Guidance |
|--------|----------|
| **Accountable for** | Identifying, analyzing, and proposing resolution strategies for top risks in Q2 |
| **Archetypes** | **Quality advocate** (primary), **Orchestrator** (risk coordination) |
| **Key outputs** | Risk register, risk analysis reports, prototype/simulation recommendations, risk resolution evidence |

May be a dedicated role or combined with chief architect on smaller teams. The critical requirement is that **someone** owns systematic risk analysis each spiral.

## 3. Chief architect / technical lead

| Aspect | Guidance |
|--------|----------|
| **Accountable for** | Architecture evolution across spirals; technical feasibility; design integrity |
| **Archetypes** | **Implementer** (architecture), **Quality advocate** (structural integrity) |
| **Key outputs** | Architecture documents, design decisions (ADRs), prototype architectures, NFR strategies |

**Prescriptive rule:** Architecture should be **validated** in early spirals (prototypes, proof-of-concept) before committing to full-scale build in later spirals.

## 4. Development team

| Aspect | Guidance |
|--------|----------|
| **Accountable for** | Q3 execution — design, code, test, integrate within the spiral's scope |
| **Archetypes** | **Implementer** (primary), **Quality advocate** (testing) |
| **Key outputs** | Working increments, test results, build artifacts |

Team composition may change across spirals (e.g. more prototyping specialists early, more production engineers later).

## 5. Stakeholders / sponsors

| Aspect | Guidance |
|--------|----------|
| **Accountable for** | Funding commitment, objective validation, go/no-go at anchor-point milestones |
| **Archetypes** | **Sponsor proxy**, **Steer** |
| **Key outputs** | Commitment decisions, constraint definitions, acceptance of risk trade-offs |

**Prescriptive rule:** Stakeholders must be **engaged** at anchor-point milestones (LCO, LCA, IOC). Passive sponsorship undermines the risk-driven model.

## 6. Ceremony participation matrix

| Ceremony | PM | Risk analyst | Architect | Dev team | Stakeholders |
|----------|----|----|-----------|----------|--------------|
| Spiral planning (Q1) | R | R | R | O | O |
| Risk review (Q2) | R | R | R | O | O |
| Development sync (Q3) | O | O | R | R | — |
| Anchor-point review (Q4) | R | R | R | R | R |
| Prototype demo | R | O | R | R | R |
| Retrospective | R | O | O | R | — |

## 7. Anti-patterns (by role)

| Anti-pattern | Why it hurts | Fix |
|--------------|--------------|-----|
| **No dedicated risk analyst** | Risk analysis becomes superficial or skipped | Assign explicit risk-analysis accountability |
| **Stakeholders delegate anchor-point decisions** | Resources committed without informed consent | Require sponsor presence at LCO/LCA/IOC |
| **Architect absent from early spirals** | Architecture not validated before scale | Architect participates from spiral 1 |
| **PM treats all spirals as identical phases** | Loses the adaptive, risk-driven nature | Vary spiral scope and approach based on risk profile |

## 8. Links

- [Ceremonies](ceremonies-prescriptive.md) · [Foundation](foundation-connection.md)
