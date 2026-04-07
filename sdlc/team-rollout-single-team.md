---
nav_title: "Team rollout: Single team"
nav_group: onboarding
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Team rollout — Single team

## What it is

Rolling out Blueprints when **one squad** needs shared vocabulary — lightest formality.

**Parent page:** [Team rollout patterns](team-rollout.md).

## When to use it

[Adopting Blueprints](adopting-blueprints.md) path **B** or **C** is a rough match, but only one team is in scope first.

## Prerequisites

- At least one repo has `blueprints/`, project `sdlc/`, and optionally `forge/` ([SETUP](SETUP.md)).

## Focus

| Aspect | Guidance |
|--------|----------|
| **Anchor repo** | Pick one service or library repo as the reference; document its layout in your internal wiki. Others copy the same submodule pin and scripts. |
| **Read order** | [SDLC blueprint](README.md) for lifecycle language; avoid assigning the whole blueprint tree as homework. |

## Example scenario (single team)

| | |
|--|--|
| **Starting situation** | One squad owns a single API; path B adoption is chosen; other teams are out of scope for now. |
| **Action taken** | Tech lead documents the anchor repo layout; others clone the same submodule pin and run [SETUP](SETUP.md) verify steps. |
| **Expected result** | Two repos match the same baseline without custom forks of `blueprints/sdlc/`. |
| **What to check** | Onboarding doc links to [SDLC blueprint](README.md) sections by role, not the whole tree. |

## How to verify success

One anchor repo is documented; teammates can repeat [SETUP](SETUP.md) verify steps without one-off forks.

## What to do next

- [Team rollout patterns](team-rollout.md) — multi-team and platform
- [Multi-team rollout](team-rollout-multi-team.md)
