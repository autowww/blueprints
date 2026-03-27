# Versona framework — kinds, interfaces, processes, sessions

This document defines **generic** concepts for Forge **Versonas**: taxonomy by kind, input/output interfaces, repeatable **process** documentation, **inter-Versona** interaction patterns, **session** storage in the consuming repo, and alignment with **Ember Log** and **day journal**. It complements the Cursor rule shape in [`VERSONA-CONTRACT.md`](VERSONA-CONTRACT.md); it does not replace per-discipline templates.

**Related:** [`README.md`](README.md) (hub — **Source layout** for paths on disk) · [`DISCIPLINE-SPIKE.md`](DISCIPLINE-SPIKE.md) (exploration spike lifecycle, anchors, open/close) · [`catalog/TEMPLATE-INDEX.md`](catalog/TEMPLATE-INDEX.md) (authoritative path per template) · [`catalog/ANCESTRY.md`](catalog/ANCESTRY.md) (kinds, domains) · [`../tasklets/TASKLET-TAXONOMY.md`](../tasklets/TASKLET-TAXONOMY.md) · [`../../../../agents/docs/VERSONA-EXECUTION-TASKLETS.md`](../../../../agents/docs/VERSONA-EXECUTION-TASKLETS.md) · [`../../../../agents/ORCHESTRATION.md`](../../../../agents/ORCHESTRATION.md)

---

## 1. Conceptual model

```ks-diagram
key: swimlane
alt: Diagram
```

| Term | Meaning |
|------|---------|
| **Work item reference** | Any stable handle the team uses: Forge **Ore**, **Ingot**, or **Spark** IDs; external epic/story/task IDs; or a **spike** label. This framework does **not** introduce a new ID scheme—teams map to what they already track. |
| **Exploration spike** | Time-boxed **discipline** learning work (feasibility, unknowns)—**not** the same as a Forge **Spark** (delivery task). Lifecycle, anchors, and templates: [`DISCIPLINE-SPIKE.md`](DISCIPLINE-SPIKE.md). |
| **Activity** | One **unit of Versona work** inside a **session** (e.g. one challenge pass, one sub-step of a larger process). Same concept if your team says “job”; this doc uses **activity** only. |
| **Process template** | A named, repeatable **sequence** of activities, optional **human gates**, and optional **handoffs** to another Versona or to a recipe. |
| **Session** | One user-visible “call”: a folder (or linked set of files) holding context, artifacts, and pointers to logs. A session may contain **multiple** activities. |

---

## 2. Versona kinds

Not every `.mdc` under `versona/` is a **discipline** challenge agent. Use this taxonomy when authoring or extending templates.

| Kind | Purpose | Required content (in rule or linked doc) | Output variant | Bridge to discipline package |
|------|---------|-------------------------------------------|----------------|------------------------------|
| **discipline** | Challenge from one professional lens | Full [`VERSONA-CONTRACT.md`](VERSONA-CONTRACT.md) sections 1–6 | Contract challenge report (concerns table, evidence, recommendation) | **Yes** — `*-SDLC-PDLC-BRIDGE.md` under `blueprints/disciplines/` |
| **routing** | Recommend which discipline Versonas to invoke | Routing rules (work item state, phase prefix, hat, scale); discipline index | Routing table (priority / optional / not recommended) | **N/A** |
| **family_aggregator** | Run several discipline challenges and merge | List of child disciplines; relevance skip rules; consolidation rules | Consolidated report + per-discipline detail | **Per child** (links to their packages) |
| **meta** | Thin orchestration over **tasklets** or shallow triage | Identity, when to use / **not** use, merge protocol; link to tasklets | Shortened or merged report (still structured) | **Optional** — may point at methodology docs only |
| **workflow** | Repo or methodology bootstrap (not a challenge gate) | Invocation triggers, checklist, handoffs to other rules | Setup or audit report (tabular status) | **N/A** or **optional** |

**Authoring rule:** Pick the kind first. Do not force a **routing** or **workflow** template into the full discipline Identity + bridge layout unless you intentionally align it for traceability.

---

## 3. Interface model (inputs, activities, outputs)

### 3.1 Input interface

Document what the Versona (or process) needs before meaningful work:

- **Work item references** — IDs or links (Spark, Ingot, Ore, external keys).
- **Artifacts** — paths under the repo (specs, diagrams, configs) or pasted excerpts.
- **Prior session** — path to another session folder when chaining calls.
- **Human declarations** — current hat, phase, risk appetite (when relevant).

Optional **machine-readable** hints (for future tooling): a short YAML or bullet schema in the session manifest or process doc—**not** enforced by blueprints v1.

Example (illustrative only):

```yaml
# Optional — session or process companion
inputs_expected:
  - work_item_refs: ["M1E1S2T3"]
  - artifact_paths: ["docs/requirements/feature-x.md"]
  - prior_session: null
```

### 3.2 Activity

