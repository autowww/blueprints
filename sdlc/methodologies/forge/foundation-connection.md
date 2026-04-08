---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Forge — connection to the SDLC foundation

This blueprint treats **Forge as a delivery methodology** that plugs into a **shared foundation**: **tracking** (spine + artifacts) and **ceremony intents** (C1–C6). Forge does **not** replace the foundation; it defines **how** the team refines, scrutinizes, executes, and releases work.

The **ceremony** names below refer to the same **meetings** listed in [`ceremonies-prescriptive.md`](ceremonies-prescriptive.md); **meeting** is the preferred public label when the distinction matters—see [Meetings vs ceremonies vs Versona sessions](NAMING-REFERENCE.md#meetings-vs-ceremonies-vs-versona-sessions).

## 1. SDLC phases A–F (how Forge maps)

| Phase | Forge expression | Notes |
|-------|------------------|-------|
| **A — Discover** | Ore intake; `discover:` Sparks | New ideas, problems, and opportunities enter the backlog as Ore |
| **B — Specify** | Ore → Ingot refinement; `specify:` Sparks | Ingots answer: what, why, constraints, evidence of done |
| **C — Design** | Ingot decomposition into Sparks; `design:` Sparks | Architecture, ADRs, technical planning |
| **D — Build** | Charge execution; `build:` Sparks | Daily work toward the iteration increment |
| **E — Verify** | Assay Gate; `verify:` Sparks | Evidence gathering: tests, reviews, acceptance |
| **F — Release** | Assay Gate pass → release; `release:` Sparks | Ship when evidence is sufficient; learning feeds new Ore |

**Prescriptive rule:** A Forge iteration should touch **A through F** but not necessarily in sequence. Sparks from different phases coexist in a single Charge. Phase A (Ore intake) and F (learning) are continuous.

## 2. Tracking spine (mandatory link)

Forge teams **still** maintain the blueprint tracking spine:

| Artifact | Forge mapping |
|----------|---------------|
| **Intent / request** | Ore — raw, unrefined input from any source |
| **Spec** | Ingot — refined work with acceptance criteria; may link to ADR/spec docs |
| **Plan** | Sparks decomposed from Ingots; Charge is the daily plan |
| **Tasks** | Sparks (the finest executable grain — same hierarchy level, richer contract) |
| **PRs** | Implementation slices for `build:` and `verify:` Sparks |
| **Reviews** | Versona sessions + peer review + Assay Gate evidence |
| **Release** | Assay Gate pass; ship decision based on evidence |
| **Exploration spike (discipline)** | Versona session + `outputs/SPIKE-CLOSE.md` under `forge-logs/versona/`; may link to Ore/WBS when stable — see [`versona/DISCIPLINE-SPIKE.md`](versona/DISCIPLINE-SPIKE.md) |

**Prescriptive rule:** Every Spark that ships should be **linkable** to its parent Ingot and the original Ore. The Ember Log captures decision context that links and commits alone cannot convey.

## 3. Ceremony intents (C1–C6) ↔ Forge meetings

| Intent | Primary Forge meeting | Secondary |
|--------|------------------------|-----------|
| **C1 — Align & decide** | Refinement (Ore → Ingot), Versona session | Stakeholder sessions, hat-switching declarations |
| **C2 — Plan the slice** | Planning (Ingot → Sparks), Charge selection | Iteration scope negotiation |
| **C3 — Execute & unblock** | Daily sync (Charge confirmation) | Ad-hoc pairing, Versonas for blocked Sparks |
| **C4 — Review & quality** | Review (evidence assessment) | Versona sessions at decision points |
| **C5 — Reflect & improve** | Retro (learning → new Ore) | Ember Log review, Versona reliability assessment |
| **C6 — Assure / release** | Assay Gate (evidence-based release decision) | Continuous via quality gates in CI |

See [ceremony foundation](../ceremonies/ceremony-foundation.md) and [methodology bridge](../ceremonies/methodology-bridge.md).

## 4. Role archetypes (blueprint hats on a Forge team)

| Forge hat | Typical archetype emphasis | Notes |
|-----------|----------------------------|-------|
| **Product** | **Sponsor proxy** + **Orchestrator** (prioritization) | Owns Ore intake and Ingot acceptance; decides value |
| **Engineering** | **Implementer** (primary) + **Quality advocate** | Builds Sparks; owns technical quality and DoD |
| **Challenge** | **Quality advocate** (cross-cutting) | Discipline Versonas (virtual personas) + human critique; surfaces blind spots |
| **Governance** | **Orchestrator** (process) + **Quality advocate** (compliance) | Assay Gate steward; release evidence; Ember Log discipline |

Detail: [roles-archetypes.md](../roles-archetypes.md), [Forge roles chapter](roles.md).

## 5. What Forge adds beyond the foundation

- **Work state precision:** Ore → Ingot → Spark → Charge (not just "to do / doing / done").
- **Explicit discipline lenses:** Discipline Versonas linked to discipline knowledge bases and bridge documents.
- **Decision memory:** Ember Log captures *why* at decision points.
- **Strategic pause:** Banked vs Blocked distinction prevents hidden prioritization.
- **Evidence-based release:** Assay Gate with per-work-type evidence requirements.
- **Hat-switching protocol:** Explicit role transitions for solo and small teams.
- **Phase-tagged Sparks:** `discover:`, `specify:`, `design:`, `build:`, `verify:`, `release:` prefix convention.

## 6. Anti-patterns (prescriptive "don't")

| Anti-pattern | Fix |
|--------------|-----|
| Committing Ore directly to execution | Enforce refinement: Ore must become Ingot before planning |
| Sparks too large (multi-day) | Split: a Spark should complete in one focused session (1–4 hours) |
| Versonas as bureaucracy (invoke on everything) | Time-box Versona; use at decision points, not on routine work |
| Ember Log as status report | Keep it concise: decisions, trade-offs, assumptions — not narration |
| Skipping Assay Gate under schedule pressure | Assay Gate is non-negotiable; adjust scope, not evidence standards |
| Hiding prioritization as "blocked" | Use Banked for strategic pause; Blocked is for external impediments only |
| Duplicating the WBS with Forge IDs | Spark IDs inherit from existing Task IDs — one hierarchy, one namespace |
| Adding ceremony for levels that already fit | If Stories already have acceptance criteria, they are Ingots — skip the extra step |
| Creating a separate Charge board | Charge is a view (label/filter) on the existing backlog, not a new surface |
| Manual journal entry for every field | Automate from git + Cursor tracking; contributor confirms hat and DoD only |

## 7. References in-repo

- [`https://forgesdlc.com/methodology-overview.html`](https://forgesdlc.com/methodology-overview.html) — methodology summary + diagram
- [`../ceremonies/forge.md`](../ceremonies/forge.md) — fork table C1–C6
- [`../../SDLC.md`](../../SDLC.md) — phases and ceremony-intent overview
- [`versona/README.md`](versona/README.md) — discipline Versonas (virtual personas)
