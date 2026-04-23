---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
nav_title: Blueprint policy
---

# Blueprint policy

**Do not change the blueprint baseline casually.** The tree under **`blueprints/`** (including **`blueprints/sdlc/`**) is a **shared baseline**: generic process and documentation conventions you **reuse** across projects. It is not your day-to-day project scratch space.

## Rules

1. **Do not edit** files under **`blueprints/`** for normal product work — features, product requirements, roadmap notes, WBS updates, or team-specific wording.
2. **Put project work** in **`sdlc/`** (this repository’s project SDLC workspace) and **`docs/`** (requirements, roadmap, profiles, and other product documentation) unless your runbook says otherwise.
3. **Change the baseline** only when you deliberately move to a **new upstream version** (for example by **bumping the git submodule** to a new commit), fix something **with upstream**, or follow an explicit maintainer decision — not as a shortcut during a story or ticket.

## Relationship to `sdlc/`

| Location | Role |
|----------|------|
| **`blueprints/sdlc/`** | Canonical, generic text — **frozen by convention** for consumers of this repo. |
| **`sdlc/`** (repo root) | Where **this project** links, interprets, and extends the lifecycle **without** editing the submodule’s files in place. |

**Copying this layout:** You may copy **`blueprints/`** (or **`blueprints/sdlc/`**) wholesale into another repository. Use a project-level **`sdlc/`** (or equivalent) there for **repository-specific** SDLC notes.

## Updating the baseline pointer

To adopt a newer Blueprints release or move the submodule safely, use the handbook runbook **[Updating the Blueprints submodule](updating-blueprints-submodule.md)**. If something went wrong after a bump, **[Troubleshooting and FAQ](troubleshooting-faq.md)** is the right next step.