An activity is **bounded work** with a clear stop condition:

- Steps the agent performs (analysis, questions, table fill).
- **Pause points** — where the human must answer, run a script, or invoke another Versona before continuing.
- Links to **tasklets** (cognition) or **recipes** (execution plane)—see §6.

### 3.3 Output interface

**Discipline** Versonas use the structured report in [`VERSONA-CONTRACT.md`](VERSONA-CONTRACT.md) §5.

**Handoff payload** (when another Versona or human picks up next): define minimally:

- **Summary** — what was concluded or challenged.
- **Open concerns** — severity and IDs if the concerns table is split across sessions.
- **Artifacts produced** — paths under `outputs/` (or recipe workspace) the consumer must read.
- **Recommended next actor** — which Versona kind or human gate (optional but reduces dropped context).

Other kinds use their **output variant** from the table in §2.

---

## 4. Severity and recommendation rubric

Use **consistent** labels across discipline Versonas so merged and family reports stay comparable.

### 4.1 Concern severity

| Level | Meaning |
|-------|---------|
| **critical** | Wrong or unsafe to proceed without addressing; may violate obligations, lose data, or block release evidence. |
| **significant** | Material risk or rework likely if ignored; should be resolved or explicitly accepted before commitment. |
| **minor** | Improvement or clarity; deferrable if team accepts small debt. |

### 4.2 Top-level recommendation

| Value | When to use |
|-------|-------------|
| **Proceed** | No significant or critical concerns, or only minor nits. |
| **Proceed with conditions** | Significant concerns exist but bounded mitigations or follow-up Sparks are agreed. |
| **Rework** | Critical or multiple significant issues; the work item is not fit for the current gate. |
| **Bank** | Intentionally pause; preserve context (strategic pause)—not a failure verdict. |

**Bank** is a Forge state choice; the Versona recommends it when continuing would waste effort until upstream facts change.

---

## 5. Process library (how to document a process)

A **process** is methodology-level: it describes *when* and *in what order* Versonas (and humans) act. Keep processes **abstract** in blueprints; project teams copy and specialize.

Each process document should include:

1. **Goal** — outcome of the process.
2. **Entry triggers** — ceremony, gate, or event that starts it.
3. **Inputs** — work items and artifacts required at start.
4. **Steps** — ordered **activities**, each with owner type: `Human` | `Versona:kind` | `Tasklet` | `Recipe`.
5. **Outputs** — artifacts and decisions produced.
6. **Downstream consumers** — next process, Versona, or Ember Log expectation.
7. **Diagram** — mermaid `sequenceDiagram` or `flowchart` showing handoffs.

Use the template [`../../../templates/forge/versona-process.template.md`](../../../templates/forge/versona-process.template.md) in the consuming repo or when adding examples under project `sdlc/`.

**Related patterns:** [`../process-and-flows.md`](../process-and-flows.md) (Forge lifecycle) · SDD process slots [`../../../templates/sdd/PROCESS-SLOT.template.md`](../../../templates/sdd/PROCESS-SLOT.template.md) if the team maps ceremonies to I/O.

---

## 6. Inter-Versona interaction patterns

| Pattern | Description |
|---------|-------------|
| **Router-first** | Invoke **routing** Versona; then 2–4 **discipline** Versonas it recommends. |
| **Sequential handoff** | Versona A produces a **handoff payload** (§3.3); human or script starts session for Versona B with `prior_session` set. |
| **Parallel merge** | **Family_aggregator** or manual invocations; consolidate concerns in one report (family template or custom merge). |
| **Meta + tasklets** | **Meta** Versona runs neutral **tasklets** ([`TASKLET-TAXONOMY.md`](../tasklets/TASKLET-TAXONOMY.md)); discipline overlay supplies severity and boundaries. |
| **Recipe then interpret** | **Recipe** writes under `agents/workspaces/<recipe>/` ([`ORCHESTRATION.md`](../../../../agents/ORCHESTRATION.md)); cognition Versona reads copies or linked paths—optionally copied into the session `inputs/` folder for a stable audit trail. |

```ks-diagram
key: sequence
alt: Diagram
```

---

## 7. Session storage (consuming repository)

### 7.1 Recommended layout

**Primary path** (aligns with Spark-level material under `forge-logs/` in [`../process-and-flows.md`](../process-and-flows.md)):

```text
forge-logs/
  versona/
    <actor>/
      <session-id>/
        SESSION.md           # manifest + human-readable index
        session.manifest.yaml # optional duplicate machine-readable manifest
        inputs/              # snapshots, pasted specs, links
        outputs/             # challenge reports, exports
        transcript.md        # optional LLM or tool transcript
```

**Alias:** Some teams prefer `forge/versona-sessions/<actor>/<session-id>/` to keep all of `forge/` self-contained. If you use the alias, **link** to the same SESSION fields and journal conventions below.

### 7.2 Actor folder

