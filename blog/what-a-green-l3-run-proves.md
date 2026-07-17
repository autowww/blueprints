---
title: What a Green L3 Run Proves (and Doesn't)
meta_description: "Example 7 from bounded execution: a demonstrated L3 use-case slice is evidence-backed scope—not full app autonomy."
---

# What a Green L3 Run Proves (and Doesn't)

Forge recently published **Example 7** in the [bounded execution examples](https://blueprints.forgesdlc.com/sdlc--methodologies-forge-bounded-execution-examples.html) handbook page—a green **L3 use-case slice** run from the `lenses-production-l3-ci` campaign. This post explains what that evidence actually means for adopters evaluating unattended agent delivery.

## What L3 claims

At **L3**, the autonomous unit is an **end-to-end user-visible flow** inside one existing app: logic, docs, and UI layers touched, with end-to-end verification. Architecture and platform stay fixed. Humans supply **intent and acceptance criteria in**; they **review out**.

That is a meaningful step up from **L2**, where the unit is a multi-file change-set without requiring cross-layer or E2E proof.

## What Example 7 did

The `L3-ui-smoke` campaign item targeted a sandbox **docs-health** app:

| Aspect | Value |
|--------|-------|
| Plan | 3 patch units across layers: `logic`, `docs`, `ui` |
| Files changed | `app/scanner.py`, `README.md`, `ui/index.html` |
| E2E | `verify-docs-health-l3.py` recorded in `tests_run` |
| Result | `final_status: pass`, `escalated: false` |

The assay gate enforced L3-specific rules: **≥2 distinct layers**, **both** `.py` and non-`.py` files in the proof union, and **E2E pass** in the test record—not merely “three files changed.”

## What it proves

1. **The ladder is enforceable in code** — L3 is not only a policy table row; `assay_gate.py` rejects passes that lack cross-layer and E2E evidence.
2. **A use-case slice can be decomposed** — three ordered patch units, each applied and verified, then aggregated proof.
3. **Machine records are auditable** — dual-wiki trace (machine JSON + generated human report) supports back-tracing without hand-edited narratives.

Teams evaluating Forge Dark Factory (PoC) can treat this as **demonstrated** L3—not “foundation only.”

## What it does not prove

- **Production app autonomy** — the target was a PoC sandbox, not a live product repo with promotion to main.
- **L4+ capability** — no multi-repo Campaign, ADR gate, or release gate was exercised.
- **Unsupervised ship** — the run stops at evidenced pass; merge and release remain human decisions.
- **Cloud-free delivery at scale** — local-first routing still applies; L2–L3 often needs ROI-gated escalation to larger models or humans at pivots.

Do not read a green L3 run as “our agent owns the product.” Read it as “we can bound and evidence a **single use-case slice** inside fixed architecture.”

## How to read the handbook cluster

This example sits in a deliberate reading order:

1. [Respecting resources](https://blueprints.forgesdlc.com/sdlc--methodologies-forge-respecting-resources.html) — scarce vs abundant, decompose before escalate
2. [Autonomy levels](https://blueprints.forgesdlc.com/sdlc--methodologies-forge-autonomy-levels.html) — canonical L0–L8 policy
3. [Bounded execution examples](https://blueprints.forgesdlc.com/sdlc--methodologies-forge-bounded-execution-examples.html) — Examples 1–7 with diagrams
4. [Platform autonomy hub](https://platform.forgesdlc.com/docs-autonomy-levels-index.html) — readiness matrix and [L3 building blocks](https://platform.forgesdlc.com/docs-autonomy-levels-l3-use-case-slice.html)

## Go deeper

- [Example 7 in the handbook](https://blueprints.forgesdlc.com/sdlc--methodologies-forge-bounded-execution-examples.html#example-7--l3-use-case-slice-across-logic-docs-and-ui)
- [L3 — Use-case slice (Platform)](https://platform.forgesdlc.com/docs-autonomy-levels-l3-use-case-slice.html)
