# DSDM (Dynamic Systems Development Method)

## What it is

**DSDM** is an Agile project delivery framework that provides **governance and structure** for Agile teams, particularly in environments that also use **PRINCE2** or other project management standards. Originally created in 1994 in the UK, it is now maintained by the **Agile Business Consortium**. DSDM defines a full project lifecycle with phases, roles, and principles — making it one of the few Agile methods that addresses **project governance** explicitly.

DSDM's core principle is that **time and cost are fixed; scope is variable** (the opposite of traditional project management). It uses **MoSCoW prioritization** (Must have, Should have, Could have, Won't have) to manage scope within fixed timeboxes.

## Process diagram (handbook)

![DSDM lifecycle phases](../docs/assets/methodology-dsdm-lifecycle.svg)

*Feasibility → Foundations → Evolutionary Development (iterative) → Deployment. Pre-project and post-project phases bookend the lifecycle.*

---

## Authoritative sources (external)

| Resource | Executive summary (why it's linked here) |
|----------|------------------------------------------|
| [**Wikipedia — Dynamic systems development method**](https://en.wikipedia.org/wiki/Dynamic_systems_development_method) | **Stable overview** of DSDM phases, principles, and roles. |
| [Agile Business Consortium](https://www.agilebusiness.org/) | **Official** DSDM body — framework documentation, training, and certification. |
| [Agile Alliance — DSDM](https://www.agilealliance.org/glossary/dsdm/) | **Short definition** in the Agile glossary. |

---

## Eight principles

| Principle | Meaning |
|-----------|---------|
| **Focus on the business need** | Every decision should be traceable to a business objective. |
| **Deliver on time** | Timeboxing is non-negotiable; scope flexes, not deadlines. |
| **Collaborate** | Active, continuous collaboration between business and technical roles. |
| **Never compromise quality** | Quality is defined early and is not a negotiable variable. |
| **Build incrementally from firm foundations** | Understand the scope before deep build, then evolve incrementally. |
| **Develop iteratively** | Embrace change through iterative refinement; feedback drives convergence. |
| **Communicate continuously and clearly** | Informal and formal communication; daily stand-ups and workshops. |
| **Demonstrate control** | Plans and progress must be visible; governance is not optional. |

---

## Lifecycle phases

| Phase | Purpose |
|-------|---------|
| **Pre-project** | Confirm the project is worth doing; initial business case. |
| **Feasibility** | Assess technical and business feasibility; prove viability. |
| **Foundations** | Establish scope (MoSCoW), architecture, development approach, and team. |
| **Evolutionary Development** | Iterative timeboxes producing increments; the main build phase. |
| **Deployment** | Release to production; user training; handover. |
| **Post-project** | Benefits assessment; lessons learned. |

---

## Mapping to this blueprint's SDLC

| DSDM idea | Blueprint touchpoint |
|-----------|----------------------|
| Pre-project + feasibility | Phase A: discovery, feasibility. |
| Foundations | Phase A–B: scope, architecture, planning. |
| Evolutionary Development | Phase C–D: iterative build and verify. |
| Deployment | Phase E–F: release and operate. |
| MoSCoW prioritization | Backlog management; scope management per [`change.html`](../docs/change.html). |
| Demonstrate control | Governance, tracking, reporting per [`SDLC.md`](../SDLC.md). |

---

## Roles (DSDM-specific)

| Role | Responsibility |
|------|----------------|
| **Business sponsor** | Funding, strategic alignment, removing business-level impediments. |
| **Business visionary** | Defines the business vision; ensures the solution meets business needs. |
| **Technical coordinator** | Technical architecture, standards, quality; equivalent to chief architect. |
| **Team leader** | Facilitates the team; manages timebox execution (similar to Scrum Master). |
| **Business ambassador** | Day-to-day business voice; provides requirements and feedback (similar to Product Owner). |
| **Solution developers** | Build and test the solution within timeboxes. |
| **Solution testers** | Dedicated testing; work within or alongside the development team. |

---

## DSDM + PRINCE2 (common combination)

DSDM provides the **Agile delivery** approach within a **PRINCE2** project management framework. PRINCE2 handles **governance**, **stage gates**, and **exception management**; DSDM handles **iterative development** within stages. This combination is common in UK government and enterprise contexts.

---

## Agentic SDLC: DSDM + agents

| Topic | Guidance |
|-------|----------|
| **Timeboxing** | Agent throughput increases what fits in a timebox; ensure **review and quality** keep pace. |
| **MoSCoW** | Agents can help analyze and prioritize requirements; **business ambassador** makes final MoSCoW decisions. |
| **Governance** | DSDM's explicit governance maps well to agent audit trails; ensure agent-generated changes are traceable. |

---

## Further reading

- [Wikipedia — DSDM](https://en.wikipedia.org/wiki/Dynamic_systems_development_method) — **Overview**.
- [Agile Business Consortium](https://www.agilebusiness.org/) — **Official** framework body.
- Companion: [Phased delivery](phased-delivery.md), [Scrum](scrum.md), [Agile umbrella](agile.md)
