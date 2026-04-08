---
nav_title: Advanced customization
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Advanced customization (consumer view)

## What it is

Where **safe** customization lives in a **consumer** repository — without treating `blueprints/` as an editable scratchpad.

## When to use it

Use this page when you have baseline adoption working ([SETUP.md](SETUP.md)) and need project-specific process, tooling, or docs beyond the frozen submodule.

## Prerequisites

- [First hour](quickstarts/first-hour.md) or equivalent layout in place.
- Familiarity with [Policy](POLICY.md) (frozen baseline vs project space).

## Steps

### Principles

1. **`blueprints/`** — Frozen baseline; changes only per [Policy](POLICY.md) (upstream bumps, deliberate exceptions).
2. **Project `sdlc/`** — Your interpretations, principles, and links into the baseline — created by [`init-sdlc-workspace.sh`](scripts/init-sdlc-workspace.sh) and owned by the product repo.
3. **`docs/`** — Requirements, roadmaps, product docs; structure can follow your org. For a full **consuming-repo** doc tree template, see [`sdlc/DOCUMENTATION-STRUCTURE.md` on GitHub](https://github.com/autowww/blueprints/blob/main/sdlc/DOCUMENTATION-STRUCTURE.md) (maintainer-oriented layout reference).
4. **`forge/`** — Forge config, logs paths, Versona usage — seeded by [forge-init](methodologies/forge/setup/forge-init.sh) and edited for your project.

### Extension points (examples)

| Need | Where to work |
|------|----------------|
| Custom SDLC wording for *this* product | Project `sdlc/` Markdown; link to `blueprints/sdlc/` where useful. |
| Cursor rules and tasklets | `.cursor/` and scripts under `blueprints/.../forge/setup/` **invoked from** your repo root; generated files in `.cursor/rules/`. |
| CI that checks blueprint presence | Your pipeline YAML at repo root; call `test -f blueprints/sdlc/README.md` or run upstream `check` scripts. |
| Extra methodology reading | Consume selectively from `blueprints/sdlc/methodologies/` — do not fork the whole tree unless policy requires it. |

## How to verify success

- A newcomer can still follow [first hour](quickstarts/first-hour.md) without undoing your customizations.
- Submodule updates do not routinely conflict with files **you** own under `sdlc/`, `docs/`, `forge/`.

## What to do next

- [Updating the submodule](updating-blueprints-submodule.md)
- [Troubleshooting / FAQ](troubleshooting-faq.md)