---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
date: YYYY-MM-DD
iteration: PRE-F1
hat: Engineering
---

# Optional exploration spikes for the branching initiative

Run these only if the unknown is **real**. If the answer is already obvious from the repo and team setup, skip the spike and continue with [Charge 01](charge-01-profile-and-baseline.md).

These are **discipline spikes** (learning, evidence), not Forge Sparks — see [DISCIPLINE-SPIKE.md](../../../versona/DISCIPLINE-SPIKE.md). Close with evidence and Ember Log when policy changes.

---

## Spike A — Topology spike

- **Branch or worktree:** `spike/architecture/polyrepo-topology`
- **Run when:** you are unsure whether the ForgeSDLC repo is a single repo, monorepo, polyrepo, or submodule assembly.
- **Questions to answer:**
  - Which repos are source-of-truth versus assembly repos?
  - Do child repos need mirrored Product Spark and iteration names?
  - Does integration happen by merge, manifest update, or submodule SHA bump?
- **Expected output:**
  - `docs/process/repo-topology.md`
  - one recommendation on whether parent `product/*` branches are mandatory
- **Close condition:**
  - promote findings into Charge 01 and Charge 03

---

## Spike B — Governance spike

- **Branch or worktree:** `spike/governance/protected-branch-gates`
- **Run when:** branch protection, audit, or regulated approvals are unclear.
- **Questions to answer:**
  - Which branches must be protected?
  - Which checks are required before merge?
  - Who approves release or hotfix promotion?
- **Expected output:**
  - `docs/process/branch-protection-matrix.md`
  - one policy note for Charge 03 and Charge 08
- **Close condition:**
  - protections and approvals are concrete enough to encode

---

## Spike C — CI and merge automation spike

- **Branch or worktree:** `spike/devops/merge-automation`
- **Run when:** you do not know whether CI can enforce the policy or whether Branch Steward must stay mostly manual.
- **Questions to answer:**
  - Which checks already exist on push or PR?
  - Can merge queues, required checks, or auto-merge be used?
  - Where do release and hotfix checks differ?
- **Expected output:**
  - `docs/process/ci-gates.md`
  - a yes or no decision on scriptable promotion
- **Close condition:**
  - CI maturity is clear enough to finish Charges 03, 05, and 08

---

## Related

- [Branching charge pack README](README.md)
- [BRANCHING-STRATEGY.md](../../BRANCHING-STRATEGY.md)
