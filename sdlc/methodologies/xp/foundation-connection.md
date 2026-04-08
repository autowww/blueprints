---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# XP — connection to the SDLC foundation

XP emphasizes **technical excellence** (TDD, refactoring, CI, simple design) and **tight business feedback** (customer, small releases). The blueprint **tracking spine** and **C1–C6** still apply.

## 1. SDLC A–F (XP lens)

| Phase | XP expression |
|-------|----------------|
| **A — Shape** | **User stories** with customer; **release planning** themes |
| **B — Plan** | **Iteration planning**; task breakdown |
| **C — Build** | **Pair programming**, **TDD**, **continuous integration** |
| **D — Verify** | **Acceptance tests** (customer-written or team+customer); **collective ownership** reviews |
| **E — Release** | **Small releases**; frequent deployment where possible |
| **F — Operate & learn** | Production feedback; **retrospective** each iteration |

## 2. Tracking spine

| Artifact | XP mapping |
|----------|------------|
| **Intent** | Story |
| **Spec** | Story + acceptance test = spec |
| **Plan** | Iteration plan, tasks on board |
| **Tasks** | Engineering tasks (often on card wall) |
| **PRs** | Still used in git workflows; pair may co-author |
| **Reviews** | Pair review + team standards |
| **Release** | Small batch or continuous |

## 3. Ceremony intents ↔ XP

| Intent | XP practice / meeting |
|--------|------------------------|
| **C1** | Release planning; quarterly alignment |
| **C2** | Iteration planning |
| **C3** | Stand-up (if team uses it); **informal coordination** via pairing |
| **C4** | Acceptance tests; demo to customer |
| **C5** | Retrospective |
| **C6** | **Coding standards** doc; **metaphor** / shared vocabulary |

## 4. Role archetypes

| XP role | Archetypes |
|---------|------------|
| **Customer** (product voice) | **Sponsor proxy** |
| **Coach** | **Orchestrator**, **Quality advocate** |
| **Developers** | **Implementer**, **Quality advocate** (shared) |

## 5. Anti-patterns

| Anti-pattern | Fix |
|--------------|-----|
| “XP” without tests | Reinstate **TDD/ATDD** as non-negotiable |
| Customer proxy unavailable | Appoint empowered **single** proxy with acceptance authority |
| Pairing as watch-the-typer | Rotate driver/navigator; use ping-pong for TDD |

## 6. Links

- [`https://forgesdlc.com/methodology-xp.html`](https://forgesdlc.com/methodology-xp.html) · [ceremonies/xp.md](../ceremonies/xp.md)
