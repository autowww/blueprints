---
product_spark: F1
type: mvp
status: planning
core_value: "Adopters and maintainers share one clear story: what Blueprints is, who it is for, and the first concrete steps after submodule add — backed by roadmap and WBS."
target_date:
---

# MVP plan — Adoption spine v1 (F1)

## Core value proposition

Ship the **minimum narrative + structure** so a team can **understand**, **position**, and **start using** Blueprints without reading the entire tree: positioning one-pager, adoption quickstart, maintainer roadmap, and a small WBS that maintainers can execute.

## Target users

| User | Job-to-be-done |
|------|----------------|
| **New submodule adopter** | “What do I do in the first hour?” |
| **Maintainer** | “What are we shipping next for the framework product?” |
| **Internal champion** | “How do I explain this vs Confluence/SAFe?” |

## Scope boundaries

### Must have (MVP scope)

| Ingot | Value | Acceptance criteria |
|-------|-------|---------------------|
| Positioning doc | Category, ICPs, alternatives, MVP rationale | [`discovery/framework-positioning-and-mvp.md`](../discovery/framework-positioning-and-mvp.md) merged; links from ADOPTION + ROADMAP |
| Adoption quickstart | ICP paths A/B/C | [`../../ADOPTION.md`](../../ADOPTION.md) complete; linked from README |
| Roadmap | NOW/NEXT/LATER + M1 | [`../../ROADMAP.md`](../../ROADMAP.md) reflects F1 and M2 |
| WBS M1 | Executable stories | [`../../requirements/WBS.md`](../../requirements/WBS.md) with owners/estimates where known |

### Should have (first phase after MVP)

- Handbook / **blueprints-website** home CTA to [`ADOPTION.md`](../../ADOPTION.md) (or equivalent on-site copy).
- First **evidence** snippet in positioning doc.

### Won't have (deferred)

- Automated multi-repo scaffold script.
- Changes to frozen `blueprints/sdlc/` baseline text (policy edits are separate governance).
- Revenue, licensing, or partnership deals.

## Forge iterations

| Iteration | Focus | Key Ingots |
|-----------|-------|------------|
| F1 | Docs + alignment | Positioning, ADOPTION, ROADMAP, WBS, README links |

## Assay Gate criteria (MVP exit)

- [ ] All **must have** rows above satisfied in `main`
- [ ] README links to `docs/ROADMAP.md`, `docs/ADOPTION.md`, and positioning doc
- [ ] WBS stories M1E1S1–M1E2S2 marked **done** or explicitly rescheduled with reason
- [ ] PM Versona close recorded (spike `outputs/SPIKE-CLOSE.md`) with **Proceed** or **Proceed with conditions**

## Versona sessions planned

| Discipline | Timing | Focus |
|------------|--------|-------|
| Product Management | Close (done) | Positioning evidence, scope creep vs handbook |
| BA | Optional before baseline | WBS completeness for F1 |

## Risks

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Positioning overclaims vs reality | Med | Reputation | Evidence loop in M2; “draft” status until validated |
| F1 swallowed by site work | Med | Slippage | Park handbook CTA as M2; keep F1 repo-local |

## Success metrics (post-launch)

- Maintainer can answer “what is the next framework deliverable?” using **only** `docs/ROADMAP.md` + WBS.
- At least **one** external reader walks **ADOPTION** path without requesting clarification (qualitative until M2).
