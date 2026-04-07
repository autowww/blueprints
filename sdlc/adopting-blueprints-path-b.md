---
nav_title: "Adopting: path B (team lead / EM)"
nav_group: onboarding
public_publish: true
audience: public
handbook_area: blueprints
learning_level: overview
---

# Adopting Blueprints — Path B (team lead / EM)

## What it is

**ICP path B:** a **shared vocabulary** for phases, ceremonies, and discipline bridges across repos.

**Parent page:** [Adopting Blueprints](adopting-blueprints.md). Complete path **A** first; path **B** builds on it.

## When to use it

When the [decision guide](adopting-blueprints.md#decision-guide) points you to path **B**.

## Prerequisites

- Path **A** basics in place (submodule, project `sdlc/`).

## Steps

**Job to be done:** “I need a shared vocabulary for phases, ceremonies, and discipline bridges across repos.”

| Step | Action | Verify |
|------|--------|--------|
| 1 | Complete path **A**. | Same checks as [path A](adopting-blueprints-path-a.md). |
| 2 | Point the team at the [SDLC blueprint](README.md) and the methodology slice you follow (e.g. Scrum, Kanban, Forge) under `blueprints/sdlc/methodologies/`. | Team can name your default methodology entry file. |
| 3 | Optionally wire **Forge** artifacts (`forge/`, `ember-logs/`) using templates under `blueprints/sdlc/templates/forge/` in a **consumer** repo. | `forge/forge.config.yaml` exists after [Forge init](methodologies/forge/setup/README.md). |

## How to verify success

Team can name your methodology entry point and (if using Forge) has a valid `forge/forge.config.yaml`. Use [Team rollout patterns](team-rollout.md) when more than one repo must align.

## What to do next

- [Adopting Blueprints](adopting-blueprints.md) — path C (platform)
- [Team rollout patterns](team-rollout.md)
- [Project setup profile](SETUP.md)
