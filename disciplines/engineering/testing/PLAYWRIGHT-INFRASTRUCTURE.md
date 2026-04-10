---
slug: discipline-testing-playwright
tier: 201
lens: discipline
nav_section: Disciplines
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Playwright — blueprint infrastructure

**Purpose:** Standard place for **Playwright** adoption in repos that embed [`blueprints/`](../../README.md) as a submodule: copyable templates, bootstrap scripts, container recipe, and workspace-level orchestration. **Runtime dependencies** (`@playwright/test`, lockfile, specs, CI workflows) stay in the **application repository** — not inside the blueprint text tree.

**Audience:** Teams adding **browser E2E** or **Electron shell** automation; DevOps wiring CI.

| Related | Role |
|---------|------|
| [`AUTOMATION-LANDSCAPE.md`](AUTOMATION-LANDSCAPE.md) | Where Playwright sits in the tooling taxonomy |
| [`APPROACHES.md`](APPROACHES.md) | Test levels and pyramid |
| [`../../../sdlc/SDLC.md`](../../../sdlc/SDLC.md) §7 | Quality gates and CI expectations |
| [`../../../sdlc/templates/TEST-PLAN.template.md`](../../../sdlc/templates/TEST-PLAN.template.md) | Automation stack section |
| [`../../../sdlc/templates/playwright/`](../../../sdlc/templates/playwright/) | Config and spec **templates** (copy into your repo) |
| [`../../../sdlc/scripts/README.md`](../../../sdlc/scripts/README.md) | `init-playwright-e2e.sh`, `playwright-workspace-run.sh` |
| [`../../../agents/templates/recipe/playwright-e2e/`](../../../agents/templates/recipe/playwright-e2e/) | Optional Docker recipe template |

---

## 1. Adoption checklist

1. **Choose surface:** Browser (Chromium/Firefox/WebKit) vs **Electron** (`@playwright/test` **Electron** API). Hybrid repos may use both with separate projects or configs.
2. **Install in the app repo** (directory that owns `package.json` for the UI):  
   `npm install -D @playwright/test`  
   then `npx playwright install` (add `--with-deps` on Linux CI for system libraries).
3. **Copy templates** from `blueprints/sdlc/templates/playwright/` into your repo (e.g. `./e2e/`), or run from repo root:  
   `./blueprints/sdlc/scripts/init-playwright-e2e.sh`
4. **Adjust paths** in `playwright.config.*` and specs: `main` entry, `cwd`, and any `baseURL` for web apps.
5. **Add npm scripts**, e.g. `"test:e2e": "playwright test"`.
6. **CI:** Use the GitHub Actions snippet in `github-actions-snippet.md` in the template folder; on Linux runners, **Electron** and headed flows often need **`xvfb-run`** (documented in the snippet).
7. **Document** the gate in `docs/development/` or your test plan ([`TEST-PLAN.template.md`](../../../sdlc/templates/TEST-PLAN.template.md) §8).

---

## 2. Submodule layout

Consuming repos typically have:

```text
your-repo/
  blueprints/          # submodule → autowww/blueprints
  e2e/                 # mutable — your Playwright specs + local config
  package.json         # @playwright/test here (or under packages/foo/)
```

Reference blueprint files by **relative path** from your repo root (e.g. `blueprints/sdlc/templates/playwright/README.md`). Do not commit `node_modules` into blueprints.

---

## 3. Electron vs browser

| Topic | Browser E2E | Electron |
|--------|----------------|----------|
| Entry | `baseURL`, `page.goto` | `electron.launch({ args, cwd, env })`, then `firstWindow()` |
| Binary | Playwright-managed browsers | `electron` package / your packaged app |
| CI | Often headless | May need `xvfb-run` on Linux; many shells use `--no-sandbox` in dev |

**Security:** Do not enable **remote debugging** on end-user builds. Treat debug ports as **development/CI only**.

---

## 4. Workspace-level runs (sibling repos)

If your machine checkouts look like:

```text
~/Code/
  forge-lenses/
  blueprints/          # standalone clone, or each consumer has its own submodule
```

Run Playwright across **multiple** Node packages from a **parent directory** using the script shipped in blueprints:

```bash
export WORKSPACE_ROOT="$HOME/Code"
./forge-lenses/blueprints/sdlc/scripts/playwright-workspace-run.sh \
  forge-lenses/desktop \
  other-repo/frontend
```

Paths are **relative to `WORKSPACE_ROOT`**. The script changes into each directory that contains a `package.json` and runs `npm ci` (fallback: `npm install`), `npx playwright install`, and `npm run test:e2e` when that script exists. Override with `PLAYWRIGHT_WORKSPACE_NPM_SCRIPT` if your script name differs.

---

## 5. Traces, reports, and cost

- **Traces** (`trace: 'on-first-retry'` or `on`) help debug flakes; store CI artifacts for failed jobs only to limit storage.
- **Playwright** itself is open source; recurring **cost** is mostly **CI minutes** and **maintaining selectors**, not per-test licensing.

---

## 6. Optional: agents container

For repeatable Linux environments, copy [`blueprints/agents/templates/recipe/playwright-e2e/`](../../../agents/templates/recipe/playwright-e2e/) into your repo’s mutable `agents/recipes/` and extend the **Playwright-capable** image described in [`blueprints/agents/docker/README.md`](../../../agents/docker/README.md). See [`STRUCTURE.md`](../../../agents/STRUCTURE.md) for frozen vs mutable layers.

---

*Keep product-specific selectors, secrets, and CI YAML in the application repository; keep this file as generic blueprint guidance.*
