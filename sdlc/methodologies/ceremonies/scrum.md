# Scrum ceremonies → ceremony foundation

**Purpose:** Map **Scrum events** (Scrum Guide) to methodology-neutral **intent types** in [`ceremony-foundation.md`](ceremony-foundation.md).

**Canonical Scrum narrative:** [`../scrum.md`](../scrum.md) · [**The Scrum Guide**](https://scrumguides.org/scrum-guide.html)

---

## Events × intent types

Official **events** are **time-boxed**; all occur **within a Sprint**.

| Scrum event | Foundation intents (primary → secondary) | Notes |
|-------------|------------------------------------------|--------|
| **Sprint Planning** | **C2 Commit** → **C1 Align** | Forecast + Sprint Goal + how to deliver; selects Sprint Backlog. |
| **Daily Scrum** | **C3 Sync** | Inspect progress toward Sprint Goal; adapt Sprint Backlog; 15-minute time-box for Developers (SM facilitates if needed). |
| **Sprint Review** | **C4 Inspect** → **C1 Align** | Stakeholders on increment; informs future Product Backlog (adaptation). |
| **Sprint Retrospective** | **C5 Improve** | Team process, interactions, Definition of Done evolution—not backlog ordering. |
| **Sprint** (container) | *(hosts all above)* | Produces **Done** increment; enables **C6** continuously via **Definition of Done** and integration. |

**C6 Assure / release** is **continuous** in Scrum via the **Definition of Done** and **increment** quality; **formal release** (Phase F) may still be a separate **org** ritual—see project release docs.

---

## What git-based tracking approximates vs what ceremonies need

| Event | Git / commits approximate | You still need (ALM / human) |
|-------|---------------------------|-------------------------------|
| Planning | Recent activity, linked work units | Sprint Goal, PO ordering, **capacity** |
| Daily | Activity per contributor | Verbal/async **blockers**, coordination |
| Review | Merged work | **Stakeholder feedback**, acceptance |
| Retro | Throughput themes (weak) | **Psychological safety**, agreed experiments |

See project [`TRACKING-CHALLENGES.md`](../../../../sdlc/TRACKING-CHALLENGES.md).

---

## Agentic note

Human **accountability** for commitments and acceptance stays with [**roles**](../roles-archetypes.md); agents assist execution. Planning and Review still need **human** intent and **DoD** ownership—[`../agentic-sdlc.md`](../agentic-sdlc.md).
