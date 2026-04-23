---
nav_title: Troubleshooting and FAQ
nav_group: onboarding
public_publish: true
audience: public
handbook_area: blueprints
learning_level: troubleshooting
---

# Troubleshooting and FAQ

## What it is

Short answers for **consuming** Blueprints in a repo — not upstream maintainer runbooks.

## When to use it

Use this page when something failed during [first hour](quickstarts/first-hour.md), [Project setup checklist](SETUP.md), or a [submodule update](updating-blueprints-submodule.md).

## Prerequisites

No extra prerequisites — jump to the subsection below that matches your symptom.

## Symptom index

| Symptom | Jump to |
|---------|---------|
| Missing `blueprints/sdlc/...` after clone | [Submodule and layout](#submodule-and-layout) |
| “No such file” when running a script | [Submodule and layout](#submodule-and-layout) — working directory |
| Accidental edits under `blueprints/` | [Submodule and layout](#submodule-and-layout) |
| `forge-init` or Cursor sync errors | [Forge and Cursor](#forge-and-cursor) |
| Looking for roadmap / maintainer docs | [Handbook vs GitHub](#handbook-vs-github) |

**Fast triage:** confirm you are at the **repository root**, then `git submodule update --init --recursive`, then re-run the failing command.

**Evidence to gather before asking for help:** exact command, working directory, output of `git status` (root and `blueprints/`), and whether the repo just bumped the `blueprints` submodule.

## Steps

Work through the subsection that matches your issue.

### Submodule and layout

**`blueprints/sdlc/...` not found after clone**

Run from the repo root:

```bash
git submodule update --init --recursive
```

**Scripts assume wrong working directory**

Most scripts expect the **repository root** (the folder that contains `blueprints/`). `cd` to that root and re-run.

**I edited files under `blueprints/` by mistake**

Stop; see [Blueprint policy](POLICY.md). Prefer changes in project `sdlc/`, `docs/`, or `forge/`. Revert local edits to the submodule or reset to the committed SHA, then apply your intent in the project workspace.

### Forge and Cursor

**`forge-init.sh` or sync scripts error**

- Confirm **Python 3** is on `PATH`.
- Run from repo root; paths are relative to it.
- After a submodule bump, run `sync-forge-cursor-rules.sh diff` or `check` before `--force` sync — see [CURSOR-RULES-QUICKSTART.md](methodologies/forge/setup/CURSOR-RULES-QUICKSTART.md).

**Where is Forge Studio?**

Forge Studio (Lenses Studio) is a **separate** app: [forge-lenses](https://github.com/autowww/forge-lenses). Handbook pages for it are published under [Lenses on the handbook](https://blueprints.forgesdlc.com/lenses/index.html); the runnable server is local to your machine — see [Forge Studio quickstart](quickstarts/forge-studio.md).

### Handbook vs GitHub

**I need maintainer roadmap, WBS, or wiki sync details**

Those live under `docs/` in the upstream repo on **GitHub** only — not the adoption-first handbook surface. Start from the repo’s [`docs/` folder](https://github.com/autowww/blueprints/tree/main/docs).

## How to verify success

- The blocking issue is resolved: submodule present, commands run from repo root, or you know to use **GitHub** for maintainer-only docs.
- Optional: re-run the **Verify** checks from [first hour](quickstarts/first-hour.md) or [updating the submodule](updating-blueprints-submodule.md).

## What to do next

- [Adopting Blueprints](adopting-blueprints.md)
- [First hour](quickstarts/first-hour.md)
- [Project setup profile](SETUP.md)