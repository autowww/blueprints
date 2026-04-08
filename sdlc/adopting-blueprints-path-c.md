---
nav_title: "Adopting: path C (org / platform)"
nav_group: onboarding
public_publish: true
audience: public
handbook_area: blueprints
learning_level: overview
---

# Adopting Blueprints — Path C (organization / platform group)

## What it is

**ICP path C:** a **single upstream corpus** you submodule into many products and keep in sync.

**Parent page:** [Adopting Blueprints](adopting-blueprints.md). Path **A** (and usually **B**) still apply at the repo level; path **C** adds governance across products.

## When to use it

When the [decision guide](adopting-blueprints.md#decision-guide) points you to path **C**.

## Prerequisites

- Documented upstream and bump process; teams comfortable with [Policy](POLICY.md) and submodule workflows.

## Steps

**Job to be done:** “We want a single upstream corpus we can submodule into many products and keep in sync.”

| Step | Action | Verify |
|------|--------|--------|
| 1 | Treat the [upstream Blueprints repository](https://github.com/autowww/blueprints) as **upstream**; fork only if you must diverge on policy. | Documented upstream URL and bump process. |
| 2 | Maintain a **consumer** playbook: submodule bump cadence, [policy](POLICY.md) exceptions if any. | [Updating the submodule](updating-blueprints-submodule.md) is part of ops. |
| 3 | For category positioning when briefing leadership, see [framework positioning and MVP](https://github.com/autowww/blueprints/blob/main/docs/product/discovery/framework-positioning-and-mvp.md). | Stakeholders have a one-pager link when needed. |

## Example scenario (path C)

| | |
|--|--|
| **Starting situation** | Platform team owns `autowww/blueprints` consumption across fifteen services; security wants a single approved SHA quarterly. |
| **Action taken** | Publish a “golden” submodule bump schedule; teams follow [Updating the submodule](updating-blueprints-submodule.md); exceptions go through documented policy. |
| **Expected result** | Product repos move `blueprints/` in lockstep or on an approved lag; no silent one-off forks of upstream text. |
| **What to check** | CI or release notes show bump commits; [Platform playbook for Blueprints](team-rollout-org-platform.md) matches how you coordinate. |

## How to verify success

Playbook exists; golden SHA or cadence is published; [Platform playbook for Blueprints](team-rollout-org-platform.md) patterns apply when coordinating many repos.

## What to do next

- [Updating the Blueprints submodule](updating-blueprints-submodule.md)
- [Team rollout patterns](team-rollout.md)
- [Adopting Blueprints](adopting-blueprints.md) — recap paths A / B
