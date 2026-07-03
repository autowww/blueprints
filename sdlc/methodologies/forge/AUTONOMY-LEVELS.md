---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Autonomy levels

## Introduction

Autonomy is not binary. Levels are theoretically unbounded; this ladder gives a **meaningful, testable progression** for governed agent execution. Each level is defined by its **unit of autonomous delivery**, **what stays fixed**, and **where humans gate**.

The ladder is extended by two finer axes:

- **[Maturity grades a–d](#maturity-grades-ad)** on every level — how *proven* a level is, from defined policy to operational default.
- **[Sub-levels](#sub-levels-l1l4-band)** in the **L1–L4 band** — named variants of the autonomous unit, each with its own checkable assay evidence.

Use the ladder when scoping unattended runs, PDCA campaigns, wizard sessions, or Dark Factory targets—so teams do not claim more autonomy than their gates and resources support. Per-project observed maturity and scoring: [Autonomy maturity framework](AUTONOMY-MATURITY-FRAMEWORK.md).

## Implementation readiness (summary)

Operator hub and per-level reference architecture (building blocks, evidence, vision): **[Forge Platform autonomy levels](https://platform.forgesdlc.com/docs-autonomy-levels-index.html)**.

| Level | Policy | Grade today | PoC demonstrated |
|-------|--------|-------------|------------------|
| L0 | Defined | a (interactive; grades N/A beyond a) | N/A (interactive) |
| L1 | Defined | b | Yes (L1.1, L1.2 retro-tagged) |
| L2 | Defined | b | Yes (L2.2 retro-tagged) |
| L3 | Defined | b | Yes (L3.1 retro-tagged) |
| L4–L8 | Defined (vision gates) | a | No |

Full readiness matrix, Wizard ↔ execution mapping, and per-level architecture pages live on the Platform hub — this page remains the **canonical policy** table.

## L0–L8 ladder

| Level | Autonomous unit | What stays fixed | Human gate |
|-------|-----------------|------------------|------------|
| L0 Assisted | Suggestions only | Everything | Continuous |
| **L1 Function** | One method/function to a given signature/contract | Architecture, API, tests | Approve branch/merge |
| L2 Change-set | Multi-function / multi-file defect fix or small change, no rearchitecture | Architecture, public contracts | Accept acceptance criteria + merge |
| **L3 Use-case slice** | End-to-end user-visible flow inside one existing app (UI + logic + data + tests) | Existing architecture, single platform | Intent + acceptance in; review out |
| L4 Feature/component | Capability across modules; may add a component within existing architecture; cross-repo, one platform | Platform, major architecture | ADR + release gate |
| L5 Subsystem w/ local arch evolution | Introduces patterns/refactors within a platform | Platform boundary | Architecture decision escalation |
| L6 Product increment | Multi-repo, multi-service on a single cloud/platform | Cloud/platform choice | Go/no-go |
| L7 Multi-cloud / multi-platform solution (max − 1) | A whole engineered solution spanning clouds/platforms | Business framing | Strategic checkpoints |
| L8 (max) Autonomous problem solving | Frames a business/humanity problem and composes L7 solutions as puzzle pieces | Nothing but the goal | Mission definition only |

![Autonomy ladder L0 to L8 with L0 to L3 emphasized as defined and exercised and L4 to L8 muted as future vision](../../docs/assets/methodology-autonomy-ladder-l0-l3.svg)

*L0–L3 are defined and exercised today (L1–L3 are demonstrated in the [worked examples](BOUNDED-EXECUTION-EXAMPLES.md)); L4–L8 remain vision requiring ADRs, go/no-go, and strategic checkpoints. Higher levels add gates and never remove lower-level ones. The diagram shows the flat ladder; the grade and sub-level axes below are not yet drawn.*

## Maturity grades (a–d)

A level number says what a run was **allowed** to change; a grade says how **proven** that level is in practice. Grades apply to **every** level L0–L8 and to each sub-level, and they compose with the ladder rather than replacing it.

| Grade | Name | Meaning | Evidence required |
|-------|------|---------|-------------------|
| **a** | Defined | Policy row + gates documented | Ladder row in this page |
| **b** | Demonstrated | One green run with machine evidence | Assay pass + trace (previously the "Demonstrated" label) |
| **c** | Repeatable | Green over ≥5 runs in a real repo | Campaign history; escalation rate < 40% |
| **d** | Operational | Default mode for that work type | Escalation rate trending down over 30 days + human review sampling |

Grades are **scoped**: a claim names where it holds (for example "L2.2c in forge-lenses" — repeatable cross-file defect fixes in that repo). A grade earned in a sandbox does not transfer to a production repo; re-earn **b** and above per target.

## Sub-levels (L1–L4 band)

Sub-levels give named, testable variants of the autonomous unit where day-to-day progress actually happens. **L0 and L5–L8 stay flat** — sub-dividing suggestions-only or vision-stage levels would add taxonomy without adding checks. Each sub-level exists **only because** it has distinct assay evidence.

| Sub-level | Autonomous unit | Distinct assay evidence |
|-----------|-----------------|-------------------------|
| **L1.1** | Single function against provided tests | Provided test file unchanged, turns green |
| **L1.2** | Function + agent-authored unit tests | New test file in diff; tests pass |
| **L1.3** | Batch of N independent functions in one run | ≥2 function units, each individually verified |
| **L2.1** | Mechanical multi-file (rename / apply-pattern) | ≥2 files with same-shaped hunks; no behavior-test delta |
| **L2.2** | Cross-file defect fix | Pre-existing failing test recorded, turns green; ≥2 files |
| **L2.3** | Small behavior change with new tests | ≥2 files incl. new/changed test; acceptance criteria list |
| **L3.1** | Slice in sandbox app | ≥2 layers, .py + non-.py, registered E2E runner pass |
| **L3.2** | Slice in a production repo on a branch | L3.1 evidence + target repo not in sandbox allowlist |
| **L3.3** | Slice including data/schema migration | L3.2 evidence + migration file + rollback note |
| **L3.4** | Multiple slices under one campaign | ≥2 L3.x-passing items under one campaign id |
| **L4.1** | New component, single repo | New module/dir + ADR draft + release-gate record |
| **L4.2** | Cross-repo change-set with submodule bump | ≥2 repos; submodule pointer commit; per-repo assay pass |
| **L4.3** | Capability with agent-drafted, human-signed ADR | L4.1/4.2 evidence + signed ADR reference |

Sub-levels within a level are **peer variants ordered by typical adoption**, not strictly increasing risk. For example **L4.2** has wider span than **L4.1** but lower architectural risk — a mechanical cross-repo change-set with a submodule bump changes less about the system's shape than introducing a new component in one repo.

## Notation

Claims combine level, sub-level, and grade as `L<level>.<sub><grade>` plus scope:

- **`L2.2c in forge-lenses`** — cross-file defect fixes, repeatable, in that repo.
- **`L3.1b`** — sandbox use-case slice, demonstrated once.
- **`L1b`** (no sub-level) — legacy or aggregate claim at the level grain; valid, but prefer the sub-level form when the evidence identifies one.

Do not confuse execution sub-levels with the Wizard planning enum (`l0_analyst`…`l3_goal_autopilot`), LCDL schema maturity (L0–L4), or standards precedence (L1–L6) — see the [concept map collision register](CONCEPT-MAP.md#term-collision-register).

## Promotion criteria (grade transitions)

- **a → b** — one green run at the declared (sub-)level with a passing Assay gate and machine + human trace.
- **b → c** — ≥5 green runs at the same (sub-)level in the same repo, with **escalation rate < 40%** across those runs (loop escalation to a human, not worker-ladder stepping — see [Respecting resources](RESPECTING-RESOURCES.md#escalation-rate-operator)).
- **c → d** — escalation rate trending down over a 30-day window **and** periodic human review sampling finds no mis-sized claims (an L2 pass that was really an L1 patch, etc.).
- **Demotion** is expected: a spike in escalations or a failed review sample drops the grade one step; grades are observations, not entitlements.

## How a level is enforced

1. A run (or campaign item) declares its **target level** — and, in the L1–L4 band, its **target sub-level**.
2. The **Assay gate** for that level must pass before the change is considered done. Core evidence in `forge/forge.config.yaml` includes `tests_pass`, `acceptance_criteria_met`, and `risks_reviewed`.
3. **Higher levels do not skip lower-level gates**; they add gates (for example ADR + release at L4).
4. At **L2**, multi-file work should produce proof that **two or more distinct files** changed when acceptance criteria require a change-set—not a single-file patch dressed as L2. Sub-level assays go further: **L2.2** additionally requires a **pre-existing failing test** recorded before the fix, and **L3.x** E2E evidence must come from a **registered runner allowlist**, not name matching.
5. When a sub-level is declared, its **distinct assay evidence** (table above) is enforced in addition to the level's core evidence; a run that fails the sub-level check may still be reported at the plain level grain if that level's evidence holds.

## Resource honesty (local-first)

Fully **cloud-free** autonomy above **L1** is not realistic on a ~4GB local model profile: planning, architecture, and ambiguity exceed small-model capability.

| Level band | Realistic local-first posture |
|------------|------------------------------|
| **L0–L1** | Achievable with deterministic routing + local worker + verify/repair |
| **L2–L3** | Often needs **ROI-gated escalation** to a larger model or human at pivots |
| **L4+** | Requires explicit human gates (ADR, go/no-go, strategic checkpoints) regardless of model |

The realistic operating mode is **local-first with ROI-gated escalation**. Track **escalation rate** over time; it should fall as capability cards and deterministic scaffolds improve. See [Respecting resources](RESPECTING-RESOURCES.md).

## Wizard alignment (planning intent)

The **Blueprints Wizard** in Forge Lenses captures planning-time autonomy separately from runtime loops. The `AutonomyLevel` enum includes `l0_analyst`, `l1_drafter`, `l2_stage_autopilot`, and `l3_goal_autopilot`, with `MutationPolicy` describing how far downstream automation may edit artifacts.

Wizard policies **inform prompts and downstream automation**; they do not silently apply upstream edits. Persisted session policies should match the ladder level you intend for execution. Full Wizard ↔ execution mapping: [Platform autonomy levels hub](https://platform.forgesdlc.com/docs-autonomy-levels-index.html).

## Forge Dark Factory (PoC reference implementation)

**Forge Dark Factory** is the current **PoC reference implementation** for bounded autonomous coding—not a production Platform submodule.

![Forge Dark Factory bounded execution loop: classify, route, context, plan, draft, apply, verify, proof, trace, escalate](../../docs/assets/methodology-bounded-execution-loop.svg)

*The governed loop for L1–L3. Verify failures trigger bounded repair; ambiguity or budget exhaustion escalates to a human, who still approves the branch or merge.*

| Aspect | PoC scope today |
|--------|----------------|
| **Target autonomy** | **L1–L3** demonstrated (function, change-set, use-case slice); see [worked examples](BOUNDED-EXECUTION-EXAMPLES.md) |
| **Loop** | Classify → route → context → plan → draft → apply → verify → repair → proof → dual-wiki trace → escalate |
| **Dependencies** | `forge-lcdl` (patch units, verify, repair, proof); `forge-workcells` (optional local worker) |
| **Trace** | Machine record (M) + generated human narrative (H) with freeze gate |
| **Routing** | Deterministic Cynefin × t-shirt × value; decompose before cloud/human escalate |

Do not treat Dark Factory as compliance-ready or as permission for unsupervised push/deploy. It demonstrates how the ladder and [respecting resources](RESPECTING-RESOURCES.md) rules compose in code.

## What we do not claim

- **No unsupervised push/deploy** — Git workflow and release decisions remain human-gated unless your org explicitly automates them with separate policy.
- **No compliance-ready autonomy** — The ladder is engineering governance, not a certification.
- **No “fully autonomous” delivery** — Even L8 assumes mission definition by humans; intermediate levels add explicit gates.
- **Escalation is expected** — Especially for architecture, security, and ambiguous work; a low escalation rate is a goal, not a guarantee on day one.

## Related

- [Autonomy maturity framework](AUTONOMY-MATURITY-FRAMEWORK.md) — per-project observed level, grade, 0–100 score, and recommendations
- [Forge Platform autonomy levels](https://platform.forgesdlc.com/docs-autonomy-levels-index.html) — operator hub, readiness matrix, per-level reference architecture
- [Bounded execution examples](BOUNDED-EXECUTION-EXAMPLES.md) — real L1–L3 runs with loop, PDCA, and dual-wiki diagrams
- [Respecting resources](RESPECTING-RESOURCES.md) — token economics, decompose-before-escalate, bounded loops
- [Cost-aware planning and model tiering](COST-AWARE-PLANNING-AND-MODEL-TIERING.md) — interactive Cursor planning
- [Agentic SDLC](../agentic-sdlc.md) — humans own intent; agents amplify execution
- [Agentic coding standards](../agentic-coding-standards.md) — review capacity and smaller PRs
- [Assay Gate ceremony](ceremonies-prescriptive.md#5-assay-gate-release-readiness)
