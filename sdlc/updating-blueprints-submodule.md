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

### Update lifecycle (visual)

```blueprint-diagram
key: linear
alt: Submodule update lifecycle — routine bump, validate and test, then recovery only if something fails
title: Submodule update lifecycle
summary: Pick a guide topic, run the governed bump workflow, and reach a reviewable outcome—or recovery if validation fails.
node: Choose a topic
detail: Select routine bump, validate, or recovery from the topic table.
more: The table links to routine bump, validate and test, and recovery pages; the quick flow is routine, then validate, then recovery only on failure.
node: Start
detail: Begin from prerequisites with a submodule at the repository root.
more: Confirm blueprints/ is a git submodule and you have permission to commit pointer updates on your default branch.
node: Core steps (see walkthrough below)
detail: Execute fetch, pull, validate, and test per your chosen topic page.
more: Routine covers fetch and pointer commit; validate adds CI and frozen-tree checks; recovery applies when bumps or tests fail.
node: Outcome
detail: A committed submodule pointer or a documented rollback path.
more: Success is a reviewable pointer update on your branch; failures route to recovery and the troubleshooting FAQ.
fallback_ascii: |
  Choose a topic

  Start
      |
      v
  Core steps (see walkthrough below)
      |
      v
  Outcome
```

## What to do next

- [Blueprint policy](POLICY.md) — when you may change files under `blueprints/` vs project space.
- [Troubleshooting / FAQ](troubleshooting-faq.md) — common submodule and path issues.
