---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Autonomy levels

## Introduction

Autonomy is not binary. Levels are theoretically unbounded; this ladder gives a **meaningful, testable progression** for governed agent execution. Each level is defined by its **unit of autonomous delivery**, **what stays fixed**, and **where humans gate**.

Use the ladder when scoping unattended runs, PDCA campaigns, wizard sessions, or Dark Factory targets—so teams do not claim more autonomy than their gates and resources support.

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

*L0–L3 are defined and exercised today (L1 and L2 are demonstrated in the [worked examples](BOUNDED-EXECUTION-EXAMPLES.md)); L4–L8 remain vision requiring ADRs, go/no-go, and strategic checkpoints. Higher levels add gates and never remove lower-level ones.*

## How a level is enforced

1. A run (or campaign item) declares its **target level**.
2. The **Assay gate** for that level must pass before the change is considered done. Core evidence in `forge/forge.config.yaml` includes `tests_pass`, `acceptance_criteria_met`, and `risks_reviewed`.
3. **Higher levels do not skip lower-level gates**; they add gates (for example ADR + release at L4).
4. At **L2**, multi-file work should produce proof that **two or more distinct files** changed when acceptance criteria require a change-set—not a single-file patch dressed as L2.

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

Wizard policies **inform prompts and downstream automation**; they do not silently apply upstream edits. Persisted session policies should match the ladder level you intend for execution.

## Forge Dark Factory (PoC reference implementation)

**Forge Dark Factory** is the current **PoC reference implementation** for bounded autonomous coding—not a production Platform submodule.

![Forge Dark Factory bounded execution loop: classify, route, context, plan, draft, apply, verify, proof, trace, escalate](../../docs/assets/methodology-bounded-execution-loop.svg)

*The governed L1 loop. Verify failures trigger bounded repair; ambiguity or budget exhaustion escalates to a human, who still approves the branch or merge.*

| Aspect | PoC scope today |
|--------|----------------|
| **Target autonomy** | **L1** (function/small change); foundation for **L2** change-sets and **L3** use-case slices |
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

- [Bounded execution examples](BOUNDED-EXECUTION-EXAMPLES.md) — real L1/L2 runs with loop, PDCA, and dual-wiki diagrams
- [Respecting resources](RESPECTING-RESOURCES.md) — token economics, decompose-before-escalate, bounded loops
- [Cost-aware planning and model tiering](COST-AWARE-PLANNING-AND-MODEL-TIERING.md) — interactive Cursor planning
- [Agentic SDLC](../agentic-sdlc.md) — humans own intent; agents amplify execution
- [Agentic coding standards](../agentic-coding-standards.md) — review capacity and smaller PRs
- [Assay Gate ceremony](ceremonies-prescriptive.md#5-assay-gate-release-readiness)
