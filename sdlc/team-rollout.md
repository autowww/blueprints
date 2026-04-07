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
- At least one repo has `blueprints/`, project `sdlc/`, and optionally `forge/` in place ([SETUP.md](SETUP.md)).

## Rollout by scale

| Scale | Primary audience | What “good” looks like |
|-------|------------------|-------------------------|
| **Single team** | Tech lead + ICs | One **anchor** repo everyone can copy; shared read order for SDLC vocabulary |
| **Multi-team** | Chapter or org with several products | Published **golden** `blueprints` SHA; named owner for bumps and [submodule update](updating-blueprints-submodule.md) cadence |
| **Platform / org** | Enablement or architecture | Playbook for new repos; governance for exceptions to [Policy](POLICY.md); leadership briefing link when needed |

## Phased rollout (recommended)

| Phase | Focus | Success signal |
|-------|---------|----------------|
| **Pilot** | One anchor repo + one squad | [SETUP](SETUP.md) verify steps pass without one-off forks |
| **Expand** | Additional repos copy pin + scripts | Teams can state where baseline vs project text lives |
| **Standardize** | Golden SHA + office hours | New services reach parity without custom `blueprints/` edits |

## Steps

1. **Anchor repo** — Pick one service or library repo as the reference; document its layout in your internal wiki. Others copy the same submodule pin and scripts.
2. **Shared “golden” submodule SHA** — Platform or architecture publishes an approved `blueprints` commit; product repos bump on a cadence ([updating the submodule](updating-blueprints-submodule.md)).
3. **Office hours** — Short weekly slot for `forge-init`, Cursor rule sync, and “frozen vs project `sdlc/`” questions ([POLICY.md](POLICY.md)).
4. **Read order** — [SDLC blueprint](README.md) for lifecycle language; [disciplines hub](../disciplines/README.md) when a role needs depth; avoid assigning the whole tree as homework.

## Risks and mitigations

| Risk | Mitigation |
|------|------------|
| Silent drift — teams interpret ceremonies differently | Shared **read order** + link to one methodology slice you standardize on |
| Submodule chaos — mixed SHAs in production repos | Published golden SHA + [Updating the submodule](updating-blueprints-submodule.md) as the shared ritual |
| Change fatigue | Keep office hours short; prioritize **verify** steps over reading volume |

## How to verify success

- Teams can explain where **baseline** text lives (`blueprints/`) vs **their** interpretations (`sdlc/`, `docs/`).
- New repos reach the same **verify** steps as [SETUP.md](SETUP.md) without one-off forks of upstream.

## What to do next

- [Troubleshooting / FAQ](troubleshooting-faq.md)
- [Advanced customization](advanced-customization.md) — safe extension points in the consumer repo