`<actor>` is an **opaque** label chosen by the team: OS username, initials, `shared` for pair/mob work, or a service identity. **Do not** require personally identifiable information in paths; follow org policy.

### 7.3 Session ID

Use a unique string: ISO timestamp + short slug (e.g. `2025-03-25T0930Z-spark-review`) or a UUID. Avoid spaces.

### 7.4 Manifest fields

Populate `SESSION.md` YAML frontmatter (and optionally mirror in `session.manifest.yaml`):

| Field | Required | Description |
|-------|----------|-------------|
| `session_id` | Yes | Same as folder name or stable UUID. |
| `started_at` | Yes | ISO-8601 datetime. |
| `work_item_refs` | Recommended | List of IDs/strings. |
| `work_item_kind` | Recommended | `ore` \| `ingot` \| `spark` \| `spike_discipline` \| `spike_general` \| `other` |
| `process_id` | Optional | Name of process template (if any). |
| `versona_kind` | Optional | From §2. |
| `discipline` | Optional | Display name when kind is `discipline`. |
| `parent_session` | Optional | Relative path to parent session folder for chains. |
| `ember_log_ref` | Optional | Path to `ember-logs/YYYY-MM-DD.md` and anchor or summary line. |
| `versona_session_schema_version` | Optional | Integer or semver string for the **session/manifest shape** this folder uses — enables migration notes when blueprints evolves fields (see [`MIGRATIONS.md`](MIGRATIONS.md)). Not enforced by blueprints v1. |

**Optional hints for exploration spikes** (not enforced by blueprints; for tooling or human clarity—see [`DISCIPLINE-SPIKE.md`](DISCIPLINE-SPIKE.md)):

| Field | Description |
|-------|-------------|
| `spike_timebox` | End date or duration (e.g. `2025-04-02` or `3d`). |
| `spike_hypothesis` | One-line question the spike must answer. |
| `anchor_notes` | Free text for product, roadmap, or WBS paths when ids are not yet stable. |

Copy the template from [`../../../templates/forge/versona-session.template.md`](../../../templates/forge/versona-session.template.md).

### 7.5 Git policy (team choice)

| Mode | Use when |
|------|----------|
| **Committed** | Audit trail, teaching, regulated context—keep `inputs/`/`outputs/` small or summarized. |
| **Gitignored** | Large transcripts, sensitive drafts—ignore `forge-logs/versona/**/transcript.md` or whole subtrees via `.gitignore`; keep Ember Log for **decisions** only. |

Document the team choice in `forge/` README or `sdlc/README.md`. Example ignore line (optional):

```gitignore
# Optional: local-only Versona sessions
# forge-logs/versona/
```

---

## 8. Logging and time alignment

### 8.1 Ember Log

When a session **records a decision**, **trade-off**, **risk acceptance**, or **scope change**, append an entry under `ember-logs/YYYY-MM-DD.md` using [`../scripts/forge-ember.sh`](../scripts/forge-ember.sh).

Example HTML comment pattern (after append) tying session to Sparks:

```markdown
---
<!-- spark_refs: [M1E1S2, M1E1S3] | decision_type: trade-off -->
```

Set `ember_log_ref` in the session manifest to that file (and heading if used).

### 8.2 Day journal

At end of day, record Versona usage in `forge/journal/YYYY-MM-DD.md`. Prefer **one row per session** (or per major activity) so traces line up with `forge-logs/versona/...`. Use the extended table in [`../daily/day-journal.template.md`](../daily/day-journal.template.md) (optional columns: session path, duration, process, outcome).

### 8.3 Time tracking

Blueprints does **not** ship a first-class time-tracking or ALM sync module. **Duration** fields are **optional** and manual (or supplied by external tools). Deeper integration is a separate initiative.

### 8.4 Scaffolding script

Optional helper: [`../scripts/forge-versona-session.sh`](../scripts/forge-versona-session.sh) creates a new session folder from templates and prints a line for the day journal.

---

## 9. Creating a new discipline Versona (checklist)

1. Choose kind **`discipline`** and follow [`VERSONA-CONTRACT.md`](VERSONA-CONTRACT.md).
2. Document **input interface** (what artifacts and IDs it needs) in the template or a short companion note.
3. If the Versona participates in a **process**, add or link a process doc (§5) with mermaid handoffs.
4. For **execution** steps, link to recipes under `agents/recipes/` per [`VERSONA-EXECUTION-TASKLETS.md`](../../../../agents/docs/VERSONA-EXECUTION-TASKLETS.md).
5. Calibrate **severity** using §4; test outputs against sample work items.
6. Recommend **session** use for multi-step engagements (§7).

---

## 10. Stable headings (for future site generators)

Major headings in this file are stable anchors: **Conceptual model**, **Versona kinds**, **Interface model**, **Severity and recommendation rubric**, **Process library**, **Inter-Versona interaction patterns**, **Session storage**, **Logging and time alignment**, **Creating a new discipline Versona**.
