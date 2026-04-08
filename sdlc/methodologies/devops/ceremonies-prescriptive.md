---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# DevOps — ceremonies & rhythm (prescriptive)

DevOps ceremonies complement development-focused events (planning, review, retro) with **operational** ceremonies. Below: common DevOps-specific practices.

---

## 1. Deployment review

**Intent:** **C4** + **C6**.

| | |
|--|--|
| **Inputs** | Deployment plan, change list, rollback procedure, monitoring checklist |
| **Outputs** | Go / no-go for deployment; deployment record |
| **Participants** | Release engineer (**R**), dev team (**R**), SRE (**O**), on-call (**O**) |
| **Timebox** | 15–30 min (pre-deployment); brief for automated deployments |

**Agenda:**

1. Review changes in this deployment.
2. Confirm rollback procedure is tested.
3. Confirm monitoring and alerts are in place for new changes.
4. Go / no-go decision.

For fully automated CD pipelines, this may be a **policy check** rather than a meeting.

---

## 2. Incident response (structured)

**Intent:** **C3** (sync during incident) + **C6** (assure resolution).

| | |
|--|--|
| **Inputs** | Alert, customer report, or automated detection |
| **Outputs** | Incident mitigated/resolved; timeline documented; follow-up actions identified |
| **Participants** | On-call (**R**), incident commander (**R** for major incidents), dev team (**R** for owning service), SRE (**R**) |
| **Timebox** | Until resolved; structured handoffs for long incidents |

**Roles during incident:**

| Role | Responsibility |
|------|----------------|
| **Incident commander** | Coordinates response; manages communication; decides escalation |
| **Technical lead** | Diagnoses and implements fix; delegates investigation |
| **Communications** | Updates stakeholders, status page, customers |

---

## 3. Blameless post-mortem

**Intent:** **C5** + **C6**.

| | |
|--|--|
| **Inputs** | Incident timeline, impact data, root-cause analysis |
| **Outputs** | Post-mortem document; action items with owners and deadlines |
| **Participants** | Incident participants (**R**), SRE (**R**), engineering lead (**O**), affected teams (**O**) |
| **Timebox** | 1–2 hours (within 5 business days of incident) |

**Agenda:**

1. Review timeline (what happened, when, who responded).
2. Identify contributing factors (not "who is to blame").
3. Determine action items to prevent recurrence.
4. Assign owners and review dates for action items.

**Prescriptive rule:** Post-mortems are **blameless**. Focus on **systems and processes**, not individual mistakes. The goal is learning, not punishment.

---

## 4. SLO review

**Intent:** **C4** + **C1**.

| | |
|--|--|
| **Inputs** | SLO dashboards, error budget status, reliability trends |
| **Outputs** | SLO adjustments, reliability investment decisions, error budget policies |
| **Participants** | SRE (**R**), dev team (**R**), product owner (**O**), engineering lead (**O**) |
| **Timebox** | 30–60 min; monthly or quarterly cadence |

**Agenda:**

1. Review SLO performance vs targets.
2. Review error budget consumption.
3. Decide: invest in reliability or features (error budget informs).
4. Adjust SLOs if targets are too tight or too loose.

---

## 5. Pipeline retrospective

**Intent:** **C5**.

| | |
|--|--|
| **Inputs** | DORA metrics (deployment frequency, lead time, change failure rate, MTTR), pipeline incidents |
| **Outputs** | Pipeline improvements prioritized; toil reduction initiatives |
| **Participants** | Platform engineer (**R**), dev team (**R**), release engineer (**R**), SRE (**O**) |
| **Timebox** | 1 hour; monthly or after significant pipeline changes |

---

## 6. On-call handoff

**Intent:** **C3** + **C6**.

| | |
|--|--|
| **Inputs** | Current on-call log, active incidents, known issues, upcoming deployments |
| **Outputs** | Clean handoff; incoming on-call is aware of context |
| **Participants** | Outgoing on-call (**R**), incoming on-call (**R**) |
| **Timebox** | 15–30 min |

---

## 7. Quick I/O summary

| Ceremony | Primary output |
|----------|----------------|
| Deployment review | Go / no-go; deployment record |
| Incident response | Incident resolved; timeline documented |
| Post-mortem | Root-cause analysis; action items |
| SLO review | SLO adjustments; error budget decisions |
| Pipeline retro | Pipeline improvements |
| On-call handoff | Clean context transfer |

## 8. Links

- [Process maps](process-and-flows.md) · [Foundation](foundation-connection.md)
