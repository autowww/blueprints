---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# V-Model — ceremonies (prescriptive)

The V-Model's ceremonies center on **design reviews** (left-side gates) and **test reviews** (right-side gates). Each V-level has corresponding ceremonies.

---

## 1. Requirements review

**Intent:** **C1** + **C2**.

| | |
|--|--|
| **Inputs** | Draft requirements, stakeholder needs, constraints, regulatory obligations |
| **Outputs** | Approved requirements baseline; acceptance test strategy agreed |
| **Participants** | Systems engineer (**R**), test manager (**R**), sponsor (**R**), PM (**R**) |
| **Timebox** | Half day to 2 days (scales with complexity) |

**Agenda:**

1. Walk through requirements for completeness, testability, and traceability.
2. Identify ambiguities and conflicts.
3. Agree on acceptance criteria and high-level test approach.
4. Baseline the requirements document.

---

## 2. System design review

**Intent:** **C2** + **C4**.

| | |
|--|--|
| **Inputs** | System design document, interface specifications, requirements traceability |
| **Outputs** | Approved design baseline; system test plan inputs |
| **Participants** | Systems engineer (**R**), test manager (**R**), dev team (**R**), PM (**O**) |
| **Timebox** | 2–4 hours |

---

## 3. Detailed design review

**Intent:** **C2** + **C4**.

| | |
|--|--|
| **Inputs** | Module-level design, algorithms, data structures, integration interfaces |
| **Outputs** | Approved detailed design; integration test plan inputs; unit test strategy |
| **Participants** | Dev team (**R**), systems engineer (**R**), test manager (**O**) |
| **Timebox** | 1–2 hours per module group |

---

## 4. Test plan review (per V-level)

**Intent:** **C2** + **C6**.

| | |
|--|--|
| **Inputs** | Test plan for the specific V-level, traceability matrix, test environment plan |
| **Outputs** | Approved test plan; environment readiness criteria |
| **Participants** | Test manager (**R**), IV&V (**R** where applicable), systems engineer (**R**), PM (**O**) |
| **Timebox** | 1–2 hours |

**Prescriptive rule:** Review the **traceability** — every requirement should map to at least one test case. Flag untested requirements explicitly.

---

## 5. Test readiness review (TRR)

**Intent:** **C4** + **C6**.

| | |
|--|--|
| **Inputs** | Test plan, test environment, test data, build under test, entry criteria |
| **Outputs** | Go / hold decision for test execution |
| **Participants** | Test manager (**R**), dev team (**R**), PM (**R**), IV&V (**O**) |
| **Timebox** | 1–2 hours |

---

## 6. Test result review (per V-level)

**Intent:** **C4**.

| | |
|--|--|
| **Inputs** | Test execution results, defect reports, coverage metrics |
| **Outputs** | Pass / fail / conditional pass; defect resolution plan |
| **Participants** | Test manager (**R**), systems engineer (**R**), IV&V (**R** where applicable), PM (**R**) |
| **Timebox** | 1–2 hours |

---

## 7. Acceptance review

**Intent:** **C4** + **C1** (closure).

| | |
|--|--|
| **Inputs** | Acceptance test results, traceability matrix (complete), compliance evidence |
| **Outputs** | Formal acceptance or rejection; deployment authorization |
| **Participants** | Sponsor (**R**, decision), systems engineer (**R**), test manager (**R**), PM (**R**), IV&V (**R** where applicable) |
| **Timebox** | 2–4 hours |

---

## 8. Development sync (during implementation)

**Intent:** **C3**.

| | |
|--|--|
| **Inputs** | Implementation status, integration issues, environment problems |
| **Outputs** | Coordination decisions, blocked items escalated |
| **Participants** | Dev team (**R**), systems engineer (**O**), PM (**O**) |
| **Timebox** | 15–30 min (daily or as needed) |

---

## 9. Quick I/O summary

| Ceremony | Primary output |
|----------|----------------|
| Requirements review | Approved requirements baseline |
| System design review | Approved design baseline |
| Detailed design review | Approved module designs |
| Test plan review | Approved test plans with traceability |
| TRR | Go / hold for testing |
| Test result review | Pass / fail with defect plan |
| Acceptance review | Formal acceptance; deployment authorization |
| Dev sync | Coordination, unblocked items |

## 10. Links

- [Process maps](process-and-flows.md) · [Foundation](foundation-connection.md)
