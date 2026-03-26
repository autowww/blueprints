# Product creation → delivery — industry, Forge, and PMI-style map

**Purpose:** Map **problem statement through product delivery** using **industry language**, **Forge** work units, and a compact **Inputs → Process → Outputs** (IPE) view per lifecycle phase. Deep definitions live in linked canon; this file is a **navigation spine**.

**Canon:** [`../../../pdlc/PDLC.md`](../../../pdlc/PDLC.md) (P1–P6) · [`../../SDLC.md`](../../SDLC.md) (A–F) · [`FORGE-SDLC-PDLC-BRIDGE.md`](FORGE-SDLC-PDLC-BRIDGE.md) · [`planning/PLANNING-FLOW.md`](planning/PLANNING-FLOW.md) · [`process-and-flows.md`](process-and-flows.md)

**Legend**

| Column | Meaning |
|--------|---------|
| **Industry** | Plain product/delivery language. |
| **Forge** | Ore → Ingot → Spark → Charge, Product Spark, iteration, Assay — see [`NAMING-REFERENCE.md`](NAMING-REFERENCE.md). |
| **Example Sparks** | Illustrative **phase-prefixed** Forge Sparks (`discover:`, `specify:`, …). **Exploration spikes** (learning) use Versona sessions per [`versona/DISCIPLINE-SPIKE.md`](versona/DISCIPLINE-SPIKE.md), not the delivery board. |

---

## PDLC P1 — Discover problem

| **Inputs** | **Process / practices** | **Outputs** |
|------------|---------------------------|-------------|
| Market signals, support data, strategy themes | Interviews, synthesis, competitive scan, persona checks | Problem statement, research synthesis, opportunity sizing, **G1** evidence |

| | |
|--|--|
| **Industry** | Validate a **real problem** before solution work. |
| **Forge** | Validated problems feed **Ore**; no delivery commitment. |

**Disciplines — example Sparks**

| Discipline | Example Spark |
|------------|----------------|
| Product Management | `discover:` synthesize interviews → problem statement |
| UX research | `discover:` run interview protocol |
| BA | `discover:` stakeholder / process context |
| Marketing | `discover:` competitor positioning matrix |
| Architecture | `discover:` optional feasibility of *problem space* (or **exploration spike**) |
| Data | `discover:` metric definitions for evidence |

---

## PDLC P2 — Validate solution

| **Inputs** | **Process / practices** | **Outputs** |
|------------|---------------------------|-------------|
| P1 artifacts, hypotheses | Prototypes, usability tests, experiments, tech spikes | Hypothesis outcomes, feasibility view, **G2** evidence |

| | |
|--|--|
| **Industry** | Test **solution concepts** (desirability, viability, feasibility, usability). |
| **Forge** | **Ore** refined with evidence; **PoC** Product Spark possible; Versona on feasibility. |

**Disciplines — example Sparks**

| Discipline | Example Spark |
|------------|----------------|
| Product Management | `specify:` hypothesis cards; `verify:` experiment readout |
| UX | `design:` prototype; `verify:` usability results |
| BA | `specify:` scenarios tied to hypotheses |
| Architecture | **Exploration spike** or `discover:` time-boxed feasibility |
| Security | `discover:` data-classification sketch for concept |

---

## PDLC P3 — Strategize

| **Inputs** | **Process / practices** | **Outputs** |
|------------|---------------------------|-------------|
| P2 validation | Vision, OKRs, roadmap, business case, GTM, resourcing | Funded initiative, roadmap/WBS seeds, **G3** approval |

| | |
|--|--|
| **Industry** | **Commit** budget, timeline, success metrics, GTM. |
| **Forge** | **Product Sparks** (PoC/MVP/Phase); **Ingots** scoped for SDLC handoff. |

**Disciplines — example Sparks**

| Discipline | Example Spark |
|------------|----------------|
| Product Management | `specify:` roadmap themes; `release:` stage-gate pack |
| BA | `specify:` epic / capability outline |
| PM (governance) | `specify:` dependencies; `verify:` gate criteria |
| Architecture | `design:` context diagram + NFR list |
| DevOps | `discover:` pipeline / env readiness |
| Compliance | `specify:` compliance checklist for build |

---

## SDLC A — Discover / prioritize

| **Inputs** | **Process / practices** | **Outputs** |
|------------|---------------------------|-------------|
| P3 handoff | Prioritize, rough size, WBS/backlog updates | Ordered backlog; items **ready to specify** |

| | |
|--|--|
| **Industry** | **Backlog** intake and ordering. |
| **Forge** | **Ore intake**; **`discover:`** Sparks. |

**Disciplines — example Sparks:** Product `discover:` ordering workshop · BA `discover:` epic draft · Architecture `discover:` enabler Ore · PM `discover:` dependency map.

---

## SDLC B — Specify

| **Inputs** | **Process / practices** | **Outputs** |
|------------|---------------------------|-------------|
| Prioritized items | Refinement, AC, risks | **Ingots** with AC; definition of ready |

