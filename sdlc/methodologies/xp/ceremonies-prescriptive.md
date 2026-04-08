---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# XP — ceremonies & rhythm (prescriptive)

XP is often run in **iterations** (1–3 weeks). Below: common events; combine with engineering practices (TDD, CI, pair programming).

---

## 1. Release planning

**Intent:** **C1** — themes, scope, rough horizon.

| | |
|--|--|
| **Inputs** | User stories backlog, velocity history (if tracked), business goals |
| **Outputs** | **Release plan** / ordered themes; identified risky stories |
| **Participants** | Customer (**R**), developers (**R**), coach (**R**) |
| **Timebox** | Hours to 1–2 days depending on product size |

**Agenda:**

1. Customer presents priorities and constraints.  
2. Team estimates (e.g. story points or ideal days) — **planning game** rules: customer prioritizes, team estimates.  
3. Cut line for release candidate scope; mark spikes.

---

## 2. Iteration planning

**Intent:** **C2**.

| | |
|--|--|
| **Inputs** | Freshly ordered stories, team capacity |
| **Outputs** | **Iteration backlog**; tasks; acceptance tests identified |
| **Participants** | Customer (**R**), developers (**R**), coach (**O**) |
| **Timebox** | ~half day per 1-week iteration (scale) |

**Agenda:**

1. Customer selects stories for iteration capacity.  
2. Break into **engineering tasks**; identify pairs.  
3. Write / review **acceptance tests** for each story (outline minimum).

---

## 3. Daily stand-up (optional but common)

**Intent:** **C3**.

| | |
|--|--|
| **Inputs** | Iteration board |
| **Outputs** | Coordination; blocks surfaced |
| **Participants** | Developers (**R**); customer/coach (**O**) |
| **Timebox** | 15 min |

XP teams sometimes **skip** formal stand-up when pairing provides continuous sync — policy decision.

---

## 4. Move stories to acceptance (ongoing)

**Intent:** **C4**.

| | |
|--|--|
| **Inputs** | Implemented story, automated tests green |
| **Outputs** | Customer **accepts** or requests changes |
| **Participants** | Customer (**R**), pair that implemented (**R**) |

**Prescriptive rule:** **Definition of Done** includes tests agreed with customer.

---

## 5. Iteration demo / review

**Intent:** **C4** + **C6**.

| | |
|--|--|
| **Inputs** | Accepted stories, deployed or demo environment |
| **Outputs** | Feedback; updated backlog |
| **Participants** | Customer (**R**), team (**R**) |
| **Timebox** | 30–60 min |

---

## 6. Retrospective

**Intent:** **C5**.

| | |
|--|--|
| **Inputs** | Iteration incidents, practice adherence (pairing, CI) |
| **Outputs** | 1–3 **practice** experiments |
| **Participants** | Team (**R**); coach facilitates (**R**); customer (**O**) |
| **Timebox** | 1–2 hours |

---

## 7. Engineering practices (not “meetings” but scheduled discipline)

| Practice | Prescriptive cadence |
|----------|----------------------|
| **Pair programming** | Default for production code; solo by exception |
| **TDD** | Red-green-refactor; tests before merge |
| **Continuous integration** | Trunk/main stays green; integrate multiple times daily |
| **Refactoring** | Ongoing; budget in iteration |
| **Collective ownership** | Anyone improves any module per standards |

---

## 8. Quick I/O summary

| Event | Outputs |
|-------|---------|
| Release plan | Horizon + priorities |
| Iteration plan | Tasks + tests planned |
| Stand-up | Sync |
| Acceptance | Customer sign-off per story |
| Retro | Practice improvements |

## 9. Links

- [Process maps](process-and-flows.md) · [Foundation](foundation-connection.md)
