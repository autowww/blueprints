---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Forge SDLC branching charge pack

This pack turns branching adoption into **Forge-native daily Charges**: copy one charge at a time into **`forge/charge.md`** (or run it as a focused session) and execute the Sparks in order.

**Canonical location (blueprints):** this folder — `sdlc/methodologies/forge/setup/charge-plans/branching/`.

**Consuming repo:** copy or symlink the folder to **`forge/charge-plans/branching/`** so paths match the workflow below.

**Non-negotiable:** **do not create `charge/*` Git branches.** [Charge](../../../daily/README.md) is the daily selection layer. It may point at `product/*`, `iter/*`, `spark/*`, `spike/*`, `release/*`, or `hotfix/*`, but it is **never** itself a branch name.

**Policy baseline:** [Git branching and commit conventions (Forge)](../../BRANCHING-STRATEGY.md).

---

## Product Spark (parent context)

| Field | Value |
|-------|--------|
| **ID** | `PS-BRANCH-01` |
| **Name** | Forge-native branching orchestration |
| **Outcome** | A branching policy aligned with Forge planning objects (Ore, Ingot, Spark, iteration, Assay), plus a **Branch Steward** workflow so Cursor performs just-in-time Git actions **without** treating Charge as a branch. |

---

## Iteration plan

### F1 — Profile and policy

**Goal:** Freeze the setup profile that drives branch behavior, map Forge objects to Git, and define promotion rules.

| Charge | File |
|--------|------|
| 01 | [`charge-01-profile-and-baseline.md`](charge-01-profile-and-baseline.md) |
| 02 | [`charge-02-forge-to-git-mapping.md`](charge-02-forge-to-git-mapping.md) |
| 03 | [`charge-03-promotion-and-integration.md`](charge-03-promotion-and-integration.md) |

**Suggested checkpoints**

- Architecture lens on repo topology and submodule or polyrepo impact.
- Governance lens on protected branches and release promotion rules.

---

### F2 — Branch Steward and automation

**Goal:** Define the Branch Steward contract, Cursor behavior, and optional helper scripts or tasklets.

| Charge | File |
|--------|------|
| 04 | [`charge-04-branch-steward-contract.md`](charge-04-branch-steward-contract.md) |
| 05 | [`charge-05-cursor-rule-and-git-actions.md`](charge-05-cursor-rule-and-git-actions.md) |
| 06 | [`charge-06-multi-repo-banking-hotfix.md`](charge-06-multi-repo-banking-hotfix.md) |

**Suggested checkpoints**

- Engineering lens on command safety and branch naming.
- DevOps lens on CI coupling, PR gates, and merge automation.

---

### F3 — Verification and rollout

**Goal:** Exercise the branching model across setup profiles and prepare adoption evidence.

| Charge | File |
|--------|------|
| 07 | [`charge-07-scenario-verification.md`](charge-07-scenario-verification.md) |
| 08 | [`charge-08-rollout-and-assay.md`](charge-08-rollout-and-assay.md) |

**Suggested checkpoints**

- Product or PM lens on rollout clarity.
- Governance lens on final release evidence and migration path.

---

## Default assumptions

Use these unless the project already decided otherwise:

| Dimension | Default |
|-----------|---------|
| Team size | Small team (2–5) |
| Product stage | MVP |
| Iteration length | 1 week |
| Ceremony weight | Standard |
| CI/CD maturity | Standard |
| AI comfort | Advanced |
| Repo topology | Single repo until proven otherwise |

---

## Profile switches

### Solo plus PoC

- Collapse Charges 01–03 into one shorter pass.
- Skip the Product Spark **parent** branch unless the repo is risky or long-running.
- Keep most work on the **iteration** branch.
- Use dedicated `spark/*` branches only for risky `build:` or `verify:` work.

### Team or multi-team

- Run all eight charges.
- Enable Product Spark **parent** branch when work spans multiple iterations, teams, or repos.
- Require PR-based promotion into `iter/*`, then from `iter/*` into parent or `main` (as documented in charge 03).

### Polyrepo or submodule-based

- Run [`optional-spikes.md`](optional-spikes.md) first, especially the topology spike.
- Mirror Product Spark and iteration branch names across touched repos.
- Treat manifest or submodule pin updates as explicit **Forge Sparks**, not implicit side effects.

### CI/CD basic or none

- Keep human review explicit.
- Replace automated merge assumptions with manual checklists and **Ember Log** evidence.

### CI/CD advanced

- Add branch protection, required checks, and release gating during Charges 03, 05, and 08.

---

## How to use in Cursor

1. Keep this folder at **`forge/charge-plans/branching/`** in the consuming repo (copy from blueprints or submodule path).
2. Copy **one** charge file body into **`forge/charge.md`** as the day’s Spark list, or work the charge as a checklist alongside Charge.
3. Paste [`CURSOR-PREAMBLE.md`](CURSOR-PREAMBLE.md) into the first Cursor message for the session.
4. Work active Sparks in order; update statuses and **Ember Log** / journal as your team defines.
5. When a Spark is **blocked**, use **Banking** (see [Charge template](../../../daily/charge.template.md)) instead of inventing a new branch **type**.

---

## File list

| File | Purpose |
|------|---------|
| [`README.md`](README.md) | This pack overview |
| [`CURSOR-PREAMBLE.md`](CURSOR-PREAMBLE.md) | Session opener for Cursor |
| [`optional-spikes.md`](optional-spikes.md) | Run only when genuine unknowns remain |
| [`charge-01-profile-and-baseline.md`](charge-01-profile-and-baseline.md) | F1 — profile |
| [`charge-02-forge-to-git-mapping.md`](charge-02-forge-to-git-mapping.md) | F1 — mapping |
| [`charge-03-promotion-and-integration.md`](charge-03-promotion-and-integration.md) | F1 — promotion |
| [`charge-04-branch-steward-contract.md`](charge-04-branch-steward-contract.md) | F2 — steward |
| [`charge-05-cursor-rule-and-git-actions.md`](charge-05-cursor-rule-and-git-actions.md) | F2 — Cursor + git |
| [`charge-06-multi-repo-banking-hotfix.md`](charge-06-multi-repo-banking-hotfix.md) | F2 — multi-repo |
| [`charge-07-scenario-verification.md`](charge-07-scenario-verification.md) | F3 — scenarios |
| [`charge-08-rollout-and-assay.md`](charge-08-rollout-and-assay.md) | F3 — rollout |

---

## Related

- [Work unit hierarchy](../../../process-and-flows.md#2-work-unit-hierarchy)
- [Naming reference](../../../NAMING-REFERENCE.md)
- [Setup and adoption](../../README.md)
