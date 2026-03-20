# Scrum — ceremonies & events (prescriptive)

Each **official Scrum event** below lists **inputs**, **outputs**, **participants**, **timebox** (typical), **agenda**, and **meetings** (what to schedule). Unofficial but common: **backlog refinement** — included because teams need it to make Planning workable.

Timeboxes below are **starting points** for a 1-month Sprint; scale down ~proportionally for shorter Sprints (per Scrum Guide).

---

## 0. Ongoing — Product Backlog refinement

**Intent:** Primarily **C2** (plan the slice) + **C1** (align on scope/value).

| | |
|--|--|
| **Inputs** | Product Goal, stakeholder themes, rough estimates, dependencies, risks |
| **Outputs** | PBIs ordered and **ready** for Sprint (clear value, acceptance, sized enough to select) |
| **Participants** | PO (**R**), Developers (**R**), SM (**O** — facilitate if helpful) |
| **Cadence** | Continuous; **aim for ~10% of sprint capacity** on refinement |
| **Meetings** | Recurring **Refinement** slots (e.g. 1–2× per week, 45–60 min) |

**Agenda (single refinement session):**

1. PO presents top of backlog / new items (5–10 min).  
2. Clarify acceptance & value; Developers ask questions (20–30 min).  
3. Split or spike unclear items; capture dependencies (15–20 min).  
4. Re-order if learning changed value (5–10 min).

**Definition of Ready (team working agreement — example):**

- Value statement clear to PO.  
- Acceptance criteria testable.  
- Dependencies identified or spiked.  
- Sized to fit sprint horizon (e.g. ≤ half sprint).

---

## 1. Sprint Planning

**Intent:** **C1** + **C2** — align on what to build this sprint and how to start.

| | |
|--|--|
| **Inputs** | Product Backlog, latest increment, capacity, past performance, Definition of Done |
| **Outputs** | **Sprint Goal**, selected PBIs, initial **Sprint Backlog**, forecast understood by all |
| **Participants** | PO, SM, Developers (**all required**) |
| **Timebox** | ≤ **8 hours** / month-long sprint (scale down) |

**Agenda (two-part structure):**

**Part 1 — Why & what (PO-led, whole team)**

1. PO reminds Product Goal and context.  
2. PO proposes candidate ordering / highest-value items.  
3. Team selects what fits capacity and craft **Sprint Goal** (single coherent objective).  
4. Confirm no hidden dependencies that invalidate selection.

**Part 2 — How (Developer-led)**

1. Break PBIs into Sprint Backlog work items / tasks.  
2. Identify risks, tests, integration points.  
3. Confirm team confidence in meeting Sprint Goal; adjust scope if not.

**Meetings to schedule:** One block or two adjacent blocks on first day of sprint; calendar invite to whole Scrum Team.

---

## 2. Daily Scrum

**Intent:** **C3** — execute & unblock; inspect progress toward Sprint Goal.

| | |
|--|--|
| **Inputs** | Sprint Backlog, Sprint Goal, impediments known |
| **Outputs** | Updated plan for next 24h; surfaced impediments; optional board updates |
| **Participants** | Developers (**required**); SM optional; PO usually absent unless invited |
| **Timebox** | **15 minutes** same time/place daily |

**Agenda (example formats — pick one):**

- **Walk the board:** right-to-left on in-progress items; what’s done, what’s next, blockers.  
- **By person (classic):** what I did, will do, blockers — keep strictly timeboxed.

**After the Daily:** follow-up huddles for specific problem-solving (not part of the 15 min).

**Meetings to schedule:** Recurring daily; video link + physical space; SM ensures timebox.

---

## 3. Sprint Review

**Intent:** **C4** + **C6** — review increment with stakeholders; inspect outcome vs Product Goal.

| | |
|--|--|
| **Inputs** | Done increment, Product Backlog, Sprint Goal, relevant metrics |
| **Outputs** | Stakeholder feedback captured; backlog adjustments; shared understanding of what’s next |
| **Participants** | PO, SM, Developers, **stakeholders invited** |
| **Timebox** | ≤ **4 hours** / month-long sprint |

**Agenda:**

1. PO frames sprint objective and what was forecast vs done (5–10 min).  
2. Developers **demonstrate working increment** (not slides-only) (majority of time).  
3. Stakeholders ask questions; discuss market/user impact (throughout).  
4. PO discusses backlog implications; what likely enters next sprint (10–15 min).  
5. Review timeline / budget / roadmap if relevant (optional segment).

**Meetings to schedule:** End of sprint; invite stakeholders early; share pre-read if metrics are dense.

---

## 4. Sprint Retrospective

**Intent:** **C5** — reflect and improve the system of work.

| | |
|--|--|
| **Inputs** | Sprint events data, quality issues, team mood, previous retro action items |
| **Outputs** | **1–3 committed improvement experiments** with owners and due dates |
| **Participants** | PO, SM, Developers (whole Scrum Team) |
| **Timebox** | ≤ **3 hours** / month-long sprint |

**Agenda (example — rotate formats):**

1. Set stage — safety & focus (5–10 min).  
2. Gather data — what happened this sprint (15–20 min).  
3. Generate insights — patterns, root causes (20–30 min).  
4. Decide experiments — small, measurable changes (20–30 min).  
5. Close — thank you; schedule follow-ups (5 min).

**Meetings to schedule:** After Review, same sprint end window; SM facilitates or rotating facilitator from Developers.

---

## 5. The Sprint (container)

**Intent:** Houses **B–E** phases; produces at most one **Done** increment per sprint.

| | |
|--|--|
| **Inputs** | Sprint Goal, Sprint Backlog, DoD, environments & tools |
| **Outputs** | Potentially releasable increment; transparency on progress |
| **Participants** | Whole Scrum Team |
| **Timebox** | Fixed length (e.g. 1–4 weeks); **no extension** |

**Prescriptive checkpoints (lightweight):**

- Mid-sprint: informal risk check on Sprint Goal (15 min, Developers + PO if scope threat).  
- Pre-Review: “Done?” walkthrough against DoD (Developers).

---

## 6. Quick reference — I/O summary

| Event | Primary inputs | Primary outputs |
|-------|----------------|-----------------|
| Refinement | Themes, rough PBIs | Ready, ordered backlog |
| Sprint Planning | Backlog, capacity, DoD | Sprint Goal, Sprint Backlog |
| Daily Scrum | Board, blockers | 24h plan, visible impediments |
| Sprint Review | Increment, stakeholders | Feedback, backlog updates |
| Sprint Retrospective | Sprint experience | Improvement experiments |

---

## 7. Links

- [Process maps & lifecycle](process-and-flows.md) · [Foundation connection](foundation-connection.md) · [Ceremony fork](../ceremonies/scrum.md)
