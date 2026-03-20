# Phased delivery ceremonies → ceremony foundation

**Purpose:** Map **phase gates**, reviews, and formal assurance to methodology-neutral **intent types** in [`ceremony-foundation.md`](ceremony-foundation.md).

**Canonical narrative:** [`../phased-delivery.md`](../phased-delivery.md)

---

## Typical gate / review patterns × intent types

Names vary by standard (e.g. ISO/IEC/IEEE 12207-style lifecycles). Illustrative mapping:

| Pattern | Foundation intents (primary → secondary) | Notes |
|---------|------------------------------------------|--------|
| **Requirements review / baseline** | **C1 Align** → **C6 Assure** | Baseline scope; often **Steer** approval to proceed. |
| **Design review** | **C1 Align** → **C6 Assure** | NFRs, interfaces, feasibility locked or accepted. |
| **Build / code review** (formal) | **C3 Sync** → **C6 Assure** | May be continuous (PRs) + periodic **gate** evidence. |
| **Test / verification complete** | **C6 Assure** → **C4 Inspect** | Evidence package; may include **UAT** as **C4** with business. |
| **Release / deployment approval** | **C6 Assure** | **Steer** or delegated **Assure** sign-off; often **outside git**. |
| **Phase-exit / tollgate** | **C6** + **C1** | **Go/hold/stop**; may reset **C2** for next phase’s work. |

**C5 Improve** may appear as **post-project** or **audit** lessons learned rather than frequent retros—unless the org runs **iterative** work **inside** a phase.

---

## Tracking vs compliance

**Git** shows engineering **activity**; **signatures**, **baselines**, and **gate minutes** usually live in **ALM, QMS, or document control**—[`../phased-delivery.md`](../phased-delivery.md).

---

## Suggestions (phased delivery)

| Pattern | Suggestions |
|---------|-------------|
| **Requirements / design reviews** | Treat as **C1 + C6**: alignment **and** readiness to freeze; record **explicit** waivers if you proceed with known gaps. |
| **Phase exit / tollgate** | **Agenda** per intent: evidence (**C6**), stakeholder acceptance (**C4**), **go/no-go** (**Steer**). Don’t merge **C5** into gate unless you time-box it. |
| **UAT** | Pure **C4** for product fit; separate from **technical** test exit (**C6**) when org structure blurs them. |
| **Handoffs** | Between phases, run a **short C3**-style sync on **interfaces** and **traceability ids**—reduces “wrong build” at next gate. |
| **Hybrids** | If you iterate **inside** implementation, still hold **C4** mini-reviews so **C6** at gate isn’t the first inspection. |

Bridge matrix: [`methodology-bridge.md`](methodology-bridge.md).
