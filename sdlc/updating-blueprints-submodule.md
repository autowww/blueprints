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

## Update lifecycle (at a glance)

| Stage | What you do | If something breaks |
|-------|-------------|------------------------|
| **Before** | Read upstream release notes or diff you care about; agree on target SHA with your team | Defer bump until scope is clear |
| **During** | Fetch/checkout inside `blueprints/`; fast-forward pull; return to repo root; commit pointer | See [Troubleshooting](troubleshooting-faq.md) — conflicts or dirty submodule |
| **After** | Re-run validation: frozen tree present, optional `sync-forge-cursor-rules.sh check`, CI | Revert pointer commit or reset submodule to last known-good SHA |
| **Communicate** | Note the bump in your team channel or release notes when others must re-pull | N/A |

**What could break:** new templates under `blueprints/` can require re-running Cursor rule sync or copying updated templates — not automatic. Treat a bump like a small dependency upgrade.

### Worked example (rollback mindset)

| Step | Situation | Action | Verify |
|------|-----------|--------|--------|
| 1 | CI failed after bump | `git revert` the submodule pointer commit or `git checkout` previous SHA in `blueprints/` | CI green again |
| 2 | Merge conflicts in `blueprints/` | Do not resolve by editing frozen files casually; reset submodule, re-apply upstream, or ask maintainers | Clean `git status` in submodule |

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