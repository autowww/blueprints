---
nav_title: Fast setup and adoption paths
nav_group: onboarding
public_publish: true
audience: public
handbook_area: blueprints
learning_level: overview
description: Short guided paths with verification—from Blueprints in your repo to Forge, Cursor alignment, and optional Studio.
---

# Fast setup and adoption paths

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
- A checkout where **`blueprints/`** can live at the repo root (see [Project setup checklist](../SETUP.md))

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
title: Quickstart selection flow
summary: Choose a bounded onboarding path from this hub based on role, urgency, and whether you need local Studio.
node: Selection matrix
detail: Compare quickstarts by time, outcome, and prerequisite on this page.
more: The matrix links First hour, Forge Studio, and the full Project setup profile so you can match scope before running commands.
node: Root / intake
detail: Confirm repo-root layout and baseline tooling before leaving the hub.
more: Prerequisites are Git, bash, Python 3, and a checkout where blueprints/ can live; read Adopting Blueprints first if process depth is still unclear.
node: branch A
detail: Start with Adopting Blueprints or the First hour quickstart.
more: Use Adopting Blueprints when role or org size drives how much process to adopt; use First hour when you are ready to run verified commands today (~60 min).
node: branch B
detail: Follow the Project setup profile when standardizing team or template repos.
more: SETUP.md is the multi-session ordered checklist beyond the first hour, including optional product-led steps.
node: branch C
detail: Add Forge Studio after your product repo baseline works.
more: The forge-studio quickstart installs optional forge-lenses locally for /studio/ UI and Wizard; it is a companion product, not inside blueprints/.
fallback_ascii: |
  Selection matrix

  Root / intake
      +-- branch A
      +-- branch B
      +-- branch C
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

**Deeper reference (not step 1):** [Software delivery overview](../README.md), [PDLC](../../pdlc/README.md), [disciplines hub](../../disciplines/README.md) — use after your baseline layout works.