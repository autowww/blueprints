---
nav_title: Blueprints quickstarts for repo setup and adoption
nav_group: onboarding
public_publish: true
audience: public
handbook_area: blueprints
learning_level: overview
---

# Blueprints quickstarts for repo setup and adoption

This page is the entry to **quickstarts**: short guided paths with verification. Read the first paragraph under **What it is**, then use **Selection matrix** to pick a path.

## What it is

The fastest path from “Blueprints is in my repo” to **verified** progress — commands and checks, not a methodology tour.

### Terms (quick read)

| Term | Plain language |
|------|----------------|
| **Blueprints** | **Software delivery documentation framework** at repo root (`blueprints/`). |
| **Forge Studio** | **Local engineering workspace dashboard** (Lenses) — optional companion to this handbook. |
| **Wizard** | **Guided planning workflow** inside Studio. |

## When to use it

Use this hub when you are ready to run scripts at the **repository root** next to `blueprints/`. If you are still choosing *how much* process to adopt, read [**Adopting Blueprints**](../adopting-blueprints.md) first.

## Prerequisites

- **Git** and **bash**
- **Python 3** (Forge init and Cursor rule sync)
- A checkout where **`blueprints/`** can live at the repo root (see [SETUP.md](../SETUP.md))

## Selection matrix

| Quickstart | Time (typical) | Outcome | Prerequisite |
|------------|----------------|---------|----------------|
| [**First hour**](first-hour.md) | ~60 min | Submodule, project **`sdlc/`**, **Forge**, **Cursor** rules — verify after each step | Repo root layout decided |
| [**Forge Studio**](forge-studio.md) | ~30–45 min after tooling | Local **forge-lenses** server and **`/studio/`** UI | Git + Python venv; optional after first hour |
| [**Project setup profile**](../SETUP.md) | Multi-session | Full ordered checklist including optional product-led steps | Same root layout; use after first hour or instead of ad hoc steps |

### Who starts where

| You are… | Start with |
|----------|------------|
| Choosing how much to adopt (role / org size) | [**Adopting Blueprints**](../adopting-blueprints.md) |
| Ready to run commands today | [**First hour**](first-hour.md) |
| Standardizing setup for a team or template repo | [**Project setup profile**](../SETUP.md) |
| Wanting Lenses / Studio / Wizard on your machine | [**Forge Studio**](forge-studio.md) after your product repo baseline works |

### Quickstart flow (visual)

```blueprint-diagram
key: board
alt: Adopting Blueprints or first hour first; full setup profile when standardizing; Forge Studio optional for local Studio and Wizard
```

## Steps

Pick one quickstart and follow it end-to-end:

| Quickstart | Outcome |
|------------|---------|
| [**First hour in your repo**](first-hour.md) | `blueprints/` present, project **`sdlc/`** workspace, minimal **Forge** layout, **Cursor** rules — verification after each step |
| [**Forge Studio**](forge-studio.md) | Optional **forge-lenses** clone or submodule, local server, **`/studio/`** UI — companion product, not inside `blueprints/` |

### How this hub fits nearby guides

| If you need… | Use |
|---------------|-----|
| **Which adoption story fits your role** (solo / team / org) | [**Adopting Blueprints**](../adopting-blueprints.md) first |
| **Verified commands only, ~1 hour** | **First hour** above |
| **Full checklist** (submodule through optional product flows) | [**Project setup profile**](../SETUP.md) |
| **Something failed** | [**Troubleshooting / FAQ**](../troubleshooting-faq.md) |

## How to verify success

You completed the chosen quickstart’s **Verify** / **How to verify success** section (see that page) without skipping checks you care about for your team.

## What to do next

- [**Adopting Blueprints**](../adopting-blueprints.md) — ICP-style paths when role context matters
- [**Project setup profile**](../SETUP.md) — full ordered checklist beyond the first hour
- [**Troubleshooting / FAQ**](../troubleshooting-faq.md) — submodule, paths, Forge/Cursor

**Deeper reference (not step 1):** [SDLC blueprint](../README.md), [PDLC](../../pdlc/README.md), [disciplines hub](../../disciplines/README.md) — use after your baseline layout works.