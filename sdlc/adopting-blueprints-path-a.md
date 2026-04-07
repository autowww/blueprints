---
nav_title: "Adopting: path A (solo / small team)"
nav_group: onboarding
public_publish: true
audience: public
handbook_area: blueprints
learning_level: overview
---

# Adopting Blueprints — Path A (solo developer or small team)

## What it is

**ICP path A:** a sane default SDLC/PDLC **text baseline** without writing it from scratch.

**Parent page:** [Adopting Blueprints](adopting-blueprints.md) — choose this path when you mainly need baseline text and minimal ceremony.

## When to use it

When the [decision guide](adopting-blueprints.md#decision-guide) points you to path **A**.

## Prerequisites

- Blueprints added to your repo (typically submodule at `blueprints/`). See [Adopting Blueprints](adopting-blueprints.md#prerequisites).

## Steps

**Job to be done:** “I want a sane default SDLC/PDLC text baseline without writing it from scratch.”

| Step | Action | Verify |
|------|--------|--------|
| 1 | Submodule (or copy) Blueprints into `blueprints/`. | `test -f blueprints/sdlc/README.md` |
| 2 | Add a **project** `sdlc/` folder (interpretations, principles) — do **not** edit the copy under `blueprints/sdlc/`; see [Policy](POLICY.md). | `sdlc/README.md` exists after [init script](quickstarts/first-hour.md). |
| 3 | Add `docs/product/` when you need capabilities/journeys (seed from [product templates](../product/templates/README.md)). | Optional; structure matches your product docs needs. |

## How to verify success

Same checks as the **Verify** column above. Then run [First hour](quickstarts/first-hour.md) or [Project setup profile](SETUP.md) for the full checklist.

## What to do next

- [Adopting Blueprints](adopting-blueprints.md) — other paths (B / C)
- [First hour](quickstarts/first-hour.md)
- [Project setup profile](SETUP.md)
