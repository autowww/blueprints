---
nav_title: Platform playbook for Blueprints across many repos
nav_group: onboarding
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Platform playbook for Blueprints across many repos

## What it is

Enablement- or architecture-led rollout: **playbook** for new repos, **governance** for [Policy](POLICY.md) exceptions, and leadership messaging when needed.

**Parent page:** [Team rollout patterns](team-rollout.md).

## When to use it

Many products must pin the same upstream and leadership needs visibility.

## Prerequisites

- [Multi-team](team-rollout-multi-team.md) practices or equivalent governance buy-in.

## Focus

| Aspect | Guidance |
|--------|----------|
| **Playbook** | How new repos get `blueprints/`, `sdlc/`, Forge, and Cursor alignment — link to [SETUP](SETUP.md). |
| **Governance** | Who approves exceptions to frozen baseline rules; how long they stay open. |
| **Leadership** | Category and MVP narrative for executives — use [Adopting Blueprints — Path C](adopting-blueprints-path-c.md) (step 3) when you need a stakeholder-facing line into that material. |

## Org-wide phased timeline (example)

| Quarter phase | Focus | Success signal |
|---------------|-------|----------------|
| **Define** | Playbook + golden SHA policy | New repos follow the same checklist |
| **Enable** | Office hours and [governance cadence](team-rollout-governance.md) | Questions cluster in known forums |
| **Measure** | Exceptions count and time-to-bump | Few long-lived forks of baseline text |

## Risks and mitigations

| Risk | Mitigation |
|------|------------|
| Playbook ignored | Template repo or scaffold that runs the same first steps |
| Exception creep | Time-boxed waivers with owners |

## Anti-patterns

| Anti-pattern | Better |
|--------------|--------|
| Central team edits product repos without a ritual | Published playbook + self-service with review |
| “Everyone on latest” without support | Staged rollout with pilot services first |

## Example scenario (new service line)

| | |
|--|--|
| **Starting situation** | A new division spins up ten greenfield services over a year. |
| **Action taken** | Platform publishes the consumer playbook once; each service follows [SETUP](SETUP.md) and the same bump cadence. |
| **Expected result** | Services share vocabulary; leadership sees one story, not ten variants. |
| **What to check** | Architecture review references the same [Team rollout patterns](team-rollout.md) vocabulary. |

## How to verify success

New services reach parity without custom edits inside `blueprints/`; exceptions are rare and documented.

## What to do next

- [Governance cadence](team-rollout-governance.md)
- [Updating the Blueprints submodule](updating-blueprints-submodule.md)
- [Troubleshooting / FAQ](troubleshooting-faq.md)
