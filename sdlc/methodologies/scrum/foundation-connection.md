# Scrum — connection to the SDLC foundation

This blueprint treats **Scrum as a delivery methodology** that plugs into a **shared foundation**: **tracking** (spine + artifacts) and **ceremony intents** (C1–C6). Scrum does **not** replace the foundation; it defines **how** the team timeboxes work and who facilitates.

## 1. SDLC phases A–F (how Scrum maps)

| Phase | Scrum expression | Notes |
|-------|------------------|-------|
| **A — Shape** | Product Backlog ordering, stakeholder input, vision | PO leads; Developers may join discovery |
| **B — Plan** | Sprint Planning (part 1: *what*) | Select Product Backlog items for Sprint Goal |
| **C — Build** | Sprint execution, Daily Scrum | Increment emerges; no scope change that endangers goal without PO agreement |
| **D — Verify** | Sprint Review + Definition of Done | Integrated increment; feedback |
| **E — Release** | Potentially shippable increment; release cadence may differ from sprint | May batch releases; still one increment per sprint |
| **F — Operate & learn** | Sprint Retrospective; operational handoff if applicable | Improve process; feed Product Backlog |

**Prescriptive rule:** Every **Sprint** should touch **B through E** at minimum (plan → build → verify). **A** is continuous (backlog refinement). **F** is every sprint (retro) plus ongoing ops if you ship.

## 2. Tracking spine (mandatory link)

Scrum teams **still** maintain the blueprint tracking spine:

| Artifact | Scrum mapping |
|----------|----------------|
| **Intent / request** | Often becomes Product Backlog item or epic; may start outside Scrum |
| **Spec** | Part of PBI acceptance; may live in ADR/spec doc linked from item |
| **Plan** | Sprint Backlog + Sprint Goal |
| **Tasks** | Sub-tasks on PBIs / technical tasks on board |
| **PRs** | Implementation slices toward Done |
| **Reviews** | Code review + DoD checks |
| **Release** | Ship decision; may align with sprint end or faster |

**Prescriptive rule:** Do not let the Scrum board **replace** traceability. Each PBI that ships should be **linkable** to spec/ADR and PRs in your tool.

## 3. Ceremony intents (C1–C6) ↔ Scrum events

| Intent | Primary Scrum event(s) | Secondary |
|--------|------------------------|-----------|
| **C1 — Align & decide** | Sprint Planning (goal + selection), sometimes backlog refinement | Stakeholder sessions before planning |
| **C2 — Plan the slice** | Sprint Planning (part 2: *how*), refinement | Task breakdown in sprint |
| **C3 — Execute & unblock** | Daily Scrum | Ad-hoc pairing, swarming |
| **C4 — Review & quality** | Sprint Review (stakeholder), implicit in DoD | Code review, test activities |
| **C5 — Reflect & improve** | Sprint Retrospective | Team-led improvement items |
| **C6 — Knowledge share** | Sprint Review (demo), sometimes refinement | Tech talks, documentation |

See [ceremony foundation](../ceremonies/ceremony-foundation.md) and [methodology bridge](../ceremonies/methodology-bridge.md).

## 4. Role archetypes (blueprint hats on a Scrum team)

| Scrum role | Typical archetype emphasis | Notes |
|------------|----------------------------|-------|
| **Product Owner** | **Sponsor proxy** + **Orchestrator** (prioritization) | Accountable for value; not a committee |
| **Scrum Master** | **Orchestrator** (process) + **Quality advocate** (impediments to quality of practice) | Serves the team and org; does not own backlog |
| **Developers** | **Implementer** (primary) + **Quality advocate** (shared) | Cross-functional; shared accountability for increment |

Detail: [roles-archetypes.md](../roles-archetypes.md), [Scrum roles chapter](roles.md).

## 5. What Scrum adds beyond the foundation

- **Timebox:** fixed-length Sprints.
- **Accountabilities:** PO / SM / Developers (three distinct roles).
- **Commitments:** Product Goal, Sprint Goal, Definition of Done (per Scrum Guide 2020).
- **Events:** Sprint, Planning, Daily Scrum, Review, Retrospective.

## 6. Anti-patterns (prescriptive “don’t”)

| Anti-pattern | Fix |
|--------------|-----|
| SM as project admin / note-taker only | SM protects Scrum theory; facilitates events |
| PO as sole “story writer” with no Dev input in refinement | Developers participate in refinement (C2) |
| Skipping retro when “busy” | Retro is non-negotiable for sustainable improvement |
| No increment at end of sprint | Replan; inspect why DoD / slicing failed |

## 7. References in-repo

- [`https://forgesdlc.com/methodology-scrum.html`](https://forgesdlc.com/methodology-scrum.html) — methodology summary + diagram  
- [`../ceremonies/scrum.md`](../ceremonies/scrum.md) — fork table C1–C6  
- [`../../SDLC.md`](../../SDLC.md) — phases and ceremony-intent overview  
