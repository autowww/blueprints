---
nav_title: Updating the Blueprints submodule
nav_group: onboarding
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Updating the Blueprints submodule

## What it is

Commands and checks to move **`blueprints/`** to a newer upstream commit — no methodology prose.

## When to use it

Use this guide on a schedule, after upstream fixes, or when you need a feature that landed in `autowww/blueprints`.

## Prerequisites

- `blueprints/` is a **git submodule** at the repository root (not a stray copy without git metadata).
- You have permission to commit submodule pointer updates on your default branch.

## Choose a topic

| Topic | Page |
|-------|------|
| **Routine bump** — fetch, pull, commit pointer | [Routine bump](updating-submodule-routine.md) |
| **Validate and test** — CI, `check`, frozen tree | [Validate and test](updating-submodule-validate.md) |
| **Recovery** — lifecycle, rollback, conflicts | [Recovery and rollback](updating-submodule-recovery.md) |

**Quick flow:** routine → validate → if anything fails, recovery and [Troubleshooting](troubleshooting-faq.md).

## What to do next

- [Policy](POLICY.md) — when you may change files under `blueprints/` vs project space.
- [Troubleshooting / FAQ](troubleshooting-faq.md) — common submodule and path issues.
