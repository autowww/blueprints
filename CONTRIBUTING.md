# Contributing

Thanks for helping improve these blueprints.

## Before you open a PR

1. **Read the package policy** for the area you touch:
   - [`sdlc/POLICY.md`](sdlc/POLICY.md)
   - [`docs/POLICY.md`](docs/POLICY.md)
   - [`agents/POLICY.md`](agents/POLICY.md) (if applicable)

   Blueprint text is meant to stay **product-agnostic** and **stable**. Avoid slipping in names, stacks, or living project data from a single product repo.

2. **Keep Markdown and handbook in sync** where required:
   - After substantive changes under `sdlc/`, update the HTML handbook under `sdlc/docs/` per [`sdlc/docs/MAINTENANCE.md`](sdlc/docs/MAINTENANCE.md).
   - Same idea for `docs/docs/` and `agents/docs/` when those packages change—see each folder’s `MAINTENANCE.md`.

3. **Prefer small, focused changes** (one logical fix or improvement per PR) so reviewers can reason about impact.

## How to contribute

1. Fork the repository and create a branch from `main`.
2. Make your changes; run any local checks you normally use (e.g. validate links, regenerate static assets if your change requires it).
3. Open a pull request with a short summary and, if non-obvious, rationale and tradeoffs.
4. Respond to review feedback; maintainers may merge when the change fits blueprint scope and quality.

## Wiki mirror

If you maintain the [GitHub Wiki](https://github.com/autowww/blueprints/wiki), refresh it after merging Markdown changes using [`wiki-source/sync-wiki.sh`](wiki-source/sync-wiki.sh) (see [`wiki-source/README.md`](wiki-source/README.md)).

## Code of conduct

All participants are expected to follow the [Code of Conduct](CODE_OF_CONDUCT.md).
