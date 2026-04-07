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

## Ownership (typical)

| Role | Owns |
|------|------|
| Tech lead | Anchor repo layout and first [SETUP](SETUP.md) verify pass for that repo |
| Maintainer | Submodule pointer when the approved upstream commit moves |
| Product / EM | Which methodology slice the team standardizes on first (not “everything at once”) |

## Phased timeline (example)

| Week | Focus | Success signal |
|------|-------|----------------|
| 0 | Choose anchor repo; document its layout internally | New teammates can name **baseline** (`blueprints/`) vs **project** (`sdlc/`, `docs/`) |
| 1–2 | Each developer runs the same verify steps | No one-off edits inside `blueprints/` for product wording |
| 3–4 | One shared read order (e.g. [SDLC blueprint](README.md) sections by role) | Onboarding links to **sections**, not the whole tree |

### Week-zero checklist (visual)

```blueprint-diagram
key: checklist
alt: Anchor repo, document layout, verify SETUP, standardize one read slice
```

## Risks and mitigations

| Risk | Mitigation |
|------|------------|
| Homework overload | Cap reading to one slice; use [Adopting Blueprints](adopting-blueprints.md) to justify the scope |
| Drift in ceremonies | Tie rituals to the anchor repo’s documented layout |

## Anti-patterns

| Anti-pattern | Better |
|--------------|--------|
| Forking upstream `blueprints/` for one team’s wording | Use project **`sdlc/`** and [Policy](POLICY.md) |
| “Everyone read everything” | Publish a short **read order** and revisit in retro |

## Example scenario (single team)

| | |
|--|--|
| **Starting situation** | One squad owns a single API; path B adoption is chosen; other teams are out of scope for now. |
| **Action taken** | Tech lead documents the anchor repo layout; others clone the same submodule pin and run [SETUP](SETUP.md) verify steps. |
| **Expected result** | Two repos match the same baseline without custom forks of `blueprints/sdlc/`. |
| **What to check** | Onboarding doc links to [SDLC blueprint](README.md) sections by role, not the whole tree. |

## Example scenario (shared library first)

| | |
|--|--|
| **Starting situation** | A platform library repo is the natural anchor; app teams will follow in a later wave. |
| **Action taken** | Library team completes verify steps and documents the submodule pin; app teams are told to copy the same ritual when they join. |
| **Expected result** | One golden pattern exists before scaling to more repos. |
| **What to check** | [Updating the Blueprints submodule](updating-blueprints-submodule.md) is linked from the team wiki or runbook. |

## How to verify success

One anchor repo is documented; teammates can repeat [SETUP](SETUP.md) verify steps without one-off forks.

## What to do next

- [Team rollout patterns](team-rollout.md) — multi-team and platform
- [Multi-team rollout](team-rollout-multi-team.md)
- [Updating the Blueprints submodule](updating-blueprints-submodule.md) · [Troubleshooting / FAQ](troubleshooting-faq.md)
