---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# ForgeSDLC — concept map and term-collision register

**Purpose:** Single-page **canonical concept matrix** (how core terms relate to lifecycles, owners, artifacts, and meetings) and a **term-collision register** for known ambiguities. Detailed term → path mapping remains in [`NAMING-REFERENCE.md`](NAMING-REFERENCE.md).

**Sources:** [`NAMING-REFERENCE.md`](NAMING-REFERENCE.md), [`ARTIFACT-AND-DECISION-MODEL.md`](ARTIFACT-AND-DECISION-MODEL.md), [`FORGE-SDLC-PDLC-BRIDGE.md`](FORGE-SDLC-PDLC-BRIDGE.md), [`foundation-connection.md`](foundation-connection.md), [`ceremonies-prescriptive.md`](ceremonies-prescriptive.md), [`roles.md`](roles.md), [`../../../README.md`](../../../README.md), [`../../SDLC.md`](../../SDLC.md), [`../../../pdlc/PDLC.md`](../../../pdlc/PDLC.md), [`../../../disciplines/engineering/software-architecture/SOFTWARE-ARCHITECTURE.md`](../../../disciplines/engineering/software-architecture/SOFTWARE-ARCHITECTURE.md).

---

## Concept matrix

| Concept | Canonical definition | Not this | Grain / scope | Human owner or accountable role | Versona role | Primary artifacts | Primary meetings | PDLC relationship | SDLC relationship | Common confusions / aliases | Recommendation |
|---------|----------------------|----------|---------------|--------------------------------|--------------|-------------------|------------------|-------------------|-------------------|----------------------------|----------------|
| **ForgeSDLC** (Forge SDLC) | Forge **delivery methodology**: Ore→Ingot→Spark→Charge, Assay Gate, Ember Log, discipline Versonas, mapped to **A–F** and **C1–C6**. | The whole **Blueprints** repo; not a substitute for generic `SDLC.md` / `PDLC.md`. | Iteration-level (often 1–2 weeks) inside product + delivery lifecycles. | Delivery team (all **hats**); split per [`roles.md`](roles.md). | Assist at **decision points**; not org roles. | Ore, Ingots, Sparks, Charge, Ember Log, Assay evidence, `forge-logs/versona/…`. | Prescriptive Forge **meetings** in [`ceremonies-prescriptive.md`](ceremonies-prescriptive.md). | Feeds / fed by **P1–P6** (e.g. problems→Ore; Assay→P4; learnings→P5). | Embodies **A–F** mechanics atop generic SDLC. | “Forge” alone; **Forge iteration** vs **Product Spark**. | Use **Forge SDLC** or **Forge** + link to overview; avoid ambiguous **ForgeSDLC** without first mention. |
| **Blueprints** | Reusable **documentation and process packages** — lifecycles, disciplines, support — **prescriptive framework** for any project ([`README.md`](../../../README.md)). | A single product site; not team-specific runbooks. | Org-wide / multi-project reuse. | Framework maintainers (`POLICY.md`); adopters apply locally. | N/A (meta-package). | Markdown packages, templates, bridges. | N/A (teams instantiate). | Hosts **PDLC** + **SDLC** definitions Forge plugs into. | Defines generic SDLC + ceremony **foundation**. | “Handbook” = often **blueprints-website** output. | Call **Blueprints** the **framework**; **Forge** is a **methodology** within SDLC practice. |
| **Versona** | Discipline **virtual persona** (often AI-mediated); optional **§5** structured report per contract — **not** an org role ([`versona/README.md`](versona/README.md)). | A calendar **meeting**; not synonymous with **Challenge pass** globally. | Discipline / session template scope. | Humans own outcomes; Versona assists judgment. | **Is** the instantiated persona. | Rules, `forge-logs/versona/<actor>/<session-id>/`. | Invoked inside or outside **meetings**. | **P2** validation; **P3** alignment. | Spans **A–F** by discipline. | **User persona** (PDLC); **Product Management Versona** (template scope). | **Canonical**; disambiguate **Product Management Versona** as named template. |
| **Versona session** | One interaction with a Versona — folder under `forge-logs/versona/<actor>/<session-id>/`; may include several **activities** ([`VERSONA-FRAMEWORK.md`](versona/VERSONA-FRAMEWORK.md)). | A **meeting** or **ceremony** object (different record model). | Single session; multi-activity allowed. | Invoker + owners for acted-on outcomes. | Session’s discipline lens. | `SESSION.md`, manifests, outputs; optional `ember_log_ref`. | May align with review/refinement **meetings**. | **P2–P3** evidence. | **C1/C4**-shaped when challenging. | **Challenge pass** = one activity type only. | **Canonical**; keep **meeting / ceremony / Versona session** distinction ([`NAMING-REFERENCE.md`](NAMING-REFERENCE.md)). |
| **Meeting** | Scheduled, accountable **team** collaboration — preferred **public** label for Forge events ([`NAMING-REFERENCE.md`](NAMING-REFERENCE.md)). | A Versona folder; not “ceremony” alone in external copy. | Calendar / team event. | Per ceremony matrices in [`ceremonies-prescriptive.md`](ceremonies-prescriptive.md). | Optional discipline participation. | Agendas, notes → Ember Log / directives. | **Is** the meeting. | Realizes product + delivery intents across PDLC/SDLC. | Covers **C1–C6** over time. | **Ceremony** = same events when mapping **C1–C6**. | **Canonical** public label for those events. |
| **Forge Spark** | Smallest **delivery** unit (~1–4 h), phase-prefixed; maps to WBS **Task**; same hierarchy, richer contract. | **Product Spark**; exploration **spike**. | Task-level execution. | **Implementer** primary; Owner accepts increment. | Scope/review for risk and quality. | Spark IDs, PRs, `forge-logs/`. | Daily sync (Charge), review, verify. | Delivers **Product Spark** scope over iterations. | **D–F** execution; tags **A–F**. | **Story/Task**; informal “spark”. | Prefer **Forge Spark** when ambiguity exists. |
| **Product Spark** | Potentially shippable **product** slice: PoC, MVP, or phased increment. **Aliases (same meaning):** **release slice**, **product increment**. | **Forge Spark** (task). | Product / roadmap grain; many iterations. | **Product hat** / PM — value and scope. | Product Management Versona (roadmap DoR, fit). | Roadmap, WBS, planning docs. | Planning, roadmap gates, review. | **P3** commitment; milestones. | **Contains** multiple **Forge iterations**. | Agile “increment”; **milestone** alignment. | **Canonical** head term; aliases allowed in context. |
| **Charge** | **Today’s** selected Forge Sparks — daily commitment; **view** on backlog, not a separate board. | Second backlog system; not a milestone. | Single day. | Team confirms; Engineering often leads execution. | Unblock sessions optional. | Daily Charge file / selection ([`daily/README.md`](daily/README.md)). | **Daily sync** (**C3**). | Reflects **P3** commitments. | **Build (D)**. | Sprint commitment (other methods). | **Canonical**; reinforce “view, not board”. |
| **Ore** | Raw **intake** — ideas, problems, opportunities **before** refinement. | Execution-ready work. | Backlog intake. | **Product hat** — intake quality ([`foundation-connection.md`](foundation-connection.md)). | Optional product/strategy lenses. | Backlog items as Ore. | **Ore intake**; refinement. | **P1** feeds validated problems → Ore. | **Discover / Prioritize (A)**. | Ungroomed ticket; “idea”. | **Canonical** upstream of Ingot. |
| **Ingot** | Refined, **plannable** work (often story-level) with **acceptance criteria**. | Spark; raw Ore. | Story-ready grain. | Product + Engineering refinement; Owner accepts. | Versonas at refinement. | Specs, AC, ADR links. | **Refinement** (**C1**). | **P3** scoping. | **Specify (B)**. | “Story”, “feature spec”. | **Canonical** between Ore and Spark. |
| **Assay Gate** | **Evidence-based release** decision (e.g. market-ready vs code-only). | Optional sign-off under pressure (anti-pattern). | Release decision point. | **Governance** steward; cross-hats participate. | Security/Compliance often. | Evidence package, checklists, release notes. | **Assay Gate** meeting. | **P4 Launch** readiness. | **Verify/Release (E–F)**. | Informal “go-live”. | **Canonical** named gate vs generic approval. |
| **PDLC** | **Product development lifecycle** — Forge uses **P1–P6**; **SDLC** nested as Build & Release after **P3** ([`PDLC.md`](../../../pdlc/PDLC.md)). | Duplicate of SDLC naming. | Product-wide; months to years. | PM, UX, Tech Lead, etc. (§1). | Discipline bridges. | Vision, experiments, GTM, metrics. | Stage-style decisions; discovery cadences. | **Is** PDLC. | **Contains** SDLC for delivery. | Seven-phase **benchmark** vs **P1–P6** — [`PDLC.md` § Benchmark map](../../../pdlc/PDLC.md#benchmark-map-seven-phase-reference) · [`NAMING-REFERENCE.md`](NAMING-REFERENCE.md). | **Canonical**; point to `PDLC.md`. |
| **SDLC** | Delivery flow: **Discover/Prioritize → … → Release** — “building the product **right**” ([`SDLC.md`](../../SDLC.md)). | PDLC; Forge-specific mechanics (those live under Forge). | Delivery lifecycle inside PDLC. | **Owner / Implementer** + methodology maps. | Per-discipline bridges. | Specs, tests, ADRs, release notes. | Ceremonies covering **C1–C6** intents. | Runs **inside** PDLC post-commitment. | **Is** SDLC. | **A–F** shorthand vs reader-facing names. | **Canonical**; prefer reader-facing names on public pages. |
| **Decision Record** | **Map to:** **Ember Log** entries — trade-offs, risk acceptance, scope/priority changes; decision **memory** ([`NAMING-REFERENCE.md`](NAMING-REFERENCE.md) **Ember Log**). | Same as full **ADR** for every line. | Decision-point lines in `ember-logs/`. | Governance + Owner for product decisions. | Prompt → Ember Log from §5 / activities. | `ember-logs/YYYY-MM-DD.md`. | Any meeting with decisions. | **P3–P5** strategic cuts. | All phases when scope/quality shifts. | “Decision log” (industry). | Treat as **synonym for Ember Log entry** or define project schema in `sdlc/`. |
| **Retro Record** | **Map to:** documented **retro** outputs + traceability to **directives** (evidence, owner, approval) per [`ceremonies-prescriptive.md`](ceremonies-prescriptive.md) § “From retro to directives”. | A second parallel artifact system if it duplicates Ember Log + directives. | Per retro cycle. | Whole team; experiment **owner**. | Versona effectiveness review. | Retro notes → **directive** PRs/files. | **Retro** (**C5**). | Learnings → **P5**; new **P1** Ore. | **C5** Improve. | “Retrospective minutes” only. | Link **retro documentation** to **directive** updates explicitly. |
| **Directive** | Markdown files governing **how the team works** — `sdlc/` rules, `.cursor/rules/`, norms, **ADR-style process** changes ([`ceremonies-prescriptive.md`](ceremonies-prescriptive.md)). | Informal chat without owner. | Team policy grain. | Named owner + governance approval. | May encode Versona norms. | Rules files, team norms. | Fed by **retro**. | Shapes **P3–P6** execution. | Shapes SDLC **application**. | Charter, working agreement (if not in repo). | **Canonical** for governed team rules. |
| **ADR** (Architecture Decision Record) | Short record: context, decision, consequences for **significant architectural** choices ([`SOFTWARE-ARCHITECTURE.md`](../../../disciplines/engineering/software-architecture/SOFTWARE-ARCHITECTURE.md)). | Every Ember Log line; not every product pivot doc. | Architecture decision grain. | Tech lead / engineering accountability. | Architecture Versona may prompt. | `docs/adr/` (typical). | Design reviews, refinement. | **P2** feasibility; **P3** constraints. | **Design (C)**. | **Technical Decision Record** as loose synonym. | **ADR** canonical; use **Technical Decision Record** only as plain-language alias for **ADR**, not for Ember Log or directives. |

The table above is a **summary**. The subsections below preserve **full definitions, boundaries, and cross-links** so nuance is not lost when cells are shortened.

---

## Detailed concept notes

### ForgeSDLC (Forge SDLC)

- **What it is:** Forge is a **delivery methodology** that plugs into the shared blueprint **foundation**: tracking spine + ceremony intents **C1–C6**. It defines *how* a team refines, scrutinizes, executes, and releases work — Ore → Ingot → Spark → Charge, evidence at **Assay Gate**, **Ember Log** for decision memory, and **Versonas** for discipline lenses (see [`foundation-connection.md`](foundation-connection.md)).
- **Boundaries:** Forge does **not** replace generic [`SDLC.md`](../../SDLC.md) or [`PDLC.md`](../../../pdlc/PDLC.md); it **operationalizes** SDLC phases **A–F** with Forge-specific mechanics and artifacts.
- **Iteration:** A **Forge iteration** is a delivery cycle (often 1–2 weeks) **inside** a **Product Spark**; scope and evidence are assessed at the iteration boundary ([`NAMING-REFERENCE.md`](NAMING-REFERENCE.md)).
- **Prescriptive shape:** Phase-tagged Sparks (`discover:` … `release:`), traceability Ore → Ingot → Spark, **Assay Gate** non-negotiable for evidence-based release ([`foundation-connection.md`](foundation-connection.md)).
- **Naming:** Publish **Forge SDLC** or **Forge** with a link to the methodology overview; **ForgeSDLC** (one word) is acceptable in branding only if defined once — avoid mixing spellings without a glossary entry.

### Blueprints

- **What it is:** The **Blueprints** repository is reusable **documentation and process packages**: **`sdlc/`**, **`pdlc/`**, **`disciplines/`**, and support packages — prescriptive **framework** text for any adopting project ([`README.md`](../../../README.md)).
- **Framework vs methodology:** **Blueprints** is the **framework** (shared vocabulary, lifecycles, templates). **Forge** is one **methodology** (operating detail) within that ecosystem, not the whole repo.
- **Consumption:** Sites such as **blueprints.forgesdlc.com** are **handbook outputs**; the **source of truth** for definitions remains Markdown in the **blueprints** repo (submodule in consumers).

### Versona

- **What it is:** A **discipline-focused virtual persona** — typically AI-instantiated (e.g. Cursor rules) — that brings a professional lens; it is **not** an org chart role ([`roles.md`](roles.md), [`versona/README.md`](versona/README.md)).
- **§5 output:** Teams may use a **§5-shaped structured concern report** ([`VERSONA-CONTRACT.md`](versona/VERSONA-CONTRACT.md)); other activities (advise, draft, handoffs) are equally valid per [`VERSONA-FRAMEWORK.md`](versona/VERSONA-FRAMEWORK.md).
- **Families:** Engineering, Data, Product, Governance, Cross-cutting (e.g. Security) — see [`roles.md`](roles.md) table.
- **Accountability:** Versonas **assist** judgment; humans own delivery, release, and Ember Log integrity.

### Versona session

- **What it is:** One **interaction** with a Versona: a folder under `forge-logs/versona/<actor>/<session-id>/`, which may contain several **activities** ([`VERSONA-FRAMEWORK.md`](versona/VERSONA-FRAMEWORK.md) §1).
- **Not a meeting:** **Meetings** are calendar-accountable **team** events. **Versona sessions** are bounded discipline work with a different storage model — they do **not** replace daily sync, retro, or gates ([`NAMING-REFERENCE.md`](NAMING-REFERENCE.md) § “Meetings vs ceremonies vs Versona sessions”).
- **Challenge pass:** Informal name for a **§5-shaped** discipline review — **one** possible session activity, **not** the global meaning of “Versona” ([`NAMING-REFERENCE.md`](NAMING-REFERENCE.md)).
- **Artifacts:** Session manifests, `work_item_kind` values (e.g. `spark`, `spike_discipline`), optional `ember_log_ref` when a decision is logged ([`NAMING-REFERENCE.md`](NAMING-REFERENCE.md)).

### Meeting

- **What it is:** Scheduled, accountable **team** collaboration — the preferred **public** label for Forge events in prescriptive docs ([`NAMING-REFERENCE.md`](NAMING-REFERENCE.md)).
- **Ceremony:** The same events are **ceremonies** when tied to blueprint **intent types C1–C6** ([`ceremony-foundation.md`](../ceremonies/ceremony-foundation.md)). **Meeting** = external-friendly label; **ceremony** = foundation mapping — not three competing object types vs **Versona sessions**.
- **Inventory:** Ore intake, refinement, planning, daily sync, review, Assay Gate, retro — inputs/outputs in [`ceremonies-prescriptive.md`](ceremonies-prescriptive.md).

### Forge Spark

- **What it is:** The smallest **delivery** unit (~1–4 hours), often **phase-prefixed** (`discover:`, `specify:`, `design:`, `build:`, `verify:`, `release:`). It maps to WBS **Task**; **Spark = Task** — one hierarchy, one namespace, no duplicate WBS ([`README.md`](README.md), [`process-and-flows.md`](process-and-flows.md)).
- **Not a spike:** Exploration / **discipline spikes** are time-boxed **learning** with a different lifecycle — **not** Forge Sparks ([`versona/DISCIPLINE-SPIKE.md`](versona/DISCIPLINE-SPIKE.md)).
- **Traceability:** Prescriptive rule: every Spark that ships should be **linkable** to parent Ingot and original Ore ([`foundation-connection.md`](foundation-connection.md)).
- **PRs:** Implementation slices for `build:` and `verify:` Sparks ([`foundation-connection.md`](foundation-connection.md)).

### Product Spark (release slice / product increment)

- **What it is:** A potentially shippable **product** slice — PoC, MVP, or phased increment. **Aliases (same meaning):** **release slice**, **product increment** ([`NAMING-REFERENCE.md`](NAMING-REFERENCE.md)).
- **Why keep all three names:** **Product Spark** is the canonical Forge head term; **release slice** and **product increment** help readers coming from other practices — they are **not** separate concepts.
- **Grain:** Spans **multiple Forge iterations**; roadmap and WBS alignment in [`planning/PLANNING-FLOW.md`](planning/PLANNING-FLOW.md).
- **Collision:** Never conflate with **Forge Spark** (task-level).

### Charge

- **What it is:** **Today’s** selected Forge Sparks — the daily commitment ([`NAMING-REFERENCE.md`](NAMING-REFERENCE.md)).
- **View, not board:** Charge is a **label/filter** on the existing backlog — **not** a second board or parallel system ([`foundation-connection.md`](foundation-connection.md) anti-patterns).
- **Ceremony fit:** Aligns with **daily sync** and **C3** ([`foundation-connection.md`](foundation-connection.md) C3 — Plan the slice / Execute & unblock).

### Ore

- **What it is:** Raw, unrefined **intake** — ideas, problems, opportunities — **before** refinement ([`NAMING-REFERENCE.md`](NAMING-REFERENCE.md)).
- **Flow:** Phase **A (Discover)** in the seven-phase benchmark map; continuous intake; feeds refinement Ore → Ingot ([`foundation-connection.md`](foundation-connection.md)).
- **PDLC:** Validated product problems from **P1** feed the Ore pipeline ([`FORGE-SDLC-PDLC-BRIDGE.md`](FORGE-SDLC-PDLC-BRIDGE.md)).

### Ingot

- **What it is:** Refined, **plannable** work (often story-level) with **acceptance criteria** — the “spec” step between Ore and executable Sparks ([`NAMING-REFERENCE.md`](NAMING-REFERENCE.md), [`foundation-connection.md`](foundation-connection.md)).
- **Not:** Not yet the **Spark** / task execution grain; not raw Ore.

### Assay Gate

- **What it is:** An **evidence-based release** decision — e.g. market-ready vs code-only — with per-work-type evidence expectations ([`NAMING-REFERENCE.md`](NAMING-REFERENCE.md), [`planning/PLANNING-FLOW.md`](planning/PLANNING-FLOW.md)).
- **Anti-pattern:** Skipping Assay Gate under schedule pressure is explicitly out of bounds in Forge prescriptive guidance ([`foundation-connection.md`](foundation-connection.md) anti-patterns).
- **PDLC / SDLC:** Ties to **P4 Launch** readiness and SDLC **Release (F)** / **Verify (E)** prep ([`FORGE-SDLC-PDLC-BRIDGE.md`](FORGE-SDLC-PDLC-BRIDGE.md)).

### PDLC

- **What it is:** **Product development lifecycle** — Forge documents **P1–P6** in [`PDLC.md`](../../../pdlc/PDLC.md): Discover problem → Validate solution → Plan & Commit → Launch → Grow → Mature/Retire (sunset).
- **SDLC nesting:** After **P3**, the generic **SDLC** runs as the **Build & Release engine** inside the product lifecycle ([`PDLC.md`](../../../pdlc/PDLC.md) opening, [`PDLC-SDLC-BRIDGE.md`](../../../pdlc/PDLC-SDLC-BRIDGE.md)).
- **Seven-phase benchmark:** External “seven-stage” NPD language maps to **P1–P6** for comparison; Forge does **not** claim seven **public** PDLC phases — see [Benchmark map (seven-phase reference)](../../../pdlc/PDLC.md#benchmark-map-seven-phase-reference) and [`NAMING-REFERENCE.md`](NAMING-REFERENCE.md).

### SDLC

- **What it is:** Software **delivery** lifecycle in blueprint terms: **Discover / Prioritize → Specify → Design → Build → Verify → Release** — “building the product **right**” ([`SDLC.md`](../../SDLC.md)).
- **Shorthand:** **A–F** is internal shorthand for bridges and examples; reader-facing names are primary on [`SDLC.md`](../../SDLC.md).
- **Ceremony intents C1–C6:** Recurring collaboration should cover these intent types over time; they do not replace artifact obligations ([`SDLC.md`](../../SDLC.md) § “Ceremony intents vs phases”).

### Decision Record (mapped term)

- **Canonical mapping:** This phrase is **not** a separate artifact type in [`NAMING-REFERENCE.md`](NAMING-REFERENCE.md). Use **Ember Log** entries for operational **decision memory**: trade-offs, risk acceptance, scope/priority changes — stored under `ember-logs/YYYY-MM-DD.md` ([`NAMING-REFERENCE.md`](NAMING-REFERENCE.md) **Ember Log**, [`daily/README.md`](daily/README.md)).
- **Separation from ADR:** Ember Log captures *why* at decision points; **ADRs** capture **architectural** decisions with template structure ([`SOFTWARE-ARCHITECTURE.md`](../../../disciplines/engineering/software-architecture/SOFTWARE-ARCHITECTURE.md)).
- **Project choice:** Teams may add a local `sdlc/` convention naming structured “decision records” if they still roll up to Ember Log and traceability rules.

### Retro Record (mapped term)

- **Canonical mapping:** **Retro** outputs must be documented enough to feed **directives** — with **evidence**, **owner**, **approval**, and **review/expiry** per team governance ([`ceremonies-prescriptive.md`](ceremonies-prescriptive.md) § “From retro to directives”).
- **Minimum bar:** Link retro notes, metrics, or Ember Log entries that justify directive changes; experiments may **graduate** into directive updates.
- **Not:** A duplicate artifact category if the same content is already captured as retro notes + PR to rules files — the important part is **traceability**, not the label “Retro Record.”

### Directive

- **What it is:** Markdown files that **govern how the team works** — e.g. project `sdlc/` rules, `.cursor/rules/`, team norms, **ADR-style process decisions** ([`ceremonies-prescriptive.md`](ceremonies-prescriptive.md)).
- **Lifecycle:** Retros produce experiments; successful changes become **directive** updates with evidence and owners — not informal chat.

### ADR (Architecture Decision Record); Technical Decision Record

- **ADR:** Significant **architectural** choices documented with context, decision, and consequences — see [`SOFTWARE-ARCHITECTURE.md`](../../../disciplines/engineering/software-architecture/SOFTWARE-ARCHITECTURE.md) §3 and the ADR row in [`../../../disciplines/documentation/templates/README.md`](../../../disciplines/documentation/templates/README.md).
- **Technical Decision Record:** Use only as **plain-language** synonym for **ADR** in reader-facing copy. Do **not** use it as a second bucket for Ember Log lines or **directives** — that creates three-way confusion with **Ember Log** and **directives**.

---

## Term-collision register

Known collisions and the **canonical resolution** (expand in [`NAMING-REFERENCE.md`](NAMING-REFERENCE.md) where cited).

| Collision | Parties | Canonical resolution |
|-----------|---------|----------------------|
| **Spark** | **Forge Spark** (task) vs **Product Spark** (product slice) | Different concepts; use full phrase or first-use disambiguation ([`NAMING-REFERENCE.md`](NAMING-REFERENCE.md)). |
| **Spark** | **Forge Spark** vs **exploration / discipline spike** | Spike = **learning**, different lifecycle ([`versona/DISCIPLINE-SPIKE.md`](versona/DISCIPLINE-SPIKE.md)). |
| **Spark** | Informal **product spike** vs **Product Spark** | “Product spike” = colloquial discipline spike on strategy — **not** a fourth official type, **not** a Product Spark. |
| **Session** | **Versona session** vs **meeting** | Different objects: meetings = calendar accountability; Versona sessions = `forge-logs/versona/…` ([`NAMING-REFERENCE.md`](NAMING-REFERENCE.md)). |
| **Gate** | **Assay Gate** vs **PDLC** stage gates / Stage-Gate | Assay = iteration **release evidence**; product gates = **PDLC** / approaches — see bridges. |
| **Increment** | **Product increment** (alias of Product Spark) vs generic agile **Increment** | Disambiguate with **Product Spark** or **Forge iteration**. |
| **Persona** | **Versona** vs **user persona** (PDLC) | Use **Versona** for discipline virtual persona; context for user/market personas. |
| **Framework** | **Blueprints** (framework) vs **Forge** (methodology) | Blueprints = reusable packages; Forge = **methodology** within SDLC practice. |
| **Decision** | **Ember Log** vs **ADR** vs **Directive** | Ember Log = operational **decision memory**; ADR = **architecture**; Directive = **team rules** evolution. |
| **Record** | Informal **Decision Record** / **Retro Record** vs **Ember Log** / retro → **directives** | Map industry phrases to **Ember Log** and **retro-to-directive** traceability (matrix rows above). |

### Detailed collision notes

- **Spark (three-way):** (1) **Forge Spark** = WBS **task**-level delivery unit. (2) **Product Spark** = product slice (PoC/MVP/phase); aliases **release slice**, **product increment**. (3) **Discipline / exploration spike** = learning spike — see [`DISCIPLINE-SPIKE.md`](versona/DISCIPLINE-SPIKE.md). **Product spike** (informal) = discipline spike on product/strategy — **not** a fourth official spike type and **not** a Product Spark ([`NAMING-REFERENCE.md`](NAMING-REFERENCE.md)).
- **Session vs meeting:** **Meetings** carry **human accountability** on the calendar. **Versona sessions** live under `forge-logs/versona/` and may occur inside or outside a meeting. **Ceremonies** name the same meetings when mapping **C1–C6** ([`NAMING-REFERENCE.md`](NAMING-REFERENCE.md) § “Meetings vs ceremonies vs Versona sessions”).
- **Gate (two layers):** **Assay Gate** = Forge **iteration release** evidence decision. **PDLC** stage gates (e.g. G1–G5 in bridges) and **Stage-Gate** NPD gates = **product** lifecycle decisions — different scope; align using [`PDLC-SDLC-BRIDGE.md`](../../../pdlc/PDLC-SDLC-BRIDGE.md) and [`FORGE-SDLC-PDLC-BRIDGE.md`](FORGE-SDLC-PDLC-BRIDGE.md).
- **Increment:** **Product increment** as an alias of **Product Spark** must be distinguished from generic Scrum “Increment” or informal “slice” language — prefer **Product Spark** or **Forge iteration** when clarifying ([`NAMING-REFERENCE.md`](NAMING-REFERENCE.md)).
- **Persona:** **Versona** (capital V) = discipline virtual persona in Forge. **User/persona** in [`PDLC.md`](../../../pdlc/PDLC.md) = market/user research artifact — disambiguate by context.
- **Framework vs methodology:** **Blueprints** = reusable **framework** packages. **Forge** = **methodology** (how to run delivery) sitting on top of generic SDLC/PDLC text — avoid calling the whole repo “the Forge methodology.”
- **Decision artifacts (three buckets):** **Ember Log** = day-to-day **decision memory** and trade-offs. **ADR** = **architecture** decisions. **Directives** = **team working rules** updated from retros with evidence — not interchangeable labels ([`ceremonies-prescriptive.md`](ceremonies-prescriptive.md), [`SOFTWARE-ARCHITECTURE.md`](../../../disciplines/engineering/software-architecture/SOFTWARE-ARCHITECTURE.md)).

---

*Blueprint reference — align with [`NAMING-REFERENCE.md`](NAMING-REFERENCE.md) when planning or roles change.*
