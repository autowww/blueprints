---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Respecting resources

## Why this matters

**Agentic SDLC** assumes humans own intent and agents amplify execution under policy. That policy must account for **finite resources**: cloud and IDE tokens, human review capacity, premium model budget, and the practical limits of **local-first** compute (for example a ~4GB local model profile).

Teams that ignore resource economics get fast-looking automation with **review bottlenecks**, token burn, and fragile unattended runs. Forge treats **bounded execution** as a first-class design choice—not an afterthought.

## What is scarce vs abundant

![Respecting resources: scarce versus abundant, and the routing order deterministic, local, decompose, escalate](../../docs/assets/methodology-resource-routing.svg)

*Protect the scarce (tokens, review, premium budget) by spending the abundant (time, deterministic checks, local calls). The router picks the cheapest tier that clears the bar. See it end-to-end in the [worked examples](BOUNDED-EXECUTION-EXAMPLES.md).*

| Resource | Default stance | Practical lever |
|----------|----------------|-----------------|
| **Cloud / IDE tokens** | Scarce | Cheapest tier that clears the quality bar; decompose before escalate |
| **Human review and attention** | Scarce | Smaller autonomous units (autonomy ladder); Assay Gate; explicit merge approval |
| **Premium model budget** | Scarce | ROI-gated escalation; strategy passes only when task size amortizes cost |
| **Wall-clock time** | Abundant (default) | Iterate, repair, decompose—spend time before spending tokens |
| **Deterministic checks** | Cheap | Scripts, CI, freeze gates—prefer when a rule exists |

**Guiding principle:** maximize deterministic work and cheap local calls; **decompose rather than pay**; escalate to a larger model or a human only when value justifies it.

## Operating rules

1. **Deterministic-first** — If a template, script, or CI check can settle the task, do not invoke an LLM.
2. **Cheapest tier that clears the bar** — Classify the task (domain, size, value); route to deterministic → local → decompose → escalate in that order.
3. **Decompose before escalate** — When local quality is marginal, split into smaller units that fit local capability instead of paying for cloud reasoning immediately.
4. **Bounded loops** — Cap retries, decomposition depth, context budget, and per-run local calls; refuse to spend past the ceiling and escalate instead.
5. **Architecture and security always escalate** — Required quality is set high for these task classes regardless of local model cards.
6. **Track escalation rate** — A rising rate signals weak scaffolds or mis-sized autonomy; improve capability cards and gates over time.

## Resource types in practice

| Type | Where it shows up | Forge alignment |
|------|-------------------|-----------------|
| **Tokens (Cursor / cloud)** | IDE context, subagents, API calls | [Cost-aware planning and model tiering](COST-AWARE-PLANNING-AND-MODEL-TIERING.md) for **interactive** work |
| **Compute (local ~4GB profile)** | Ollama / Granite / small local workers | Strong on XS/S clear/complicated edits; weak on planning and architecture—see [Autonomy levels](AUTONOMY-LEVELS.md) |
| **Human gates** | Merge, Assay Gate, approval requests | [Forge ceremonies](ceremonies-prescriptive.md#5-assay-gate-release-readiness); Lenses agentic bridge |
| **Evidence (CI)** | Tests, acceptance criteria, risks reviewed | `forge/forge.config.yaml` core evidence; proof reports from governed runs |

## Interactive planning vs autonomous execution

| Mode | Audience | Primary doc |
|------|----------|-------------|
| **Interactive (Cursor)** | Human in the loop each turn | [Cost-aware planning and model tiering](COST-AWARE-PLANNING-AND-MODEL-TIERING.md) — t-shirt triage, model tiering, plan structure |
| **Autonomous / bounded loops** | Unattended or PDCA campaigns | This page + [Autonomy levels](AUTONOMY-LEVELS.md) — ladder, gates, local-first routing |

Cost-aware rules shape **how you plan** in the IDE. Respecting resources shapes **how much change** an autonomous run may attempt and **when** it must stop and ask a human.

## Autonomy ladder (overview)

Autonomy is not binary. Forge defines a **testable L0–L8 ladder**: each level names the **unit of autonomous delivery**, what architecture or contracts stay fixed, and where humans gate.

At a glance: **L0** is suggestions only; **L1** is a single function or small contract-bound change; **L2** is a multi-file change-set without rearchitecture; **L3** is an end-to-end use-case slice inside one existing app. Higher levels add scope and gates.

Full table, enforcement, and PoC notes: **[Autonomy levels](AUTONOMY-LEVELS.md)**.

## Reference implementation: Forge Dark Factory (PoC)

**Forge Dark Factory** is a governed, sequential, **local-first** autonomous coding loop (PoC). It implements deterministic classify → route → context → plan → draft → apply → verify → repair → proof → dual-wiki trace → escalate, with an **L1** target today and foundation for **L2–L3**.

The PoC repo is not a published product surface; the **ladder and resource rules in this handbook** are methodology whether or not you run Dark Factory. Operators adopting Platform workcells or LCDL patch execution can use the same gates and honesty about local model limits.

**See it in action:** [Bounded execution examples](BOUNDED-EXECUTION-EXAMPLES.md) walks real L1 and L2 runs — including a token-free deterministic fix and a local→Cursor worker-ladder step — so you can see exactly what each level spends.

## Related

- [Bounded execution examples](BOUNDED-EXECUTION-EXAMPLES.md) — real L1/L2 runs, loop, routing, PDCA, and dual-wiki diagrams
- [Autonomy levels](AUTONOMY-LEVELS.md) — L0–L8 ladder, Assay enforcement, 4GB boundary
- [Cost-aware planning and model tiering](COST-AWARE-PLANNING-AND-MODEL-TIERING.md) — Cursor triage and model tiering
- [Agentic SDLC](../agentic-sdlc.md) — cross-cutting agent layer
- [Agentic coding standards](../agentic-coding-standards.md) — review bottleneck and WIP
- [Versona operating model](VERSONA-OPERATING-MODEL.md) — cognition vs execution plane
- [Assay Gate ceremony](ceremonies-prescriptive.md#5-assay-gate-release-readiness)
