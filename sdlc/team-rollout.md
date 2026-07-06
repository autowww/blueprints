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
- At least one repo has `blueprints/`, project `sdlc/`, and optionally `forge/` in place ([Project setup checklist](SETUP.md)).

## Rollout by scale (chooser)

| Scale | Primary audience | Deep dive |
|-------|------------------|-----------|
| **Single team** | Tech lead + ICs | [Single-team rollout](team-rollout-single-team.md) |
| **Multi-team** | Chapter or org with several products | [Multi-team rollout](team-rollout-multi-team.md) |
| **Platform / org** | Enablement or architecture | [Platform / org rollout](team-rollout-org-platform.md) |
| **Governance** | Phased rollout, office hours, risks | [Governance cadence](team-rollout-governance.md) |

### Rollout scale (visual)

Formality and coordination increase as you move from one team to many repos and platform governance — pick the row that matches your scope, then read that child page.

```blueprint-diagram
key: timeline
alt: Team rollout — increasing scale from single team to multi-team, platform, and governance cadence
title: Rollout scale progression
summary: How teams move from picking a rollout scope to governed, shared Blueprints adoption.
node: Rollout by scale (chooser)
detail: Match your org scope to a rollout row in the table.
more: Single team needs fewer artifacts than platform governance; pick the row that fits before reading the deep dive.
node: Actor / trigger
detail: A lead or enablement role recognizes Blueprints must scale beyond one repo.
more: Typically follows a successful first-hour layout in at least one repo and path B or C from Adopting Blueprints.
node: System step
detail: Apply the rollout pattern from the matching child page.
more: Each scale page defines ceremonies, artifacts, and coordination appropriate to that audience without forking upstream baseline text.
node: Outcome / handoff
detail: Teams share vocabulary and reach the same verify steps.
more: Success means baseline lives in blueprints/ while project interpretations stay in sdlc/ and docs/ without one-off forks.
fallback_ascii: |
  Rollout by scale (chooser)

  Actor / trigger
      |
      v
  System step
      |
      v
  Outcome / handoff
```

## How to verify success

- Teams can explain where **baseline** text lives (`blueprints/`) vs **their** interpretations (`sdlc/`, `docs/`).
- New repos reach the same **verify** steps as [Project setup checklist](SETUP.md) without one-off forks of upstream.

## What to do next

- [Troubleshooting / FAQ](troubleshooting-faq.md)
- [Advanced customization](advanced-customization.md) — safe extension points in the consumer repo
