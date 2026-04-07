---
nav_title: Adopting Blueprints
nav_group: onboarding
public_publish: true
audience: public
handbook_area: blueprints
learning_level: overview
---

# Adopting Blueprints

## What it is

Choosing **which adoption story** matches you (ICP-style paths A / B / C) — not the command-by-command [first hour](quickstarts/first-hour.md).

Blueprints is a **reusable documentation framework**: SDLC, PDLC, disciplines, and Forge / Versona patterns you consume as a **Blueprints tree** in your repository (often a submodule named `blueprints/`). Your **project** work lives in **`sdlc/`**, **`docs/`**, **`forge/`** at the repository root — not in edits to the frozen baseline inside the Blueprints tree (see [Policy](POLICY.md)).

**Hands-on first hour:** [Quickstarts — First hour](quickstarts/first-hour.md).

## When to use it

Use this page **before** you deep-read methodology folders or maintainer docs. Pick a **path** below, then run the [first hour](quickstarts/first-hour.md) or the full [setup checklist](SETUP.md).

## Prerequisites

1. Add Blueprints to your repo (typically as a **git submodule** at `blueprints/`; or copy the tree if you do not use submodules). The [handbook home](../README.md) summarizes layout expectations.
2. Use the **decision guide** and **path pages** next.

## Decision guide

Answer in order; the first row that matches your situation is usually the right starting path.

| Question | If yes → |
|----------|----------|
| You mainly need a solid text baseline and minimal ceremony | Start with [**path A**](adopting-blueprints-path-a.md) |
| You must align several contributors or repos on vocabulary and ceremonies | [**Path B**](adopting-blueprints-path-b.md) after **A**’s basics |
| You maintain a platform corpus and many products must pin the same upstream | [**Path C**](adopting-blueprints-path-c.md) (often with governance for submodule bumps) |

### Path choice (visual)

The decision guide above maps three situations to paths A, B, and C. Use it before deep-reading methodology folders.

```blueprint-diagram
key: decision
alt: Adoption path choice — match your situation to path A, B, or C from the table above
```

## What changes vs what stays frozen

| Area | What you add or own in *your* repo | What stays upstream (do not fork casually) |
|------|-------------------------------------|--------------------------------------------|
| Interpretations, principles, “how we run it” | Project **`sdlc/`**, **`docs/`**, optional **`forge/`** | **`blueprints/sdlc/`** baseline text — see [Policy](POLICY.md) |
| Tooling and editor alignment | Cursor rules, optional Forge tasklets — see [SETUP](SETUP.md) | Templates in **`blueprints/`** you **copy** or sync; not edited in place for product specifics |
| Submodule pointer | Your commit moves **`blueprints/`** to a new SHA | Upstream **`autowww/blueprints`** remains the canonical framework |

## Risks and trade-offs (chooser)

| Path | Main trade-off | Mitigation |
|------|----------------|------------|
| **A** | Too little shared process if the team grows | Move to **B** when you need shared ceremony language |
| **B** | Heavier alignment cost | Anchor one repo; use [Team rollout](team-rollout.md) patterns |
| **C** | Submodule drift across products | Published “golden” SHA + cadence; see [Updating the submodule](updating-blueprints-submodule.md) |

## Choose your path (deep dives)

| Path | Page |
|------|------|
| **A** — Solo developer or small team | [Adopting Blueprints — path A](adopting-blueprints-path-a.md) |
| **B** — Team lead / EM | [Adopting Blueprints — path B](adopting-blueprints-path-b.md) |
| **C** — Organization / platform group | [Adopting Blueprints — path C](adopting-blueprints-path-c.md) |

## How to verify success

You have picked a path and can follow that path’s **Steps** page. Next, confirm repo checks in [first hour](quickstarts/first-hour.md) or [Project setup profile](SETUP.md).

## What to do next

- [Quickstarts hub](quickstarts/README.md)
- [First hour](quickstarts/first-hour.md) (~60 minutes)
- [Project setup profile](SETUP.md)
- [Troubleshooting and FAQ](troubleshooting-faq.md)
- [Updating the submodule](updating-blueprints-submodule.md)
- [Team rollout patterns](team-rollout.md)

---

## Maintainer and GitHub-only detail

Release notes and framework-product context live on GitHub (for example [ADOPTION.md](https://github.com/autowww/blueprints/blob/main/docs/ADOPTION.md), [ROADMAP.md](https://github.com/autowww/blueprints/blob/main/docs/ROADMAP.md)). Skip this block until you need upstream or release mechanics.
