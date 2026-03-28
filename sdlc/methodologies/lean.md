---
slug: methodology-lean
tier: 201
lens: methodology
nav_section: "Methodology Comparisons"
---

# Lean Software Development

## What it is

**Lean Software Development** adapts **Lean manufacturing** principles (Toyota Production System) to software engineering. Mary and Tom Poppendieck formalized **seven principles**: eliminate waste, amplify learning, decide as late as possible, deliver as fast as possible, empower the team, build integrity in, and optimize the whole. Lean is **not** a process framework with named events (like Scrum); it is a **thinking model** that underpins Kanban, SAFe, and many continuous-delivery practices.

Use Lean when you want a **principle-based lens** for improving any existing process—whether Scrum, Kanban, phased, or XP—rather than adopting a new ceremony set.

## Process diagram (handbook)

![Lean principles applied to the value stream](../docs/assets/methodology-lean-stream.svg)

*Identify value → map the value stream → create flow → establish pull → pursue perfection. The inner loop drives continuous improvement (Kaizen).*

---

## Authoritative sources (external)

| Resource | Executive summary (why it's linked here) |
|----------|------------------------------------------|
| [**Wikipedia — Lean software development**](https://en.wikipedia.org/wiki/Lean_software_development) | **Stable overview** of the seven principles, history, and relationship to manufacturing Lean—entry point before the Poppendiecks' books. |
| [Wikipedia — Toyota Production System](https://en.wikipedia.org/wiki/Toyota_Production_System) | **Manufacturing roots**—understanding TPS clarifies why "waste" and "pull" matter in software contexts. |
| [Wikipedia — Lean manufacturing](https://en.wikipedia.org/wiki/Lean_manufacturing) | **Broader** Lean context—five principles (value, value stream, flow, pull, perfection) that the software adaptation draws from. |
| [Agile Alliance — Lean software development](https://www.agilealliance.org/glossary/lean-software-development/) | **Short definition** in the Agile glossary—shared vocabulary. |

**Books:** Mary & Tom Poppendieck, *Lean Software Development: An Agile Toolkit* (2003) and *Implementing Lean Software Development* (2006) are the canonical texts; purchase or library for full narrative.

---

## Seven principles (summary)

| Principle | Meaning in software |
|-----------|---------------------|
| **Eliminate waste** | Remove anything that does not add customer value: unnecessary features, handoffs, waiting, partially done work, task switching, defects. |
| **Amplify learning** | Short feedback loops, experiments, iterations, tests—learning is the product of development. |
| **Decide as late as possible** | Defer irreversible decisions until the **last responsible moment** to preserve options; invest in reversible choices. |
| **Deliver as fast as possible** | Shorter lead times reduce risk, increase feedback, and compress the cost of delay. |
| **Empower the team** | Push decisions to the people with the knowledge; managers set context, not commands. |
| **Build integrity in** | Conceptual integrity (consistent UX/API) and structural integrity (tests, refactoring) from the start—not bolted on later. |
| **Optimize the whole** | Sub-optimizing one phase (e.g. coding speed) at the expense of another (e.g. testing, deployment) increases total waste. |

---

## Lean thinking tools

| Tool | Purpose |
|------|---------|
| **Value-stream mapping** | Visualize the end-to-end flow from idea to production; identify waiting, handoffs, and rework loops. |
| **A3 problem-solving** | Structured single-page analysis: background, current condition, root cause, target, countermeasures, follow-up. |
| **Five Whys** | Iterative root-cause analysis; stop fixing symptoms. |
| **Kaizen events** | Time-boxed improvement sprints focused on one value-stream segment. |
| **Kanban boards** | Visualize WIP and flow; see [`kanban.md`](kanban.md) for the full method. |
| **Set-based design** | Explore multiple solutions in parallel; narrow late based on evidence. |

---

## Mapping to this blueprint's SDLC

| Lean idea | Blueprint touchpoint |
|-----------|----------------------|
| Value stream | Phases A–F end-to-end; waste lives in handoffs **between** phases, not only within one. |
| Pull | Kanban-style WIP limits; demand-driven planning. |
| Build integrity in | Definition of Done ([`dod.html`](../docs/dod.html)), CI quality gates, TDD. |
| Decide late | ADRs ([`docs/adr/`]) capture **durable** decisions; reversible choices stay informal. |
| Optimize the whole | Cross-phase metrics (lead time, cycle time) vs phase-local velocity. |

**Ceremonies:** Lean does not prescribe named ceremonies. It **strengthens** existing ones by asking "does this meeting reduce waste or add it?" See [`ceremonies/lean.md`](ceremonies/lean.md) for intent mapping.

**Roles:** Lean emphasizes **team empowerment** and **manager-as-teacher**; see how this relates to delivery archetypes in [`roles-archetypes.md`](roles-archetypes.md).

---

## Agentic SDLC: Lean + agents + tracking

| Topic | Guidance |
|-------|----------|
| **Eliminate waste** | Agents can automate **non-value-adding** work (boilerplate, formatting, routine tests). Validate that automation **reduces** total lead time, not just coding time. |
| **Amplify learning** | Use agent-generated drafts as **learning accelerators**, not as finished output. Review cycles **are** learning—do not skip them for speed. |
| **Decide late** | Agents can generate **options** (multiple implementations, design alternatives) to support set-based design. |
| **Deliver fast** | Agents compress coding time; ensure **review** and **deployment** keep pace or the bottleneck just shifts. |
| **Optimize the whole** | Measure **end-to-end** lead time (idea → production), not just "time agent spent coding." |

---

## Lean vs other methodologies

| Comparison | Relationship |
|------------|-------------|
| **Lean → Kanban** | Kanban **operationalizes** Lean flow principles with boards, WIP limits, and policies. |
| **Lean → SAFe** | SAFe is built on **Lean-Agile** values; Lean Portfolio Management, flow metrics, and PI cadence are Lean-derived. |
| **Lean → Scrum** | Scrum time-boxes are compatible with Lean; Sprint Reviews and Retros enable **amplify learning** and **Kaizen**. |
| **Lean → XP** | XP practices (TDD, CI, refactoring) directly serve **build integrity in** and **eliminate waste** (defects). |
| **Lean → Phased** | Lean thinking can **diagnose** waste in phased delivery (long gates, handoffs) and motivate hybrid approaches. |

---

## Prescriptive deep dive (teams)

Package **[`lean/README.md`](lean/README.md)** — foundation fit, roles (value-stream manager, team, Lean coach), ceremonies (Kaizen, value-stream review, stand-up, A3), flow maps.

---

## Further reading

- [Lean Enterprise Institute](https://www.lean.org/) — **Practitioner** community; manufacturing and beyond.  
- [Agile Alliance — Lean software development](https://www.agilealliance.org/glossary/lean-software-development/) — **Glossary** entry.  
- Companion: [Kanban](kanban.md), [SAFe](safe.md), [Agile umbrella](agile.md), [Agentic SDLC](agentic-sdlc.md)
