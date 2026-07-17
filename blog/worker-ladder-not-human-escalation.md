---
title: The Worker Ladder Is Not Human Escalation
meta_description: "Inside a bounded agent loop, local to Cursor recovery is not the same as escalating to a human—read the bounded execution examples carefully."
---

# The Worker Ladder Is Not Human Escalation

One of the most common misreadings in [bounded execution examples](https://blueprints.forgesdlc.com/sdlc--methodologies-forge-bounded-execution-examples.html) is Example 2: the router picks the `local` tier, Granite stalls, and the run steps to **Cursor**—yet `escalated: false`.

Teams report this as “the agent escalated to a better model.” That description is imprecise enough to break governance conversations. **Worker-ladder stepping** and **loop escalation to a human** are different mechanisms.

## Two different “escalations”

| Mechanism | What moves | Who decides | Typical trigger |
|-----------|------------|-------------|-----------------|
| **Worker ladder** | Draft backend inside the loop (`local` → `cursor` → `deterministic` → `fake`) | The driver / router | Local stall, timeout, weak draft quality |
| **Loop escalation** | The run stops for human judgment | A person | Ambiguity, budget exhaustion, architecture/security class |

Example 2 spends a **within-loop** recovery: same campaign item, same autonomy level (L1), no human turn during the loop. The human gate still sits at **approve branch/merge**—outside the PoC loop.

Confusing the two leads to bad metrics (“we escalated to cloud” when you only stepped the worker ladder) and bad policy (“we banned cloud” when the honest path is ROI-gated escalation only when local + decompose are exhausted).

## How the loop spends resources

The bounded execution loop is designed to spend **abundant** resources before **scarce** ones:

```text
  classify → route → plan → draft → apply → verify
                    ↑
            worker ladder (time, local compute)
                    ↓
            loop escalate → human (review, judgment)
```

**Routing tier** is what the router *selected* (deterministic, local, escalate). **Worker ladder** is what actually *ran* inside the draft step. Stepping from Granite to Cursor is **not** the same as the loop deciding a human must intervene.

See the handbook’s [resource routing diagram](https://blueprints.forgesdlc.com/sdlc--methodologies-forge-bounded-execution-examples.html) and [Example 6 — When the loop should stop](https://blueprints.forgesdlc.com/sdlc--methodologies-forge-bounded-execution-examples.html#example-6--when-the-loop-should-stop-escalation-and-honesty).

## Cloud escalation is gated separately

Even when the worker ladder reaches Cursor, **cloud escalation** in the router sense requires stricter conditions: typically `value == must_have`, `local_stalled`, and `decomposition_exhausted`. Track **escalation rate** over time—a rising rate often signals mis-sized autonomy or weak scaffolds, not “smarter” automation.

## Practical takeaway for operators

When you declare an autonomy level for a run:

1. Name the **target level** (L1, L2, L3, …).
2. Record which **worker** won each patch unit.
3. Record whether the loop **escalated to a human** (`escalated: true`).
4. Do not treat “Cursor was used” as human escalation.

## Go deeper

- [Bounded execution examples](https://blueprints.forgesdlc.com/sdlc--methodologies-forge-bounded-execution-examples.html) — Examples 2 and 6
- [Respecting resources](https://blueprints.forgesdlc.com/sdlc--methodologies-forge-respecting-resources.html) — scarce vs abundant
- [Platform autonomy hub](https://platform.forgesdlc.com/docs-autonomy-levels-index.html) — L1–L3 building blocks
