---
nav_title: Adopting Blueprints
nav_group: onboarding
---

# Adopting Blueprints

## What it is

Choosing **which adoption story** matches you (ICP-style paths A / B / C) — not the command-by-command [first hour](quickstarts/first-hour.md).

Blueprints is a **reusable documentation framework**: SDLC, PDLC, disciplines, and Forge / Versona patterns you consume as **`blueprints/`** in your repo. Your **project** work lives in **`sdlc/`**, **`docs/`**, **`forge/`** at the repository root — not in edits to the frozen baseline under `blueprints/` (see [Policy](POLICY.md)).

**Hands-on first hour:** [Quickstarts — First hour](quickstarts/first-hour.md).

## When to use it

Use this page **before** you deep-read methodology folders or maintainer docs. After you pick a path, run the [first hour](quickstarts/first-hour.md) or the full [setup checklist](SETUP.md).

## Prerequisites

1. Add Blueprints as a **git submodule** at `blueprints/` (or copy the tree if you do not use submodules). The [handbook home](../README.md) summarizes layout expectations.
2. Decide which **ICP path** below matches you — the same upstream tree supports different jobs.

## Steps

### ICP path A — Solo developer or small team

**Job to be done:** “I want a sane default SDLC/PDLC text baseline without writing it from scratch.”

| Step | Action | Verify |
|------|--------|--------|
| 1 | Submodule Blueprints under `blueprints/`. | `test -f blueprints/sdlc/README.md` |
| 2 | Add a **project** `sdlc/` folder (interpretations, principles) — do **not** edit `blueprints/sdlc/`; see [Policy](POLICY.md). | `sdlc/README.md` exists after [init script](quickstarts/first-hour.md). |
| 3 | Add `docs/product/` when you need capabilities/journeys (seed from [`product/templates/`](../product/templates/README.md)). | Optional; structure matches your product docs needs. |

### ICP path B — Team lead / EM

**Job to be done:** “I need a shared vocabulary for phases, ceremonies, and discipline bridges across repos.”

| Step | Action | Verify |
|------|--------|--------|
| 1 | Complete path **A**. | Same checks as above. |
| 2 | Point the team at [SDLC blueprint](README.md) and the methodology slice you follow (e.g. Scrum, Kanban, Forge) under `blueprints/sdlc/methodologies/`. | Team can name your default methodology entry file. |
| 3 | Optionally wire **Forge** artifacts (`forge/`, `ember-logs/`) using templates under `blueprints/sdlc/templates/forge/` in a **consumer** repo. | `forge/forge.config.yaml` exists after [Forge init](methodologies/forge/setup/README.md). |

### ICP path C — Organization method / platform group

**Job to be done:** “We want a single upstream corpus we can submodule into many products and keep in sync.”

| Step | Action | Verify |
|------|--------|--------|
| 1 | Treat [`autowww/blueprints`](https://github.com/autowww/blueprints) as **upstream**; fork only if you must diverge on policy. | Documented upstream URL and bump process. |
| 2 | Maintain a **consumer** playbook: submodule bump cadence, [policy](POLICY.md) exceptions if any. | [Updating the submodule](updating-blueprints-submodule.md) is part of ops. |
| 3 | For category positioning when briefing leadership, see [`product/discovery/framework-positioning-and-mvp.md`](../product/discovery/framework-positioning-and-mvp.md). | Stakeholders have a one-pager link when needed. |

## How to verify success

You have picked a path and can execute the **Verify** column for that path’s table (and complete path **A** before **B** or **C** where required). Next, confirm the concrete repo checks in [first hour](quickstarts/first-hour.md) or the full [SETUP](SETUP.md) checklist.

## What to do next

- **Concrete steps (~60 min):** [First hour](quickstarts/first-hour.md)
- **Full ordered checklist:** [Project setup profile](SETUP.md)
- **SDLC entry:** [SDLC blueprint](README.md)
- **Rollout with others:** [Team rollout patterns](team-rollout.md)
- **Submodule hygiene:** [Updating the submodule](updating-blueprints-submodule.md)

## Maintainer and GitHub-only detail

Roadmap, wiki sync mechanics, and generator maintenance notes stay in the upstream repo under `docs/` on **GitHub** — for example [ADOPTION.md](https://github.com/autowww/blueprints/blob/main/docs/ADOPTION.md) (companion to this page) and [ROADMAP.md](https://github.com/autowww/blueprints/blob/main/docs/ROADMAP.md). Use those when you need **release** or **framework product** context, not for day-one adoption.
