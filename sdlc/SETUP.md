---
nav_title: Project setup profile
nav_group: onboarding
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Project setup profile (consuming repository)

## What it is

The **full ordered checklist** for a product repository that hosts **`blueprints/` at the repository root** (typically a git submodule): submodule through optional Forge and product-led flows, with the same assumptions as the [first-hour quickstart](quickstarts/first-hour.md), but in one place.

You may copy this file to your project root as `SETUP.md` if you want a local checklist.

| Field | Value |
|-------|--------|
| **Profile version** | 1.0 |
| **Last reviewed** | 2025-03-24 |
| **Blueprints submodule** | Record `git rev-parse HEAD` inside `blueprints/` after `git submodule update` |

**Layout reference:** full consuming-repo doc tree (optional detail) — [`DOCUMENTATION-STRUCTURE.md` on GitHub](https://github.com/autowww/blueprints/blob/main/sdlc/DOCUMENTATION-STRUCTURE.md).

### Setup phases (map of the numbered steps)

| Phase | Steps | Page |
|-------|-------|------|
| **Bootstrap** | 1–3 | [Setup profile — Bootstrap](setup-profile-bootstrap.md) |
| **Forge + Cursor + automation** | 4–11 | [Setup profile — Forge and Cursor](setup-profile-forge-cursor.md) |
| **Product-led (optional)** | 12 | [Setup profile — Optional product-led](setup-profile-optional-product.md) |

**Depth profiles:** **Minimum** = Bootstrap + Forge through a working `forge.config.yaml`. **Recommended** = through step 10 (`sync-forge-cursor-rules.sh check` clean). **Full** = all rows including optional product-led flows.

### Setup phases (visual)

```blueprint-diagram
key: checklist
alt: Project setup profile — Bootstrap, then Forge and Cursor, then optional product-led steps
```

## When to use it

Use this page when you are **standardizing setup end-to-end** after you already know you will use Blueprints at the repo root.

**Before you start:** if you have not chosen an adoption story yet, skim [**Adopting Blueprints**](adopting-blueprints.md). For a faster guided pass with verification after each step, use [Quickstarts — First hour](quickstarts/first-hour.md) first, then return here for anything you skipped.

## Prerequisites

- **`blueprints/`** must sit at the **repository root** next to `forge/`, `sdlc/`, `docs/`, etc. Scripts such as [`methodologies/forge/setup/forge-init.sh`](methodologies/forge/setup/forge-init.sh) and [`methodologies/forge/tasklets/install-tasklets.sh`](methodologies/forge/tasklets/install-tasklets.sh) use paths like `blueprints/sdlc/...` from the current working directory (repo root).
- If your org cannot use that layout, you need **wrapper scripts** or forks that adjust paths — the stock blueprints tooling does **not** support a configurable `BLUEPRINTS_ROOT`.

## Steps (by phase)

Follow the three pages in order (or jump to the phase you skipped after [first hour](quickstarts/first-hour.md)):

1. [Bootstrap — steps 1–3](setup-profile-bootstrap.md)
2. [Forge and Cursor — steps 4–11](setup-profile-forge-cursor.md)
3. [Optional product-led — step 12](setup-profile-optional-product.md)

## How to verify success

- After Bootstrap: `test -f blueprints/sdlc/README.md` from repo root; project `sdlc/README.md` exists.
- After Forge and Cursor: `sync-forge-cursor-rules.sh check` passes when you use the recommended preset (if applicable).
- After optional product-led: artifacts per the linked methodology docs.

## What to do next

- [`methodologies/forge/setup/README.md`](methodologies/forge/setup/README.md) — adoption entry point  
- [`methodologies/forge/versona/README.md`](methodologies/forge/versona/README.md) — Versona catalog
