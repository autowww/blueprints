---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
content_id: forge.docs.blueprints.forge.epic-execution-profile
canonical_owner: blueprints
primary_persona: engineering_leader
reader_stage: adopt
maturity: defined
evidence_level: canonical_doc
refresh_policy: on_claim_change
last_reviewed: '2026-08-21'
---

# Epic execution profile

## Introduction

The **Epic execution profile** is an **opt-in overlay** on core Forge for teams that delegate **L3 use-case slices** to agents under **OpenSpec** acceptance. Humans **Charge** and specify **Epics** (intent + observable acceptance); agents execute **L1–L2 work inside** a Charged Epic as **runs**, not as Charge-visible WBS Task rows.

> **Dual profile.** Core Forge **keeps** Ore → Ingot → **Forge Spark** → Charge (**Sparks**). Under the Epic execution profile, Charge lists **Epics** instead of Sparks. Spark is **not** removed from Forge — teams choose one delivery profile (or run both on different repos). Every retargeted doc says **under the Epic execution profile** when describing Epic-specific behavior.

**When to adopt:** A team is ready when most committed delivery is **agent-executed L3 slices** with **reviewable diffs**, **one primary repo** per Epic, and **OpenSpec** acceptance criteria the Assay gate can test.

---

## Size gate (ready Epic)

An Epic is **ready to Charge** only when it passes the **size gate**:

| Gate | Requirement |
|------|-------------|
| **One OpenSpec change** | Exactly **one** OpenSpec change folder per Epic — one intent, one reviewable scope |
| **Testable SHALLs** | Capability spec → at least one observable **SHALL** / **MUST** → ≥1 **Given / When / Then** scenario — **not** implementation SHALLs (no file or class names in acceptance) |
| **One primary repo** | Execution and review stay in **one** primary repository; cross-repo work triggers **L4.2 stop-and-ask** (below) |
| **Reviewable diff** | Expected outcome fits a **single PR or merge request** a human can review in one sitting |

Epics that fail the gate stay in refinement (OpenSpec draft, scope split, or human L4 planning) — **do not Charge** until the gate passes.

---

## Grain under the profile

| Grain | Role under the Epic execution profile |
|-------|----------------------------------------|
| **Product Spark** (`M1`) | Release / Assay horizon — unchanged |
| **Epic** (`M1E3`) | Smallest **committed** unit = autonomy **L3** (OpenSpec AC in; review/merge out) |
| **Story / Task / Forge Spark** | **Not** Charge work items; **L1–L2 agent scratch** only inside the Epic |
| **Charge** | **Epics** in play — a **view**, not a Kanban system of record |
| **OpenSpec change** | **1:1** with a ready Epic; Lite SHALLs + scenarios; `tasks.md` is **non-binding** |
| **L4+** | Extra human gates (ADR, cross-repo **L4.2**); agents **stop and ask** |
| **Assay** | Still Product Spark scope; archive ≠ Released |

WBS **Epic** IDs (e.g. `M1E3`) align with committed Epics under this profile. Do **not** mint `M1E3S2T4` rows on Charge for Charged Epics.

---

## L1–L3 inside the Epic

Under the Epic execution profile, **autonomy levels L1–L3 execute inside** the Charged Epic boundary:

| Level | Inside Epic | Human gate |
|-------|-------------|------------|
| **L1** | Single function / contract-bound patch | Approve branch / merge |
| **L2** | Multi-file change-set without rearchitecture | Accept acceptance + merge |
| **L3** | End-to-end use-case slice in one existing app (default Epic target) | OpenSpec acceptance **in**; review **out** |

