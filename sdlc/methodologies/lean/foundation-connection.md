# Lean Software Development — connection to the SDLC foundation

Lean is a **principle-based** thinking model, not a prescriptive framework. It layers on top of whatever delivery cadence a team uses (iterations, flow, gates) by asking: **does each activity add value, and how can we reduce waste end-to-end?**

## 1. SDLC phases A–F (Lean lens)

| Phase | Lean expression | Waste to watch |
|-------|-----------------|----------------|
| **A — Shape** | Value definition; last responsible moment for scope decisions | Over-specifying features nobody needs (muda of overproduction) |
| **B — Plan** | Pull-based planning; just-enough detail for the next slice | Excessive upfront planning that will change (inventory of specs) |
| **C — Build** | Small batches; continuous integration; pairing for learning | Task switching, partially done work, handoff delays |
| **D — Verify** | Built-in quality (tests written with code, not after) | Separate late-stage test phases that delay feedback |
| **E — Release** | Shortest safe path to production; automate deployment | Manual release ceremonies that add waiting time |
| **F — Operate & learn** | Production feedback loops; Kaizen for next cycle | Ignoring production signals; not closing the learning loop |

**Prescriptive rule:** Map your **value stream** (idea → production) to phases A–F. Measure **waiting time** between phases — that is often where the largest waste hides.

## 2. Tracking spine (mandatory link)

Lean teams still maintain the blueprint tracking spine:

| Artifact | Lean mapping |
|----------|--------------|
| **Intent / request** | Demand signal; entry to the value stream |
| **Spec** | Just-enough specification; defer detail until pull |
| **Plan** | Commitment at the last responsible moment |
| **Tasks** | Small batches within the flow |
| **PRs** | Integration events; keep small for fast feedback |
| **Reviews** | Learning moments; catch defects at the source |
| **Release** | Value delivery; measure lead time from intent to here |

**Prescriptive rule:** Track **lead time** (intent created → value delivered) and **cycle time** (work started → work done) as primary health metrics. These are more Lean-aligned than velocity or story points.

## 3. Ceremony intents (C1–C6) ↔ Lean practices

| Intent | Lean practice | Notes |
|--------|---------------|-------|
| **C1 — Align & decide** | Value-stream mapping; portfolio Kanban; strategic A3 | Align on **what is valuable**, not just what is requested |
| **C2 — Plan the slice** | Pull-based selection; last responsible moment | Commit when you have enough information, not before |
| **C3 — Execute & unblock** | Stand-up (flow-focused); Gemba walks | Go to where the work happens; remove impediments at the source |
| **C4 — Review & quality** | Built-in quality; customer feedback on delivered value | Inspect the **value delivered**, not just the artifact produced |
| **C5 — Reflect & improve** | Kaizen events; A3 problem-solving; Five Whys | Systematic root-cause analysis, not just "what went well" |
| **C6 — Knowledge share** | Set-based design reviews; cross-team learning; standards | Share **why** decisions were made, not just what was built |

See [ceremony foundation](../ceremonies/ceremony-foundation.md) and [methodology bridge](../ceremonies/methodology-bridge.md).

## 4. Role archetypes (blueprint hats on a Lean team)

| Lean role | Typical archetype emphasis | Notes |
|-----------|----------------------------|-------|
| **Value-stream manager** | **Orchestrator** + **Sponsor proxy** | Owns end-to-end flow; removes systemic waste |
| **Lean coach / sensei** | **Orchestrator** + **Quality advocate** | Teaches Lean thinking; facilitates Kaizen |
| **Team members** | **Implementer** (primary) + **Quality advocate** | Empowered to improve their own process |
| **Management** | **Steer** (context-setter, not command-giver) | Sets vision and constraints; serves the team |

Detail: [roles-archetypes.md](../roles-archetypes.md), [Lean roles chapter](roles.md).

## 5. What Lean adds beyond the foundation

- **Seven principles** as a diagnostic lens for any methodology.
- **Value-stream thinking** — optimize the whole, not local phases.
- **Waste taxonomy** — seven wastes (muda) adapted for software.
- **Last responsible moment** — decision timing as a first-class concern.
- **Kaizen** — structured, continuous improvement as a cultural norm.

## 6. Anti-patterns (prescriptive "don't")

| Anti-pattern | Fix |
|--------------|-----|
| "Lean" as excuse to skip documentation | Lean eliminates **unnecessary** docs, not **all** docs; specs that prevent rework are value-adding |
| Optimizing one phase at the expense of others | Map the **whole** value stream; local speed gains that cause downstream bottlenecks increase total waste |
| Kaizen without follow-through | Track improvement actions; close the loop in the next cycle |
| Confusing Lean with "just go faster" | Speed is a **result** of eliminating waste, not a goal achieved by cutting corners |

## 7. References in-repo

- [`../lean.md`](../lean.md) — methodology summary + diagram  
- [`../ceremonies/lean.md`](../ceremonies/lean.md) — fork table C1–C6  
- [`../../SDLC.md`](../../SDLC.md) — phases and ceremony-intent overview  
