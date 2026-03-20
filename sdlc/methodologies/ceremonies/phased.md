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
