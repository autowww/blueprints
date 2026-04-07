---
nav_title: Updating the Blueprints submodule
nav_group: onboarding
---

# Updating the Blueprints submodule

## What it is

Commands and checks to move **`blueprints/`** to a newer upstream commit — no methodology prose.

## When to use it

Use this guide on a schedule, after upstream fixes, or when you need a feature that landed in `autowww/blueprints`.

## Prerequisites

- `blueprints/` is a **git submodule** at the repository root (not a stray copy without git metadata).
- You have permission to commit submodule pointer updates on your default branch.

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

## How to verify success

| Check | Command or expectation |
|-------|-------------------------|
| Submodule points at intended commit | `git -C blueprints rev-parse HEAD` matches upstream tag or branch tip you expect. |
| Frozen tree present | `test -f blueprints/sdlc/README.md` |
| Consumer scripts still run | From repo root: `bash blueprints/sdlc/methodologies/forge/setup/sync-forge-cursor-rules.sh check` (after [Cursor rules install](methodologies/forge/setup/CURSOR-RULES-QUICKSTART.md)) if you use Forge alignment. |
| CI | Your pipeline still passes; submodule bump can surface new templates — re-run [SETUP.md](SETUP.md) validation steps if unsure. |

## What to do next

- [Policy](POLICY.md) — when you may change files under `blueprints/` vs project space.
- [Troubleshooting / FAQ](troubleshooting-faq.md) — common submodule and path issues.
