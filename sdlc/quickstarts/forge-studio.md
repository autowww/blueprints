---
nav_title: Forge Studio quickstart
nav_group: onboarding
---

# Forge Studio quickstart

## What it is

**Forge Studio** is the browser UI for **forge-lenses** at **`/studio/`** on your local server: workspace visibility, Forge plan surfaces, and (when available) the **Blueprints Wizard** for guided sessions. The same Python process also serves the classic dashboard at `/`.

Companion tutorials on the handbook site: **[Lenses, Forge Studio, and the Blueprints Wizard](https://blueprints.forgesdlc.com/lenses/index.html)**.

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

If the repository’s [README](https://github.com/autowww/forge-lenses/blob/main/README.md) describes a setup script or submodules for your layout, follow that next.

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

If the page does not load, use the **Troubleshooting** section of the [forge-lenses README](https://github.com/autowww/forge-lenses/blob/main/README.md) on GitHub.

### 5. Optional: open the Blueprints Wizard

The **Blueprints Wizard** is an optional guided flow **inside** Forge Studio. It helps you work through methodology-aligned sessions; it does **not** change your **`blueprints/`** git submodule automatically.

- **Where to open it:** start from **`/studio/`**, then use the Wizard entry points described in the handbook — the hub lives at **`/studio/blueprints/wizard`** (sessions use URLs under that path).
- **Public guides:** [Wizard overview](https://blueprints.forgesdlc.com/lenses/guides/08-wizard-overview.html) · [Wizard 101](https://blueprints.forgesdlc.com/lenses/guides/09-wizard-101.html)

## How to verify success

- **[http://127.0.0.1:8080/](http://127.0.0.1:8080/)** loads (classic Lenses UI).
- **[http://127.0.0.1:8080/api/workspace-state](http://127.0.0.1:8080/api/workspace-state)** returns JSON when the server is healthy.
- **[http://127.0.0.1:8080/studio/](http://127.0.0.1:8080/studio/)** loads.

## What to do next

- **Blueprints first hour** (submodule, `sdlc/`, Forge, Cursor): [First hour in your repo](first-hour.md)
- **Adoption paths:** [Adopting Blueprints](../adopting-blueprints.md)
- **Full checklist:** [Project setup profile](../SETUP.md)
- **Help:** [Troubleshooting / FAQ](../troubleshooting-faq.md)
- **Lenses & Wizard tutorials:** [Lenses hub](https://blueprints.forgesdlc.com/lenses/index.html)
