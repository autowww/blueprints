---
nav_title: "Submodule update: Recovery"
nav_group: onboarding
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Updating the Blueprints submodule — Recovery and rollback

## What it is

**Before / during / after** concerns and **worked examples** when a bump goes wrong — complements [Routine bump](updating-submodule-routine.md) and [Validate and test](updating-submodule-validate.md).

**Parent page:** [Updating the Blueprints submodule](updating-blueprints-submodule.md).

## When to use it

When CI fails, the submodule is dirty, or you need to communicate a bad bump to the team.

## Update lifecycle (at a glance)

| Stage | What you do | If something breaks |
|-------|-------------|------------------------|
| **Before** | Read upstream release notes or diff you care about; agree on target SHA with your team | Defer bump until scope is clear |
| **During** | Fetch/checkout inside `blueprints/`; fast-forward pull; return to repo root; commit pointer | See [Troubleshooting](troubleshooting-faq.md) — conflicts or dirty submodule |
| **After** | Re-run validation: frozen tree present, optional `sync-forge-cursor-rules.sh check`, CI | Revert pointer commit or reset submodule to last known-good SHA |
| **Communicate** | Note the bump in your team channel or release notes when others must re-pull | N/A |

## Worked examples (rollback)

| Step | Situation | Action | Verify |
|------|-----------|--------|--------|
| 1 | CI failed after bump | `git revert` the submodule pointer commit or `git checkout` previous SHA in `blueprints/` | CI green again |
| 2 | Merge conflicts in `blueprints/` | Do not resolve by editing frozen files casually; reset submodule, re-apply upstream, or ask maintainers | Clean `git status` in submodule |

## What to do next

- [Policy](POLICY.md) — when you may change files under `blueprints/` vs project space
- [Troubleshooting / FAQ](troubleshooting-faq.md)
- [Validate and test](updating-submodule-validate.md)
