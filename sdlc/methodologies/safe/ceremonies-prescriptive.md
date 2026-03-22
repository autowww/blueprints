# SAFe — ceremonies (prescriptive)

**Purpose:** Prescriptive detail for each SAFe event: **inputs**, **outputs**, **participants**, **timebox**, and **agenda sketch**. Covers both **team-level** and **program-level** events.

**Foundation intents:** [`../ceremonies/ceremony-foundation.md`](../ceremonies/ceremony-foundation.md) (C1–C6). **SAFe fork:** [`../ceremonies/safe.md`](../ceremonies/safe.md).

---

## Program-level events

### PI Planning

| Aspect | Detail |
|--------|--------|
| **Intents** | **C1 Align** (primary), **C2 Commit** |
| **Timebox** | 2 days (face-to-face or virtual); repeated every PI (8–12 weeks) |
| **Participants** | All ART members (all teams), RTE (facilitates), Product Management (vision), System Architect (architecture), Business Owners (business value) |
| **Inputs** | Top 10 features (prioritized program backlog), vision, architecture briefing, iteration calendar, prior PI metrics |
| **Outputs** | Team PI Objectives (committed + stretch), program board (features × iterations × dependencies), ART PI Objectives, ROAM'd risks |

**Agenda sketch (Day 1):**

1. Business context — senior leadership or Product Management
2. Product / solution vision — Product Management
3. Architecture vision and enablers — System Architect
4. Planning context and process — RTE
5. Team breakout #1 — teams draft plans, identify dependencies
6. Draft plan review — teams present, dependencies identified on program board

**Agenda sketch (Day 2):**

1. Planning adjustments — address overnight feedback
2. Team breakout #2 — finalize plans, resolve dependencies
3. Final plan review and program board walkthrough
4. PI Objectives — teams present committed and stretch objectives
5. Business value assignment — Business Owners assign value to each team's objectives
6. Confidence vote — all ART members; revote if < 3/5 average
7. PI Planning retrospective and moving forward — RTE facilitates

### System Demo

| Aspect | Detail |
|--------|--------|
| **Intents** | **C4 Inspect** (primary), **C6 Knowledge share** |
| **Timebox** | 1–2 hours; every iteration (typically every 2 weeks) |
| **Participants** | RTE (facilitates), Product Management (accepts features), System Architect, Business Owners, team representatives (demo), other stakeholders |
| **Inputs** | Integrated increment from all teams; iteration review outcomes; acceptance criteria for features |
| **Outputs** | Accepted/rejected features; stakeholder feedback; updated program backlog |

**Agenda sketch:**

1. Context — RTE: iteration goals, what was planned
2. Integrated demo — team representatives show working software end-to-end
3. Feature acceptance — Product Management and Business Owners evaluate against criteria
4. Feedback capture — open discussion, new ideas, concerns
5. Wrap-up — RTE summarizes outcomes and next steps

### Inspect & Adapt (I&A)

| Aspect | Detail |
|--------|--------|
| **Intents** | **C4 Inspect**, **C5 Improve** |
| **Timebox** | 3–4 hours; end of every PI |
| **Participants** | All ART members, RTE (facilitates), Product Management, System Architect, Business Owners |
| **Inputs** | PI metrics (velocity, quality, PI Objective achievement), System Demo results, team retrospective themes |
| **Outputs** | Improvement backlog items (top items flow into next PI), root cause analysis, quantitative baseline update |

**Agenda sketch:**

1. PI System Demo — final integrated demo for the PI (if not done separately)
2. Quantitative review — RTE presents metrics: PI predictability, velocity trends, defect trends, cycle time
3. Qualitative review — retrospective: what went well, what didn't, across the ART
4. Problem-solving workshop — identify top problem; root-cause analysis (fishbone, 5 Whys); define improvement stories
5. Improvement backlog — vote on top items; assign to next PI backlog

### ART Sync

| Aspect | Detail |
|--------|--------|
| **Intents** | **C3 Sync** |
| **Timebox** | 30–60 minutes; weekly or bi-weekly |
| **Participants** | RTE (facilitates), Scrum Masters (or delegates from each team), Product Owners, System Architect |
| **Inputs** | Team progress, impediments, dependency status from program board |
| **Outputs** | Updated risk/dependency status, escalated impediments, coordination decisions |

Typically combines **Scrum of Scrums** (SM-focused: impediments, dependencies) and **PO Sync** (PO-focused: scope, priorities, feature progress). Can be combined or separate depending on ART size.

---

## Team-level events

Team-level events are identical to Scrum events — see [`../scrum/ceremonies-prescriptive.md`](../scrum/ceremonies-prescriptive.md) for full detail. Summary below for SAFe-specific context.

### Iteration Planning

| Aspect | Detail |
|--------|--------|
| **Intents** | **C2 Commit** → **C1 Align** |
| **Timebox** | 2–4 hours per iteration |
| **Participants** | PO (facilitates), SM, Developers |
| **SAFe context** | Stories selected should advance **PI Objectives**; iteration goals align with the PI plan |

### Daily Stand-up

| Aspect | Detail |
|--------|--------|
| **Intents** | **C3 Sync** |
| **Timebox** | 15 minutes |
| **SAFe context** | Surface cross-team blockers for escalation to ART Sync |

### Iteration Review

| Aspect | Detail |
|--------|--------|
| **Intents** | **C4 Inspect** |
| **Timebox** | 1 hour |
| **SAFe context** | Team-level demo feeds into the **System Demo**; Product Management may attend to preview feature progress |

### Iteration Retrospective

| Aspect | Detail |
|--------|--------|
| **Intents** | **C5 Improve** |
| **Timebox** | 1 hour |
| **SAFe context** | Team-level improvements; themes that affect the ART are escalated to **I&A** |

---

## Large Solution events (when applicable)

| Event | Timebox | Intents | Purpose |
|-------|---------|---------|---------|
| **Pre-PI Planning** | 1 day (before PI Planning) | C1 Align | Align multiple ARTs on solution context, shared objectives, and key milestones |
| **Post-PI Planning** | 1 day (after PI Planning) | C2 Commit | Integrate PI plans across ARTs; resolve cross-ART dependencies |
| **Solution Demo** | 2–4 hours (per PI or per iteration) | C4 Inspect | Demonstrate integrated capabilities across multiple ARTs |

---

## References

- [`../ceremonies/safe.md`](../ceremonies/safe.md) — intent mapping table
- [`../ceremonies/ceremony-foundation.md`](../ceremonies/ceremony-foundation.md) — C1–C6 intents
- [`../safe.md`](../safe.md) — SAFe methodology summary
- [`roles.md`](roles.md) — event participation matrix
