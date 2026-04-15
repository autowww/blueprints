---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Versioning and release notes (consuming repositories)

## What it is

A **single policy** for how product-facing version numbers and **human-readable release history** relate, plus optional **local automation** shipped from Blueprints. Use it for any repo that ships software (SPA, Python package, mobile app, desktop shell) and keeps a **Keep a Changelog**–style `CHANGELOG.md`.

**Canonical automation (optional):** `blueprints/sdlc/methodologies/forge/setup/install-version-release-hook.sh` installs a **post-commit** hook that calls `hooks/version-release-post-commit.py`. The hook is **opt-in** per repository via a committed manifest **`.forge/version-release.json`** at the repository root.

## Principles

1. **Semantic versioning** for anything users or integrators pin — follow [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html) unless a platform forbids it (then document the exception in the repo’s own `VERSIONING.md` or `README`).
2. **One changelog per release line** that matters to humans — usually `CHANGELOG.md` at repo root or next to the versioned artifact (for example `lenses-enterprise/CHANGELOG.md` for Forge Studio).
3. **Build metadata is not semver** — git SHA, build timestamps, and CI build numbers support supportability; they do not replace semver bumps.
4. **No silent semver bumps** — automation shipped here **does not** increase `MAJOR.MINOR.PATCH` on every commit. Maintainers still choose the semver delta when cutting a release; the hook **finalizes** `[Unreleased]` into `[x.y.z]` only when it detects a **committed** bump in a configured version file compared to `HEAD~1`.
5. **Blueprints stays methodology-only** — this file defines policy and tooling entry points; **product-specific** semver tables (for example Studio vs Python server in forge-lenses) live in the **product repo** beside the artifact, and may **link here** for the shared rules.

## Where version lives (by repo shape)

| Product shape | Typical version source | Changelog |
|---------------|-------------------------|-----------|
| **Node / Vite / React** | `package.json` `version` | Adjacent `CHANGELOG.md` or repo root |
| **Python package** | `pyproject.toml` `[project].version` or `__version__` in the package `__init__.py` | Repo root or `docs/` per team |
| **Android** | `versionName` / `versionCode` in Gradle | Play listing + `CHANGELOG.md` |
| **Static site generator** | Optional `package.json` or generator constant | Site “what’s new” or root `CHANGELOG.md` if you ship a versioned kit |

**Multi-surface repositories** (example: Python server + React Studio in one git repo): use **separate semver lines** and separate changelog sections or files when the surfaces ship or break compatibility independently; document the split in a short repo-local `VERSIONING.md`.

## Release workflow (human + optional hook)

1. Merge work under **`## [Unreleased]`** in `CHANGELOG.md` (hook can **append** a bullet from the latest commit subject when watched paths change — see manifest).
2. When cutting a release: bump the version field(s), rename **`[Unreleased]`** to **`[x.y.z] — YYYY-MM-DD`**, and open a fresh **`[Unreleased]`** section (hook can **finalize** the Unreleased block when it detects a semver bump in a configured version file).
3. Tag or publish per your DevOps practice.

**Skip automation for a commit:** put **`[skip-changelog]`** in the commit subject or body. **`[skip-version]`** is accepted as an alias.

**Safety:** the hook skips **merge commits** (two parents) and skips when **`CI`** is set to a non-empty value.

## Reinforcement after Blueprints init or submodule update

1. `git submodule update --init --recursive` (or your routine bump) so `blueprints/sdlc/...` exists.
2. **`./blueprints/sdlc/methodologies/forge/setup/forge-init.sh`** (once per repo) already prints optional next steps; it mentions the **version/release hook** installer.
3. Optionally: **`bash blueprints/sdlc/methodologies/forge/setup/install-version-release-hook.sh`**
4. Add **`.forge/version-release.json`** — start from [`templates/version-release.manifest.example.json`](templates/version-release.manifest.example.json).

## Related

- Example manifest: [`templates/version-release.manifest.example.json`](templates/version-release.manifest.example.json)
- Installer: [`install-version-release-hook.sh`](install-version-release-hook.sh)
- Hook implementation: [`hooks/version-release-post-commit.py`](hooks/version-release-post-commit.py)
