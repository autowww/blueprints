---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Phased delivery — ceremonies (prescriptive)

Below: typical **stage-gate** ceremonies. Adjust names to your PMO standard (PRINCE2, PMBOK, internal SDLC).

---

## 1. Initiation / charter (gate: project authorized)

**Intent:** **C1**.

| | |
|--|--|
| **Inputs** | Business case draft, high-level scope, constraints |
| **Outputs** | Signed charter; appointed PM; initial RAID |
| **Participants** | Sponsor (**R**), PM (**R**), key stakeholders (**C**) |
| **Timebox** | Project-sized (days–weeks) |

**Agenda:** problem statement → success measures → high-level scope → risks → decision.

---

## 2. Planning baseline (gate: plan approved)

**Intent:** **C1** + **C2**.

| | |
|--|--|
| **Inputs** | Requirements outline, estimates, dependencies |
| **Outputs** | Baseline schedule, WBS, budget, communication plan |
| **Participants** | PM (**R**), BA (**R**), tech lead (**R**), sponsor (**A** on go) |

**Meetings:** planning workshop series; document **baseline change** rules.

---

## 3. Design review (technical gate)

**Intent:** **C2** + **C4** (quality of solution pre-build).

| | |
|--|--|
| **Inputs** | Design docs, NFR matrix, security/privacy assessment |
| **Outputs** | Approved design baseline or **actions** list |
| **Participants** | Tech lead (**R**), security/architecture peers (**C**), PM (**O**) |

**Agenda:** walkthrough → risks → decision / conditions.

---

## 4. Weekly status / steering prep

**Intent:** **C3** + **C1** (escalations).

| | |
|--|--|
| **Inputs** | Schedule variance, RAID updates, burn/EVM if used |
| **Outputs** | Decisions, escalations, comms pack |
| **Participants** | PM (**R**), team leads (**R**), sponsor (**O** unless steering that week) |

**Timebox:** 30–60 min.

---

## 5. Test readiness review (TRR)

**Intent:** **C4**.

| | |
|--|--|
| **Inputs** | Test plans, environments, entry criteria, traceability matrix |
| **Outputs** | **Go** to formal test / **hold** with actions |
| **Participants** | QA lead (**R**), tech lead (**R**), PM (**R**) |

---

## 6. UAT / acceptance

**Intent:** **C4**.

| | |
|--|--|
| **Inputs** | UAT scripts, training materials, stable build |
| **Outputs** | Signed acceptance or defect list with severity |
| **Participants** | Business owner (**A**), BA (**R**), PM (**R**), support (**O**) |

**Prescriptive rule:** Define **objective** acceptance (pass/fail per script), not “looks fine.”

---

## 7. Go-live / release readiness

**Intent:** **C1** + **E**.

| | |
|--|--|
| **Inputs** | Release checklist, rollback plan, comms, support roster |
| **Outputs** | **Go** / **no-go**; dated release |
| **Participants** | PM (**R**), ops (**R**), sponsor (**A**), security (**C**) |

---

## 8. Post-implementation review (PIR)

**Intent:** **C5** + **C6**.

| | |
|--|--|
| **Inputs** | Benefits measures, incident data, budget final |
| **Outputs** | Lessons learned register; follow-up actions |
| **Participants** | Sponsor (**O**), PM (**R**), BA, tech lead, operations (**R**) |

---

## 9. Quick I/O summary

| Ceremony | Primary output |
|----------|----------------|
| Charter gate | Authorized project |
| Planning gate | Baselines |
| Design review | Technical approval |
| TRR | Test entry |
| UAT | Acceptance |
| Release readiness | Production go |
| PIR | Organizational learning |

## 10. Links

- [Process maps](process-and-flows.md) · [Foundation](foundation-connection.md)
