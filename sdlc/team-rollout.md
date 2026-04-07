---
nav_title: Team rollout patterns
nav_group: onboarding
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Team rollout patterns

## What it is

Patterns for introducing Blueprints **after** one person has a working [first-hour](quickstarts/first-hour.md) layout — not a full change-management program. Scale the formality to your org: a single team needs fewer artifacts than a platform coordinating many repos.

## When to use it

Use this page when more than one repo or squad needs the same vocabulary (phases, ceremonies, discipline bridges).

## Prerequisites

- [Adopting Blueprints](adopting-blueprints.md) path **B** or **C** is a rough match.
- At least one repo has `blueprints/`, project `sdlc/`, and optionally `forge/` in place ([SETUP](SETUP.md)).

## Rollout by scale (chooser)

| Scale | Primary audience | Deep dive |
|-------|------------------|-----------|
| **Single team** | Tech lead + ICs | [Single-team rollout](team-rollout-single-team.md) |
| **Multi-team** | Chapter or org with several products | [Multi-team rollout](team-rollout-multi-team.md) |
| **Platform / org** | Enablement or architecture | [Platform / org rollout](team-rollout-org-platform.md) |
| **Governance** | Phased rollout, office hours, risks | [Governance cadence](team-rollout-governance.md) |

## How to verify success

- Teams can explain where **baseline** text lives (`blueprints/`) vs **their** interpretations (`sdlc/`, `docs/`).
- New repos reach the same **verify** steps as [SETUP.md](SETUP.md) without one-off forks of upstream.

## What to do next

- [Troubleshooting / FAQ](troubleshooting-faq.md)
- [Advanced customization](advanced-customization.md) — safe extension points in the consumer repo
