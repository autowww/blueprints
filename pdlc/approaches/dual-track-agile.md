# Dual-Track Agile

## What it is

**Dual-Track Agile** is a product development approach that runs two parallel workstreams:

- **Discovery track** — validates customer problems and solution ideas to reduce uncertainty before committing engineering capacity
- **Delivery track** — builds and releases validated ideas as production software (via SDLC phases A–F)

The two tracks operate with **different cadences**, **different outputs**, and **different success criteria**, but they are tightly synchronized. Discovery is **continuous** — not a phase that finishes before delivery starts.

The approach emerged in the late 2000s because traditional Agile teams often delivered on time but built the wrong things. The root cause: weak or absent discovery. Dual-Track addresses this by making discovery a **first-class, ongoing activity** rather than an upfront phase.

---

## Authoritative sources (external)

| Resource | Executive summary (why it's linked here) |
|----------|------------------------------------------|
| [Teresa Torres — Continuous Discovery Habits](https://www.producttalk.org/2021/08/continuous-discovery-habits/) | **Practical framework** for operationalizing the discovery track: weekly touchpoints, opportunity solution trees, assumption testing. The most influential modern codification of dual-track practice. |
| [Marty Cagan — Dual-Track Agile (SVPG)](https://www.svpg.com/dual-track-agile/) | **Origin framing** from Silicon Valley Product Group: why discovery and delivery must run in parallel, and why the product trio (PM + Designer + Engineer) co-owns discovery. |
| [Jeff Patton — Dual Track Development](https://www.jpattonassociates.com/dual-track-development/) | **Practical guidance** on separating learning work from building work while keeping them synchronized — includes visual models. |

---

## Core structure

### The two tracks

| Aspect | Discovery track | Delivery track |
|--------|----------------|----------------|
| **Purpose** | Reduce **uncertainty**: Is the problem real? Does the solution work? | Reduce **risk**: Can we build it correctly, reliably, on time? |
| **Led by** | Product trio (PM + Designer + Tech Lead) | Full engineering team (Owner + Implementers per [`SDLC.md`](../../sdlc/SDLC.md)) |
| **Cadence** | Continuous; weekly experiments and interviews | Sprint / iteration / flow (per chosen methodology) |
| **Output** | Validated hypotheses, prototypes, experiment results | Shippable software increments |
| **Success metric** | Evidence quality: did we learn something actionable? | Delivery quality: did we ship correctly? |
| **Artifact** | Experiment log, opportunity tree, research synthesis | Code, tests, release notes, backlog status |
| **PDLC phase** | P1 Discover Problem, P2 Validate Solution | SDLC A–F (inside PDLC) |

### How the tracks synchronize

```blueprint-diagram
key: swimlane
alt: Diagram
```

**Sync points:**
- **Backlog handoff:** Validated ideas from discovery become **ready** backlog items in delivery (SDLC Phase A → B)
- **Sprint/iteration review (C4 Inspect):** Product trio reviews delivered work against original discovery hypotheses
- **Feedback loop:** Post-launch usage data (P5 Grow) feeds back into the discovery track as new evidence

### The product trio

The **product trio** — PM, Designer, and Tech Lead — co-owns the discovery track. Each brings a different risk lens:

| Role | Risk lens | Contribution to discovery |
|------|-----------|--------------------------|
| **PM** | Viability (will the business benefit?) | Frames opportunities, defines success metrics, prioritizes experiments |
| **Designer** | Usability + Desirability (will users want and use it?) | Designs prototypes, runs usability tests, synthesizes research |
| **Tech Lead** | Feasibility (can we build it?) | Assesses technical risk, identifies constraints, runs feasibility spikes |

---

## Mapping to PDLC phases

| PDLC phase | Dual-Track role |
|------------|----------------|
| **P1 Discover Problem** | Discovery track: user interviews, data analysis, opportunity identification |
| **P2 Validate Solution** | Discovery track: prototyping, usability testing, feasibility spikes, experiments |
| **P3 Strategize** | Product trio: vision, OKRs, roadmap based on discovery evidence |
| **SDLC A–F** | Delivery track: build validated ideas |
| **P4 Launch** | Both tracks: discovery measures launch impact; delivery handles rollout |
| **P5 Grow** | Discovery track: continuous — usage data feeds new discovery cycles |

**Key insight:** In Dual-Track, P1–P2 are not "phases" that finish. They are **continuous activities** running alongside delivery. The discovery track is always 1–2 cycles ahead of the delivery track.

## Mapping to SDLC ceremonies (C1–C6)

| SDLC ceremony intent | Dual-Track integration |
|---------------------|------------------------|
| **C1 Align** | Sprint/iteration goal includes both discovery and delivery objectives |
| **C2 Commit** | Delivery commits to building validated items; discovery commits to next experiments |
| **C3 Sync** | Daily/weekly sync surfaces blockers in both tracks; discovery shares insights |
| **C4 Inspect** | Review covers delivered work **and** discovery findings; stakeholders see both |
| **C5 Improve** | Retro examines discovery-delivery handoff quality alongside process |
| **C6 Assure** | DoD includes validation evidence, not just technical completeness |

---

## Anti-patterns

| Anti-pattern | Fix |
|-------------|-----|
| **Discovery as a separate team** | The product trio leads discovery, but uses the **same** engineering team — not a separate "research team" that throws specs over the wall. |
| **Discovery before delivery (waterfall discovery)** | Discovery runs **continuously in parallel** with delivery, not as a preceding phase. The team always has validated work ready while discovering the next thing. |
| **Tech Lead absent from discovery** | Tech Lead must attend user interviews and contribute feasibility assessments. Without them, discovery produces infeasible solutions. |
| **No evidence threshold** | Define what "validated" means before an idea enters the delivery backlog: number of interviews, usability test completion rate, feasibility spike result. |

---

## Further reading

- [Continuous Discovery Habits — Teresa Torres](https://www.producttalk.org/) — Book and blog with detailed frameworks
- [SVPG — Product Discovery](https://www.svpg.com/product-discovery/) — Marty Cagan's collection on discovery practices
- [Opportunity Solution Trees](opportunity-solution-trees.md) — Visual framework for structuring discovery (companion guide)
- [PDLC-SDLC Bridge](../PDLC-SDLC-BRIDGE.md) — How the two tracks map to the full lifecycle
