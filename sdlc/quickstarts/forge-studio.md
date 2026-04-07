# Forge Studio quickstart

## What it is

A short path (~**15–30 minutes** after Git and Python 3 are available) to a local **[forge-lenses](https://github.com/autowww/forge-lenses)** checkout, the Python server running, and **Forge Studio** (Lenses Studio) at **`/studio/`** in the browser.

**Guides:** [Lenses, Studio, and Wizard](https://blueprints.forgesdlc.com/lenses/index.html) on the handbook site — next to this Blueprints content.

**Contributors and operators:** advanced setup and troubleshooting for the **forge-lenses** repo are documented [on GitHub](https://github.com/autowww/forge-lenses/blob/main/README.md) and in [Studio quickstart — maintainer notes](https://github.com/autowww/blueprints/blob/main/docs/studio-quickstart-maintainer.md).

## When to use it

Use this quickstart after [first hour](first-hour.md) (or equivalent) when you want the **local workspace UI** and **Forge Studio** — not when you only need Markdown in `blueprints/` without Lenses.

## Prerequisites

- **Git**, **Python 3**, **pip** (venv recommended).

## Steps

### 1. Get the repository

**Standalone clone** (typical — sibling to your product repos):

```bash
git clone https://github.com/autowww/forge-lenses.git
cd forge-lenses
```

**Git submodule** (from a parent folder that contains your workspace):

```bash
git submodule add https://github.com/autowww/forge-lenses.git forge-lenses
git submodule update --init --recursive
cd forge-lenses
```

Then run `./scripts/setup.sh` for nested submodules (blueprints, kitchensink) as described in the [forge-lenses README](https://github.com/autowww/forge-lenses/blob/main/README.md).

### 2. Install Python dependencies

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

### 3. Run the server

```bash
./scripts/run-lenses.sh
```

Or: `.venv/bin/python3 -m lenses` from the repo root with the same venv activated.

### 4. Open Forge Studio

Open **[http://127.0.0.1:8080/studio/](http://127.0.0.1:8080/studio/)** (default port **8080**).

If the page does not load, you may need a one-time front-end build from the **forge-lenses** repository; see [maintainer notes](https://github.com/autowww/blueprints/blob/main/docs/studio-quickstart-maintainer.md).

### 5. Blueprints Wizard (optional)

**Blueprints Wizard** is an optional guided flow inside Forge Studio. It helps draft methodology-aligned packs; it does **not** edit the **`blueprints/`** git submodule.

- **Guides:** [Wizard overview](https://blueprints.forgesdlc.com/lenses/guides/08-wizard-overview.html) · [Lenses overview](https://blueprints.forgesdlc.com/lenses/guides/01-lenses-overview.html)

## How to verify success

- [http://127.0.0.1:8080/](http://127.0.0.1:8080/) loads (classic UI). JSON: [http://127.0.0.1:8080/api/workspace-state](http://127.0.0.1:8080/api/workspace-state).
- [http://127.0.0.1:8080/studio/](http://127.0.0.1:8080/studio/) loads after any required bundle build (see maintainer notes if needed).

## What to do next

- **First hour with Blueprints** (submodule, `sdlc/`, Forge, Cursor): [First hour in your repo](first-hour.md)
- **ICP adoption paths:** [**Adopting Blueprints**](../adopting-blueprints.md)
- **forge-lenses** upstream: [github.com/autowww/forge-lenses](https://github.com/autowww/forge-lenses)