The **committed Epic** maps to **L3 use-case slice** by default — see [Autonomy levels § Epic execution profile](AUTONOMY-LEVELS.md#epic-execution-profile). Agents may run **L1** or **L2** sub-work **inside** the Epic without new Charge rows.

**Decompose runs, not backlogs:** Agents break work into **execution runs** (classify → plan → apply → verify → repair → escalate). They **do not** maintain parallel WBS Story/Task backlogs or mint Charge rows for each run.

---

## OpenSpec Lite and Full

| Profile | When | Acceptance bar |
|---------|------|----------------|
| **OpenSpec Lite** (default) | Typical feature, UI, or internal behavior in one repo | One capability → observable **SHALL** → ≥1 scenario; `tasks.md` hints only |
| **OpenSpec Full** | API contracts, security-sensitive work, or cross-cutting platform change | Stricter change folder layout, explicit deltas, additional review gates per team OpenSpec pack |

**Rules (Lite default):**

- One change = one intent.
- Not implementation SHALLs — acceptance describes **observable behavior**, not source files.
- Humans approve OpenSpec acceptance **before** Charge; agents apply the change and prove scenarios in verify.

Full profile selection is a **human** decision at Epic specification time.

---

## Charge of Epics

Under the Epic execution profile:

1. Humans select **ready Epics** (size gate green, OpenSpec acceptance approved) into **today's Charge**.
2. Charge remains a **view** on committed work — not a second board ([`process-and-flows.md`](process-and-flows.md)).
3. **One Charged Epic** may host many agent **runs** at L1–L3; runs are **not** Charge items.
4. Daily sync confirms Epic progress, blockers, and escalation — not a Task-level standup on WBS rows.

Core Forge teams that Charge **Sparks** unchanged — see [`daily/README.md`](daily/README.md).

---

## L4.2 stop-and-ask

When work crosses **L4** boundaries, agents **stop and ask** a human before proceeding:

| Trigger | Agent behavior |
|---------|----------------|
| **Cross-repo change** (e.g. submodule bump, **L4.2**) | Stop; request human plan, ADR draft, or explicit approval |
| **New component or platform pattern** (**L4.1+**) | Stop; escalate to architecture gate |
| **Security / compliance ambiguity** | Stop; invoke Security Versona or human owner |
| **OpenSpec Full required but only Lite present** | Stop; request profile upgrade or scope reduction |

Under the Epic execution profile, **L4+ is out of autonomous scope** unless a human explicitly expands the Epic with new gates and acceptance.

---

## Trivial L1 skip

**Trivial one-liners** (typo, comment, config knob with obvious test) may **skip Epic ceremony** when a **classifier** (human or agent policy) marks them **L1 trivial**:

- No new OpenSpec change folder required.
- No Epic Charge row required.
- Still subject to normal review / merge gates.

When in doubt, **use an Epic** — the skip is for noise reduction, not scope hiding.

---

## Ember Log and decisions

Log **Ember Log** entries for **Epic-scope** or **cross-cutting** decisions only — not every L1 run inside an Epic. Operational run trace lives in machine records (Assay evidence, PR, OpenSpec verify output).

---

## Related

| Topic | File |
|-------|------|
| Autonomy L3 default for committed Epic | [`AUTONOMY-LEVELS.md`](AUTONOMY-LEVELS.md#epic-execution-profile) |
| Naming: Epic, Charge dual-profile | [`NAMING-REFERENCE.md`](NAMING-REFERENCE.md) |
| Concept matrix + collisions | [`CONCEPT-MAP.md`](CONCEPT-MAP.md) |
| Artifacts under profile | [`ARTIFACT-AND-DECISION-MODEL.md`](ARTIFACT-AND-DECISION-MODEL.md) |
| Core Spark delivery (default Forge) | [`process-and-flows.md`](process-and-flows.md) · [`forge.md`](../forge.md) |
| Bounded execution examples | [`BOUNDED-EXECUTION-EXAMPLES.md`](BOUNDED-EXECUTION-EXAMPLES.md) |

## Executive capsule

The **Epic execution profile** is an opt-in overlay: Charge lists **Epics**, OpenSpec acceptance defines **L3** scope, and agents decompose **runs** inside the Epic — not WBS Task Charge rows. Core Forge **keeps Spark → Charge**. Maturity: **defined**.

## Who this is for

Engineering leaders adopting **agent-executed L3** delivery. Read the dual-profile note first; default Forge teams can ignore this page.

## Trust boundary

Humans own Charge selection, OpenSpec acceptance, merge, and Assay. Agents execute inside declared Epic boundaries and **stop and ask** at L4.2+.

## How to use this page

Confirm the size gate and OpenSpec bar before Charging an Epic; link execution policy to [`AUTONOMY-LEVELS.md`](AUTONOMY-LEVELS.md) for ladder enforcement.
