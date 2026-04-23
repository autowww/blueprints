---
nav_title: "Submodule update: Validate and test"
nav_group: onboarding
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Updating the Blueprints submodule — Validate and test

## What it is

Checks to run **after** a routine bump so consumers (CI, Cursor rules, templates) still behave.

**Parent page:** [Updating the Blueprints submodule](updating-blueprints-submodule.md).

## When to use it

After every submodule pointer change, before you merge or tag.

## Prerequisites

- [Routine bump](updating-submodule-routine.md) completed (or you are validating a proposed SHA).

## Checks

| Check | Command or expectation |
|-------|-------------------------|
| Submodule points at intended commit | `git -C blueprints rev-parse HEAD` matches upstream tag or branch tip you expect. |
| Frozen tree present | `test -f blueprints/sdlc/README.md` |
| Consumer scripts still run | From repo root: `bash blueprints/sdlc/methodologies/forge/setup/sync-forge-cursor-rules.sh check` (after [Cursor rules install](methodologies/forge/setup/CURSOR-RULES-QUICKSTART.md)) if you use Forge alignment. |
| CI | Your pipeline still passes; submodule bump can surface new templates — re-run [Project setup checklist](SETUP.md) validation steps if unsure. |

**What could break:** new templates under `blueprints/` can require re-running Cursor rule sync or copying updated templates — not automatic. Treat a bump like a small dependency upgrade.

## What to do next

- [Recovery and rollback](updating-submodule-recovery.md) if something fails
- [Project setup profile](SETUP.md)
- [Troubleshooting / FAQ](troubleshooting-faq.md)
