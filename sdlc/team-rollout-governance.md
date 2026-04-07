---
nav_title: "Team rollout: Governance cadence"
nav_group: onboarding
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Team rollout — Governance cadence

## What it is

**Phased rollout**, **office hours**, and **risk** handling that apply across single-team, multi-team, and platform rollouts.

**Parent page:** [Team rollout patterns](team-rollout.md).

## When to use it

Whenever more than a one-off email is needed to keep adoption healthy.

## Phased rollout

| Phase | Focus | Success signal |
|-------|---------|----------------|
| **Pilot** | One anchor repo + one squad | [SETUP](SETUP.md) verify steps pass without one-off forks |
| **Expand** | Additional repos copy pin + scripts | Teams can state where baseline vs project text lives |
| **Standardize** | Golden SHA + office hours | New services reach parity without custom `blueprints/` edits |

## Office hours

Short weekly slot for `forge-init`, Cursor rule sync, and “frozen vs project `sdlc/`” questions ([POLICY.md](POLICY.md)).

## Risks and mitigations

| Risk | Mitigation |
|------|------------|
| Silent drift — teams interpret ceremonies differently | Shared **read order** + link to one methodology slice you standardize on |
| Submodule chaos — mixed SHAs in production repos | Published golden SHA + [Updating the submodule](updating-blueprints-submodule.md) as the shared ritual |
| Change fatigue | Keep office hours short; prioritize **verify** steps over reading volume |

## How to verify success

Teams use the same rituals for bumps and questions; drift is visible and corrected in office hours.

## What to do next

- [Team rollout patterns](team-rollout.md)
- [Troubleshooting / FAQ](troubleshooting-faq.md)
