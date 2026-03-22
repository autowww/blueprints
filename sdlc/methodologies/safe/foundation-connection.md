# SAFe — connection to the SDLC foundation

This blueprint treats **SAFe as a scaled delivery framework** that plugs into a **shared foundation**: **tracking** (spine + artifacts) and **ceremony intents** (C1–C6). SAFe does **not** replace the foundation; it adds **multi-team coordination**, **shared cadence**, and **portfolio governance** on top.

## 1. SDLC phases A–F (how SAFe maps)

| Phase | SAFe expression | Notes |
|-------|-----------------|-------|
| **A — Shape** | Portfolio Kanban, strategic themes, Lean business case, PI roadmap | Product Management + Business Owners drive; System Architect contributes enabler epics |
| **B — Plan** | PI Planning (program-level), Iteration Planning (team-level) | Teams commit to PI Objectives; dependencies surfaced on the program board |
| **C — Build** | Iteration execution, Daily Stand-ups, ART Sync | Each team builds its increment; cross-team integration is continuous |
| **D — Verify** | System Demo (every iteration), Iteration Review | Integrated system demo validates cross-team work; team-level review validates stories |
| **E — Release** | Release on demand; may decouple from PI cadence | Continuous delivery pipeline; release when business value warrants it |
| **F — Operate & learn** | Inspect & Adapt (I&A), Iteration Retrospective, DevOps feedback | I&A drives ART-level improvement; retros drive team improvement |

**Prescriptive rule:** Every **PI** should touch **A through F**. Every **Iteration** within a PI should touch **B through E** at minimum. **A** is continuous (backlog refinement, portfolio Kanban). **F** happens at PI boundaries (I&A) and per iteration (retro).

## 2. Tracking spine (mandatory link)

SAFe teams **still** maintain the blueprint tracking spine:

| Artifact | SAFe mapping |
|----------|--------------|
| **Intent / request** | Epic (business or enabler) in portfolio Kanban; may originate from strategic themes |
| **Spec** | Feature acceptance criteria, enabler descriptions, architectural runway specs |
| **Plan** | PI Objectives + program board (ART level); Sprint Backlog + Sprint Goal (team level) |
| **Tasks** | Stories and sub-tasks on team boards |
| **PRs** | Implementation slices toward iteration increment |
| **Reviews** | Code review + DoD checks (team); System Demo (ART); Solution Demo (large solution) |
| **Release** | Release on demand; continuous delivery pipeline; may align with PI boundary or mid-PI |

**Prescriptive rule:** Do not let the program board **replace** traceability. Each feature that ships should be **linkable** to epic, specs, stories, and PRs in your tools.

## 3. Ceremony intents (C1–C6) ↔ SAFe events

| Intent | Primary SAFe event(s) | Secondary |
|--------|------------------------|-----------|
| **C1 — Align & decide** | PI Planning (vision, context, architecture briefing), portfolio sync | Backlog refinement, strategic theme reviews |
| **C2 — Plan the slice** | PI Planning (team breakouts, draft plans), Iteration Planning | Feature/story breakdown, dependency mapping |
| **C3 — Execute & unblock** | Daily Stand-up, ART Sync (Scrum of Scrums + PO Sync) | Ad-hoc cross-team coordination, Communities of Practice |
| **C4 — Review & quality** | System Demo, Iteration Review, I&A (quantitative review) | Solution Demo, code review activities |
| **C5 — Reflect & improve** | I&A (problem-solving workshop), Iteration Retrospective | ART-level improvement backlog items |
| **C6 — Knowledge share** | System Demo (cross-team learning), Communities of Practice | PI Planning (architecture briefing), I&A (learnings) |

See [ceremony foundation](../ceremonies/ceremony-foundation.md) and [methodology bridge](../ceremonies/methodology-bridge.md).

## 4. Role archetypes (blueprint hats on a SAFe ART)

| SAFe role | Typical archetype emphasis | Notes |
|-----------|----------------------------|-------|
| **Product Management** | **Sponsor proxy** + **Orchestrator** (feature prioritization) | Owns program backlog; not the same as team-level PO |
| **Release Train Engineer** | **Orchestrator** (process at ART level) + **Quality advocate** (flow efficiency) | Servant leader for the ART; facilitates PI-level events |
| **System Architect** | **Implementer** (architectural) + **Quality advocate** (system-level NFRs) | Guides cross-team technical decisions; owns architectural runway |
| **Product Owner** | **Sponsor proxy** (team-level) + **Orchestrator** (story prioritization) | Owns team backlog; collaborates with Product Management |
| **Scrum Master** | **Orchestrator** (process) + **Quality advocate** (impediments) | Serves the team; facilitates team-level events |
| **Developers** | **Implementer** (primary) + **Quality advocate** (shared) | Cross-functional; shared accountability for iteration increment |
| **Business Owners** | **Sponsor** | Accountable for business outcomes; participate in PI Planning and I&A |

Detail: [roles-archetypes.md](../roles-archetypes.md), [SAFe roles chapter](roles.md).

## 5. What SAFe adds beyond the foundation

- **Program Increment (PI):** fixed cadence of 8–12 weeks (typically 5 iterations) aligning multiple teams.
- **Agile Release Train (ART):** long-lived team-of-teams (50–125 people) delivering a shared value stream.
- **PI Planning:** two-day face-to-face (or virtual) event for alignment and commitment across all ART teams.
- **Program Board:** visualizes features, dependencies, and milestones across teams for the PI.
- **Architectural Runway:** intentional infrastructure enabling near-term features without excessive redesign.
- **Lean Portfolio Management:** strategic themes, Lean budgets, portfolio Kanban connecting strategy to execution.
- **Continuous Delivery Pipeline:** from idea to production with built-in quality at every stage.

## 6. Anti-patterns (prescriptive "don't")

| Anti-pattern | Fix |
|--------------|-----|
| RTE as command-and-control project manager | RTE is a servant leader; facilitates, does not dictate team plans |
| PI Planning as a status report to management | PI Planning is collaborative planning *by* teams, not *for* management |
| Skipping System Demo | System Demo is essential for cross-team integration validation; never skip it |
| Teams plan in isolation without dependency mapping | Use the program board; surface and manage dependencies explicitly |
| Treating PI Objectives as contracts | PI Objectives are forecasts with committed and stretch; adjust in I&A |
| Applying SAFe to a single team | Use Scrum, Kanban, or XP instead — SAFe is for multi-team coordination |

## 7. References in-repo

- [`../safe.md`](../safe.md) — methodology summary
- [`../ceremonies/safe.md`](../ceremonies/safe.md) — fork table C1–C6
- [`../../SDLC.md`](../../SDLC.md) — phases and ceremony-intent overview
