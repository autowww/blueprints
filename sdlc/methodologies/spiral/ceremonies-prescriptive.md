---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Spiral Model — ceremonies (prescriptive)

The Spiral Model organizes work around **quadrant transitions** and **anchor-point milestones**. Below: key ceremonies mapped to the four-quadrant cycle.

---

## 1. Spiral planning (Q1 — objectives)

**Intent:** **C1** + **C2**.

| | |
|--|--|
| **Inputs** | Results from previous spiral, stakeholder feedback, updated constraints |
| **Outputs** | Objectives for this spiral, alternatives identified, risk candidates listed |
| **Participants** | PM (**R**), risk analyst (**R**), architect (**R**), stakeholders (**O**) |
| **Timebox** | Half day to 2 days (scales with spiral scope) |

**Agenda:**

1. Review previous spiral outcomes and open risks.
2. Define objectives and success criteria for this cycle.
3. Identify alternatives and constraints.
4. Agree on risk-analysis approach for Q2.

---

## 2. Risk review (Q2 — identify & resolve)

**Intent:** **C1** + **C6** (risk-driven assurance).

| | |
|--|--|
| **Inputs** | Risk register, prototypes/simulations from prior spirals, new risk candidates |
| **Outputs** | Prioritized risk list, resolution strategies, go/no-go for Q3 build scope |
| **Participants** | Risk analyst (**R**), architect (**R**), PM (**R**), domain experts (**O**) |
| **Timebox** | 2–4 hours per spiral (more for early spirals with high uncertainty) |

**Agenda:**

1. Present top risks with likelihood, impact, and evidence.
2. Review prototype/simulation results addressing prior risks.
3. Propose resolution strategies (prototype, mitigate, accept, avoid).
4. Decide build scope for Q3 based on acceptable risk level.

---

## 3. Development sync (Q3 — build)

**Intent:** **C3**.

| | |
|--|--|
| **Inputs** | Spiral plan, risk-adjusted scope, design artifacts |
| **Outputs** | Coordination decisions, blocked items escalated |
| **Participants** | Dev team (**R**), architect (**R**), PM (**O**) |
| **Timebox** | 15–30 min (daily or as needed) |

Within Q3, teams may use any development approach (Agile iterations, focused build phases) appropriate to the spiral's scope and risk profile.

---

## 4. Prototype demo

**Intent:** **C4** + **C6** (risk reduction evidence).

| | |
|--|--|
| **Inputs** | Working prototype addressing identified risks |
| **Outputs** | Risk resolution evidence, stakeholder feedback, refined requirements |
| **Participants** | Dev team (**R**), architect (**R**), stakeholders (**R**), risk analyst (**R**) |
| **Timebox** | 1–2 hours |

**Prescriptive rule:** Prototypes exist to **reduce risk**, not to become production code. Document which risks the prototype addresses and what was learned.

---

## 5. Anchor-point milestone review (Q4)

**Intent:** **C4** + **C1** (commitment gate for next spiral).

| | |
|--|--|
| **Inputs** | Spiral deliverables, risk register status, evidence packages |
| **Outputs** | Stakeholder commitment (go / no-go / redirect), updated objectives for next spiral |
| **Participants** | Stakeholders (**R**, decision), PM (**R**), risk analyst (**R**), architect (**R**), dev team (**R**) |
| **Timebox** | 2–4 hours |

### Anchor-point milestones (Boehm)

| Milestone | When | Decision |
|-----------|------|----------|
| **LCO — Life Cycle Objectives** | After initial spirals | Are objectives clear, feasible, and worth pursuing? |
| **LCA — Life Cycle Architecture** | After architecture spirals | Is the architecture sound and risks manageable? |
| **IOC — Initial Operational Capability** | After build spirals | Is the system ready for operational use? |

---

## 6. Retrospective

**Intent:** **C5**.

| | |
|--|--|
| **Inputs** | Spiral execution data, risk prediction accuracy, schedule variance |
| **Outputs** | Process improvements for next spiral, updated risk-analysis practices |
| **Participants** | PM (**R**), dev team (**R**), risk analyst (**O**), architect (**O**) |
| **Timebox** | 1–2 hours |

**Spiral twist:** Compare **predicted** vs **actual** risk outcomes. Improve the team's **risk identification** and **estimation** capability, not just engineering practices.

---

## 7. Quick I/O summary

| Ceremony | Primary output |
|----------|----------------|
| Spiral planning | Objectives, alternatives, risk candidates |
| Risk review | Prioritized risks, resolution strategies, build scope |
| Dev sync | Coordination, unblocked items |
| Prototype demo | Risk resolution evidence, refined requirements |
| Anchor-point review | Stakeholder commitment, next-spiral direction |
| Retrospective | Process and risk-estimation improvements |

## 8. Links

- [Process maps](process-and-flows.md) · [Foundation](foundation-connection.md)
