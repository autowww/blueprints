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
   - The website [blueprints.forgesdlc.com](https://blueprints.forgesdlc.com) is rebuilt from `generator/build-handbook.py`.
   - The [GitHub Wiki](https://github.com/autowww/blueprints/wiki) is synced via `wiki-source/sync-wiki.sh`.
   - See [`docs/DESIGN-PRINCIPLES.md`](docs/DESIGN-PRINCIPLES.md) for documentation standards including the 101/201/301 tiering model.
   - Add frontmatter metadata (`tier`, `surfaces`, `cross_refs`) to new `.md` files.

3. **Prefer small, focused changes** (one logical fix or improvement per PR) so reviewers can reason about impact.

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