| | |
|--|--|
| **Industry** | **Requirements** and acceptance criteria. |
| **Forge** | **Ore → Ingot**; **`specify:`** Sparks. |

**Disciplines — example Sparks:** BA `specify:` story + AC · UX `specify:` UX notes · Testing `specify:` test ideas · Security `specify:` security AC.

---

## SDLC C — Design

| **Inputs** | **Process / practices** | **Outputs** |
|------------|---------------------------|-------------|
| Ready Ingots | Design reviews, ADRs | Design artifacts; **Ingot → Spark** plan |

| | |
|--|--|
| **Industry** | Technical and UX **design**. |
| **Forge** | **`design:`** Sparks; planning decomposition. |

**Disciplines — example Sparks:** Architecture `design:` ADR · SE `design:` component note · UX `design:` handoff · DevOps `design:` pipeline change.

---

## SDLC D — Build

| **Inputs** | **Process / practices** | **Outputs** |
|------------|---------------------------|-------------|
| Design + tasks | Implementation, tests | Code, PRs, CI green |

| | |
|--|--|
| **Industry** | **Implementation**. |
| **Forge** | **Charge**; **`build:`** Sparks. |

**Disciplines — example Sparks:** SE `build:` feature slice · FE `build:` UI · DevOps `build:` workflow · Data `build:` job/model code.

---

## SDLC E — Verify

| **Inputs** | **Process / practices** | **Outputs** |
|------------|---------------------------|-------------|
| Build output | Tests, reviews, regression | Evidence; **done** candidates |

| | |
|--|--|
| **Industry** | **QA**, CI, UAT. |
| **Forge** | **Assay** preparation; **`verify:`** Sparks. |

**Disciplines — example Sparks:** Testing `verify:` e2e / exploratory · Security `verify:` review · Product `verify:` stakeholder sign-off.

---

## SDLC F — Release

| **Inputs** | **Process / practices** | **Outputs** |
|------------|---------------------------|-------------|
| Verified increment | Go/no-go, deploy, communicate | Released artifact; handoff to **P4** |

| | |
|--|--|
| **Industry** | **Ship**, comms, rollback readiness. |
| **Forge** | **Assay Gate**; **`release:`** Sparks. |

**Disciplines — example Sparks:** DevOps `release:` deploy runbook · Product/Marketing `release:` notes + announcement · CS `release:` support FAQ.

---

## PDLC P4 — Launch

| **Inputs** | **Process / practices** | **Outputs** |
|------------|---------------------------|-------------|
| Shippable increment, GTM | Beta/GA, training, monitoring | Live product; **G4** satisfied |

| | |
|--|--|
| **Industry** | **Market activation**. |
| **Forge** | **`release:`** + ops Sparks; launch criteria vs P3 metrics. |

**Disciplines — example Sparks:** Marketing `release:` launch checklist · CS `release:` playbook · DevOps `release:` dashboards/alerts.

---

## PDLC P5 — Grow

| **Inputs** | **Process / practices** | **Outputs** |
|------------|---------------------------|-------------|
| Live metrics | Experiments, funnel work | Iteration backlog → **SDLC A**; **G5** signals |

| | |
|--|--|
| **Industry** | **Adoption**, retention, growth loops. |
| **Forge** | New **Ore** from data; continuous feedback. |

**Disciplines — example Sparks:** Product/Data `discover:` metrics review → Ore · Marketing `verify:` growth experiment analysis.

---

## PDLC P6 — Mature / sunset

| **Inputs** | **Process / practices** | **Outputs** |
|------------|---------------------------|-------------|
| Lifecycle assessment | Sunset, migration, comms | EOL or reposition to P1 |

| | |
|--|--|
| **Industry** | **Retire** or harvest. |
| **Forge** | Deprecation **Ingots**; `build:`/`release:` migration work. |

**Disciplines — example Sparks:** Product `specify:` sunset plan · SE `build:` export tooling · `release:` decommission.

---

## One-page cheat sheet

| **Industry stage** | **Phase** | **Forge focus** |
|--------------------|-----------|-----------------|
| Problem insight | P1 | **Ore** (problems), research |
| Solution proof | P2 | Experiments; optional **PoC Product Spark** |
| Commit & plan | P3 | **Product Spark(s)**, roadmap, **Ingots** |
| Ready & build | A–D | Ore → Ingot → **Sparks** → **Charge** |
| Prove & ship | E–F | **`verify:`**, **Assay**, **`release:`** |
| Go live | P4 | Launch, **G4** |
| Learn | P5 | New **Ore** from metrics |
| End of life | P6 | Migration / deprecation |

---

## Related

- [`NAMING-REFERENCE.md`](NAMING-REFERENCE.md) — term → source file index  
- [`FORGE-SDLC-PDLC-BRIDGE.md`](FORGE-SDLC-PDLC-BRIDGE.md) — alignment tables and worked example
