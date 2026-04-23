# Contributing

Thanks for helping improve these blueprints.

## Before you open a PR

1. **Read the package policy** for the area you touch:
   - [`sdlc/POLICY.md`](sdlc/POLICY.md)
   - [`product/POLICY.md`](product/POLICY.md)
   - [`agents/POLICY.md`](agents/POLICY.md) (if applicable)

   Blueprint text is meant to stay **product-agnostic** and **stable**. Avoid slipping in names, stacks, or living project data from a single product repo.

2. **Markdown is the source of truth**:
   - Edit `.md` files directly. HTML is generated automatically by CI when changes are pushed to `main`.
   - The website [blueprints.forgesdlc.com](https://blueprints.forgesdlc.com) is rebuilt from **`generator/build-handbook.py`** in the **[blueprints-website](https://github.com/autowww/blueprints-website)** repo (this repo is the Markdown source; run the generator from the consumer checkout).
   - The [GitHub Wiki](https://github.com/autowww/blueprints/wiki) is synced via `wiki-source/sync-wiki.sh`.
   - See [Documentation design principles](https://github.com/autowww/blueprints/blob/main/docs/DESIGN-PRINCIPLES.md) for **public handbook** rules: `public_publish`, `audience`, `tier`, `nav_group`, `product_area`, optional `nav_title`.
   - If your change targets **blueprints.forgesdlc.com**, set **`public_publish: true`** only when the page is user-oriented and allowed by §4–§5 of DESIGN-PRINCIPLES; otherwise use `public_publish: false` or rely on manifest exclusions in **blueprints-website**.

3. **Prefer small, focused changes** (one logical fix or improvement per PR) so reviewers can reason about impact.

## Git branching & commits (Forge Team tier)

This repository uses the **Forge SDLC Team** tier (5–12 people): short-lived branches, integration via **pull request** into `main`, review before merge, and CI when configured. Canonical detail: [`sdlc/methodologies/forge/setup/BRANCHING-STRATEGY.md`](sdlc/methodologies/forge/setup/BRANCHING-STRATEGY.md) · [Handbook copy](https://blueprints.forgesdlc.com/sdlc--methodologies-forge-setup-branching-strategy.html).

### Branching

- **Default branch:** `main`.
- **Work branches:** `feature/<short-topic>` or `fix/<short-topic>` from `main`; keep them short-lived.
- **Merge:** through **pull requests** to `main` (no direct pushes to `main` once branch protection is enabled).

#### Forge-native lanes (optional)

The [branching charge pack](sdlc/methodologies/forge/setup/charge-plans/branching/README.md) describes optional `product/*`, `iter/*`, `spark/*`, and related lanes for product repos using **Branch Steward** and daily **Charge**. **This repository** uses the Team-tier names above (`feature/*`, `fix/*`) unless maintainers explicitly adopt the lane pack for framework work.

### Commit scopes (Conventional Commits–lite)

Use `type(scope): summary` where it helps history search. Common **scopes** in this repo: `sdlc`, `disciplines`, `agents`, `pdlc`, `product`, `docs`, `wiki`, `templates`, `wiki-source`. Use **`chore(scope):`** for mechanical or generated-only edits. Do not treat **embedded submodules** as the place to land upstream work—edit the standalone repository and bump the submodule pointer here in a separate commit.

### GitHub branch protection (maintainers)

For the `main` branch, configure **Rulesets** or **classic branch protection** to match org policy. Typical settings:

1. Require a pull request before merging; require at least **one** approval (adjust if your org differs).
2. Require **status checks** to pass when `.github/workflows/` defines jobs that run on `pull_request` (match exact job IDs in the workflow files).
3. Block force-push and deletion on `main`.

This repo may rely on **organization-level** CI; align required checks with whatever runs on PRs for `autowww/blueprints`.

## How to contribute

1. Fork the repository and create a branch from `main`.
2. Make your changes; run any local checks you normally use (e.g. validate links).
3. Open a pull request with a short summary and, if non-obvious, rationale and tradeoffs.
4. Respond to review feedback; maintainers may merge when the change fits blueprint scope and quality.

## Documentation surfaces

This repo feeds three documentation surfaces:

| Surface | URL | Lens |
|---------|-----|------|
| GitHub Wiki | [autowww/blueprints/wiki](https://github.com/autowww/blueprints/wiki) | Quick engineering reference |
| blueprints.forgesdlc.com | [blueprints.forgesdlc.com](https://blueprints.forgesdlc.com) | Framework documentation |
| forgesdlc.com | [forgesdlc.com](https://forgesdlc.com) | Methodology product (built from the `forgesdlc` repo) |

## Wiki mirror

If you maintain the [GitHub Wiki](https://github.com/autowww/blueprints/wiki), refresh it after merging Markdown changes using [`wiki-source/sync-wiki.sh`](wiki-source/sync-wiki.sh) (see [`wiki-source/README.md`](wiki-source/README.md)).

## Code of conduct

All participants are expected to follow the [Code of Conduct](CODE_OF_CONDUCT.md).
