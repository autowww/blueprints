---
nav_title: Forge Studio quickstart
nav_group: onboarding
public_publish: true
audience: public
handbook_area: blueprints
learning_level: overview
---

# Forge Studio quickstart

## What it is

**Forge Studio** is the browser UI for **forge-lenses** at **`/studio/`** on your local server: workspace visibility, Forge plan surfaces, and (when available) the **Blueprints Wizard** for guided sessions. The same Python process also serves the classic dashboard at `/`.

### Terms (quick read)

| Term | Plain language |
|------|----------------|
| **Forge Studio** | **Local workspace UI** for delivery visibility — multi-repo overview, plans, Studio flows. |
| **Lenses** | The **local server + Classic dashboard** that hosts Studio and Wizard on your machine. |
| **Wizard** | **Guided project planning / assessment workflow** inside Studio. |

Companion tutorials on the handbook site: **[Lenses, Forge Studio, and the Blueprints Wizard](https://blueprints.forgesdlc.com/lenses/index.html)**.

## Handbook-only reading vs running Forge Studio

| Mode | Best when | You get |
|------|-----------|---------|
| **Handbook only** | Learning methodology text, onboarding, or quickstarts in the browser | Published guides at [blueprints.forgesdlc.com](https://blueprints.forgesdlc.com/) — no local server |
| **Forge Studio (local)** | You want workspace visibility, Studio flows, and optional Wizard sessions on your machine | **forge-lenses** server — `/studio/` UI at `http://127.0.0.1:8080/studio/` |

### From clone to Studio (visual)

```blueprint-diagram
key: linear
alt: Forge Studio quickstart — clone forge-lenses, venv and dependencies, run server, open /studio/
```

## When to use it

Use this quickstart after [**First hour in your repo**](first-hour.md) (or equivalent) when you want the **forge-lenses** app with **Forge Studio** — not when you only need Blueprints Markdown in your product repo without running Lenses.

## Prerequisites

- **Git**
- **Python 3** and **pip** (use a **venv** for the steps below)

## Steps

### 1. Get forge-lenses

**Standalone clone** (typical — sibling to your product repos):

```bash
git clone https://github.com/autowww/forge-lenses.git
cd forge-lenses
```

**Git submodule** (from a parent workspace that should contain the repo):

```bash
git submodule add https://github.com/autowww/forge-lenses.git forge-lenses
git submodule update --init --recursive
cd forge-lenses
```

Unusual clone layouts (extra submodules, custom scripts): use the handbook [Troubleshooting](https://blueprints.forgesdlc.com/lenses/guides/12-troubleshooting.html) first; only open the **forge-lenses** repository docs if whoever maintains your server tells you to.

### 2. Create a venv and install dependencies

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

### 3. Run the server

From the **forge-lenses** repo root:

```bash
./scripts/run-lenses.sh
```

Or activate the venv and run **`.venv/bin/python3 -m lenses`** (same as the script).

### 4. Open Forge Studio

In your browser, open **[http://127.0.0.1:8080/studio/](http://127.0.0.1:8080/studio/)** (default port **8080**).

If the page does not load, use the handbook **[Troubleshooting](https://blueprints.forgesdlc.com/lenses/guides/12-troubleshooting.html)** end to end. Maintainer-only details stay in the **forge-lenses** project repository — not required for the default quickstart path.

### 5. Optional: open the Blueprints Wizard

The **Blueprints Wizard** is an optional guided flow **inside** Forge Studio. It helps you work through methodology-aligned sessions; it does **not** change your **`blueprints/`** git submodule automatically.

- **Where to open it:** start from **`/studio/`**, then use the Wizard entry points described in the handbook — the hub lives at **`/studio/blueprints/wizard`** (sessions use URLs under that path).
- **Public guides:** [Wizard overview](https://blueprints.forgesdlc.com/lenses/guides/08-wizard-overview.html) · [Wizard 101](https://blueprints.forgesdlc.com/lenses/guides/09-wizard-101.html)

## Example first session (generic)

| | |
|--|--|
| **Starting situation** | Server shows the dashboard at `/`; you want to confirm Studio loads and see one workspace. |
| **Action taken** | Open `/studio/`, pick the workspace root you configured, navigate to an overview or project card you expect. |
| **Expected result** | Studio shell loads without console errors; project list matches folders under your workspace root ([Workspace setup](https://blueprints.forgesdlc.com/lenses/guides/03-workspace-setup.html)). |
| **What to check** | If the list is empty, re-check root path and permissions in [Workspace setup — scan and host](https://blueprints.forgesdlc.com/lenses/guides/03-workspace-setup_03-scan-host.html). |

## Example recurring use (generic)

| | |
|--|--|
| **Starting situation** | Lenses already runs daily; you need a quick scan of plan or knowledge across repos. |
| **Action taken** | Use **Classic** `/` for fast health and links; open **Studio** `/studio/` when you need flows that only exist in the newer UI. |
| **Expected result** | Same server — you choose Classic vs Studio by job, not by reinstalling. |
| **What to check** | Port and host match [Install and run](https://blueprints.forgesdlc.com/lenses/guides/02-install-and-run.html); bookmark both `/` and `/studio/`. |

## How to verify success

| Check | Expect |
|-------|--------|
| Classic UI | **[http://127.0.0.1:8080/](http://127.0.0.1:8080/)** loads |
| Forge Studio | **[http://127.0.0.1:8080/studio/](http://127.0.0.1:8080/studio/)** loads |

**Just Studio vs Studio + Wizard later:** this quickstart covers the server and `/studio/`. Wizard URLs live under `/studio/blueprints/wizard` when you are ready — see the [Lenses handbook Wizard guides](https://blueprints.forgesdlc.com/lenses/index.html).

## What to do next

- **Blueprints first hour** (submodule, `sdlc/`, Forge, Cursor): [First hour in your repo](first-hour.md)
- **Adoption paths:** [Adopting Blueprints](../adopting-blueprints.md)
- **Full checklist:** [Project setup profile](../SETUP.md)
- **Help:** [Troubleshooting / FAQ](../troubleshooting-faq.md)
- **Lenses & Wizard tutorials:** [Lenses hub](https://blueprints.forgesdlc.com/lenses/index.html)