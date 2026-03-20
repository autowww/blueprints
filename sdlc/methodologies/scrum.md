# Scrum

## What it is

**Scrum** is a lightweight framework for developing, delivering, and sustaining **complex products** through **empirical process control**: transparency, inspection, and adaptation. Work is done in **time-boxed Sprints** by a small, cross-functional team with clear **accountabilities** (Product Owner, Scrum Master, Developers).

It is **not** a methodology for every context (e.g. pure ticket-driven ops may fit Kanban better). It **is** a strong default when you want **predictable cadence**, shared commitment to a Sprint Goal, and regular stakeholder feedback.

## Process diagram (handbook)

The human handbook ([`methodologies-scrum.html`](../docs/methodologies-scrum.html)) includes a **Sprint event chain** figure. Same asset:

![Scrum — one Sprint (time-box)](../docs/assets/methodology-scrum-sprint.svg)

*Product Backlog → Sprint Planning → build increment (with Daily Scrums) → Sprint Review → Sprint Retrospective. The Scrum Guide defines official names, time-boxes, and commitments.*

---

## Authoritative sources (external)

| Resource | Executive summary (why it’s linked here) |
|----------|------------------------------------------|
| [**The Scrum Guide**](https://scrumguides.org/scrum-guide.html) | **Official** definition of Scrum—roles, events, artifacts—the authority for mapping this blueprint’s Phases A–F to Scrum. |
| [Scrum.org — What is Scrum?](https://www.scrum.org/resources/what-is-scrum) | Training org’s **intro** and learning paths—complements the Guide, not a second standard. |
| [Agile Alliance — Scrum](https://www.agilealliance.org/glossary/scrum/) | Short **glossary** entry + community context—shared vocabulary alongside the Guide. |

**Trademark:** “Scrum” and related marks belong to their holders; this document summarizes concepts for adoption alongside this blueprint, not for certification prep.

---

## Core structure (summary)

### Accountabilities (2020 Scrum Guide)

| Accountability | Essence |
|----------------|---------|
| **Product Owner** | Maximizes product value from the work; owns ordering of the **Product Backlog**. |
| **Scrum Master** | Establishes Scrum as defined; removes impediments; serves the team and org. |
| **Developers** | Create the Sprint increment; own the **Sprint Backlog** and quality. |

**Cross-reference:** methodology-neutral **delivery archetypes** and how PO / Scrum Master / Developers sit on them — [`roles-archetypes.md`](roles-archetypes.md).

### Events (time-boxed)

| Event | Purpose |
|-------|---------|
| **Sprint** | Container for all other events; fixed length (≤ one month); produces a **Done**, usable **Increment**. |
| **Sprint Planning** | Why is this Sprint valuable? What can be Done? How will work be accomplished? |
| **Daily Scrum** | Inspect progress toward Sprint Goal; adapt Sprint Backlog. |
| **Sprint Review** | Inspect outcome, future adapt; stakeholders collaborate. |
| **Sprint Retrospective** | Inspect how people, relationships, process, tools; improvement plan. |

### Artifacts + commitments

| Artifact | Commitment |
|----------|------------|
| **Product Backlog** | **Product Goal** |
| **Sprint Backlog** | **Sprint Goal** |
| **Increment** | **Definition of Done** |

---

## Mapping to this blueprint’s SDLC

[`SDLC.md`](../SDLC.md) uses **Phases A–F** (discover → release). Scrum does **not** replace those phases; it **wraps** delivery cadence **inside** build and ship:

| Scrum idea | Blueprint touchpoint |
|------------|---------------------|
| Product Backlog / ordering | Phase A–B: backlog, specs, WBS or equivalent in `docs/requirements/`. |
| Sprint Goal + forecast | Phase B–D: what “done” means for the increment aligns with **Definition of Done** ([`dod.html`](../docs/dod.html) in handbook). |
| Increment quality | Phase D–E: CI, tests, review — see [`cicd.html`](../docs/cicd.html) / project CI docs. |
| Release | Phase F: shipping the increment; may be every Sprint or less often depending on product. |

If your repo uses **milestone → epic → story** specs, a **Sprint** often pulls from one or more **stories** that are `ready` per Phase B exit criteria.

---

## Agentic SDLC: Scrum + agents + tracking

**Agentic** here means humans steer while **tools and AI agents** assist (code generation, analysis, test scaffolding, doc drafts). Scrum still applies to **human** commitments and **team** ceremonies; agents are **enablers**, not Product Owners.

| Topic | Guidance |
|-------|----------|
| **Sprint Planning** | Capacity is **human** (availability, focus). Do not treat raw agent output as “free” capacity — review and integration still cost people. |
| **Daily Scrum** | “Yesterday / today / blockers” can reference **PRs**, **CI**, and **agent tasks** as facts; outcomes stay human-owned. |
| **Definition of Done** | Add explicit gates if agents touch code: e.g. human review, tests green, security scan — see project CI policy. |
| **Tracking foundation** | Repos that add [`sdlc/TRACKING-FOUNDATION.md`](../../../sdlc/TRACKING-FOUNDATION.md) model **contributor → events → work units**. Scrum ceremonies consume **aggregates** (e.g. work completed per Sprint); **story points / hours** for planning usually live in the **ALM tool**, not in git alone. |
| **Sprint Review** | Demo **working software**; agent-assisted features are fine if they meet DoD and product intent. |

**Caution:** High agent throughput can **compress cycle time** and create **review bottlenecks** — address in **Retrospective** (WIP on review, pairing, smaller slices).

---

## Ceremonies — inputs that git cannot replace

| Ceremony | What git-based tracking approximates | What you still need |
|----------|----------------------------------------|---------------------|
| Planning | Recent activity, linked commits | Sprint Goal, PO ordering, capacity |
| Daily | Activity per person | Verbal blockers, coordination |
| Review | Merged work, increment | Stakeholder feedback, acceptance |
| Retro | Throughput themes (weak) | Psychological safety, process changes |

See project [`TRACKING-CHALLENGES.md`](../../../sdlc/TRACKING-CHALLENGES.md) for limits of commit-based metrics.

---

## Further reading

- [Scrum Guide — History](https://scrumguides.org/) — **Official site** for guide versions and history (not the Guide text itself).  
- [Agile Manifesto](https://agilemanifesto.org/) — **Values** that Scrum aligns with; not a Scrum process.  
- Companion blueprint guides: [Kanban](kanban.md), [XP](xp.md), [Agentic SDLC](agentic-sdlc.md)
