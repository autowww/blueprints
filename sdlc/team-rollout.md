---
nav_title: Team rollout patterns
nav_group: onboarding
---

# Team rollout patterns

## What it is

Thin v1 patterns for introducing Blueprints **after** one person has a working [first-hour](quickstarts/first-hour.md) layout — not a full change-management program.

## When to use it

Use this page when more than one repo or squad needs the same vocabulary (phases, ceremonies, discipline bridges).

## Prerequisites

- [Adopting Blueprints](adopting-blueprints.md) path **B** or **C** is a rough match.
- At least one repo has `blueprints/`, project `sdlc/`, and optionally `forge/` in place ([SETUP.md](SETUP.md)).

## Steps

1. **Anchor repo** — Pick one service or library repo as the reference; document its layout in your internal wiki. Others copy the same submodule pin and scripts.
2. **Shared “golden” submodule SHA** — Platform or architecture publishes an approved `blueprints` commit; product repos bump on a cadence ([updating the submodule](updating-blueprints-submodule.md)).
3. **Office hours** — Short weekly slot for `forge-init`, Cursor rule sync, and “frozen vs project `sdlc/`” questions ([POLICY.md](POLICY.md)).
4. **Read order** — [SDLC blueprint](README.md) for lifecycle language; [disciplines hub](../disciplines/README.md) when a role needs depth; avoid assigning the whole tree as homework.

## How to verify success

- Teams can explain where **baseline** text lives (`blueprints/`) vs **their** interpretations (`sdlc/`, `docs/`).
- New repos reach the same **verify** steps as [SETUP.md](SETUP.md) without one-off forks of upstream.

## What to do next

- [Troubleshooting / FAQ](troubleshooting-faq.md)
- [Advanced customization](advanced-customization.md) — safe extension points in the consumer repo
