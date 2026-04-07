---
nav_title: Adopting Blueprints
nav_group: onboarding
---

# Adopting Blueprints

## What it is

Choosing **which adoption story** matches you (ICP-style paths A / B / C) — not the command-by-command [first hour](quickstarts/first-hour.md).

Blueprints is a **reusable documentation framework**: SDLC, PDLC, disciplines, and Forge / Versona patterns you consume as a **Blueprints tree** in your repository (often a submodule named `blueprints/`). Your **project** work lives in **`sdlc/`**, **`docs/`**, **`forge/`** at the repository root — not in edits to the frozen baseline inside the Blueprints tree (see [Policy](POLICY.md)).

**Hands-on first hour:** [Quickstarts — First hour](quickstarts/first-hour.md).

## When to use it

Use this page **before** you deep-read methodology folders or maintainer docs. After you pick a path, run the [first hour](quickstarts/first-hour.md) or the full [setup checklist](SETUP.md).

## Prerequisites

1. Add Blueprints to your repo (typically as a **git submodule** at `blueprints/`; or copy the tree if you do not use submodules). The [handbook home](../README.md) summarizes layout expectations.
2. Decide which **ICP path** below matches you — the same upstream tree supports different jobs.

## Steps

### ICP path A — Solo developer or small team

**Job to be done:** “I want a sane default SDLC/PDLC text baseline without writing it from scratch.”

| Step | Action | Verify |
|------|--------|--------|
| 1 | Submodule (or copy) Blueprints into `blueprints/`. | `test -f blueprints/sdlc/README.md` |
| 2 | Add a **project** `sdlc/` folder (interpretations, principles) — do **not** edit the copy under `blueprints/sdlc/`; see [Policy](POLICY.md). | `sdlc/README.md` exists after [init script](quickstarts/first-hour.md). |
| 3 | Add `docs/product/` when you need capabilities/journeys (seed from [product templates](../product/templates/README.md)). | Optional; structure matches your product docs needs. |

### ICP path B — Team lead / EM

**Job to be done:** “I need a shared vocabulary for phases, ceremonies, and discipline bridges across repos.”

| Step | Action | Verify |
|------|--------|--------|
| 1 | Complete path **A**. | Same checks as above. |
| 2 | Point the team at the [SDLC blueprint](README.md) and the methodology slice you follow (e.g. Scrum, Kanban, Forge) under `blueprints/sdlc/methodologies/`. | Team can name your default methodology entry file. |
| 3 | Optionally wire **Forge** artifacts (`forge/`, `ember-logs/`) using templates under `blueprints/sdlc/templates/forge/` in a **consumer** repo. | `forge/forge.config.yaml` exists after [Forge init](methodologies/forge/setup/README.md). |

### ICP path C — Organization method / platform group

**Job to be done:** “We want a single upstream corpus we can submodule into many products and keep in sync.”

| Step | Action | Verify |
|------|--------|--------|
| 1 | Treat the [upstream Blueprints repository](https://github.com/autowww/blueprints) as **upstream**; fork only if you must diverge on policy. | Documented upstream URL and bump process. |
| 2 | Maintain a **consumer** playbook: submodule bump cadence, [policy](POLICY.md) exceptions if any. | [Updating the submodule](updating-blueprints-submodule.md) is part of ops. |
| 3 | For category positioning when briefing leadership, see [framework positioning and MVP](https://github.com/autowww/blueprints/blob/main/docs/product/discovery/framework-positioning-and-mvp.md). | Stakeholders have a one-pager link when needed. |

## How to verify success

You have picked a path and can execute the **Verify** column for that path’s table (and complete path **A** before **B** or **C** where required). Next, confirm the concrete repo checks in [first hour](quickstarts/first-hour.md) or the full [SETUP](SETUP.md) checklist.

## What to do next

Stay on the adoption path (hands-on and ops — not a methodology tour):

- [Quickstarts hub](quickstarts/README.md)
- [First hour](quickstarts/first-hour.md) (~60 minutes)
- [Project setup profile](SETUP.md)
- [Troubleshooting and FAQ](troubleshooting-faq.md)
- [Updating the submodule](updating-blueprints-submodule.md)
- [Team rollout patterns](team-rollout.md)

---

## Maintainer and GitHub-only detail

Release notes and framework-product context live on GitHub (for example [ADOPTION.md](https://github.com/autowww/blueprints/blob/main/docs/ADOPTION.md), [ROADMAP.md](https://github.com/autowww/blueprints/blob/main/docs/ROADMAP.md)). Skip this block until you need upstream or release mechanics.
