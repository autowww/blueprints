---
nav_title: "Submodule update: Routine bump"
nav_group: onboarding
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Updating the Blueprints submodule — Routine bump

## What it is

The **standard commands** to fast-forward `blueprints/` to a newer upstream commit.

**Parent page:** [Updating the Blueprints submodule](updating-blueprints-submodule.md).

## When to use it

On a schedule, after upstream fixes, or when you need a feature from `autowww/blueprints`.

## Prerequisites

- [Updating the Blueprints submodule — Prerequisites](updating-blueprints-submodule.md#prerequisites)

## Steps

From the **repository root** (parent of `blueprints/`):

```bash
cd blueprints
git fetch origin
git checkout main   # or the branch your org tracks
git pull --ff-only
cd ..
git status
git add blueprints
git commit -m "chore: bump blueprints submodule"
```

If you use nested submodules inside `blueprints/`:

```bash
git submodule update --init --recursive
```

## Optional: refresh local Forge installers

Blueprint updates do **not** rewrite `.git/hooks/` in your clone. If you use the **version / release-notes** post-commit hook, reinstall it after meaningful Blueprints pulls so you pick up script fixes:

```bash
bash blueprints/sdlc/methodologies/forge/setup/install-version-release-hook.sh
```

See [Versioning and release notes](methodologies/forge/setup/VERSIONING-AND-RELEASES.md).

## What to do next

- [Validate and test](updating-submodule-validate.md)
- [Recovery and rollback](updating-submodule-recovery.md)
- [Troubleshooting / FAQ](troubleshooting-faq.md)
