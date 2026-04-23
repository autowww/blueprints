---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Forge tasklets — small Cursor operations

**Tasklets** are **single-operation** Cursor rules (`.mdc`) with a **fixed output shape**. A **meta-Versona** (for example **Sampling Versona**) can invoke them **in sequence** and merge results into a report shaped like a **§5** pass or other agreed structure (see [`VERSONA-CONTRACT.md`](../versona/VERSONA-CONTRACT.md)).

They are **not** a replacement for **discipline** Versonas (virtual personas for Product Management, BA, Testing, …). Use tasklets as **building blocks** and teaching aids.

Full taxonomy (execution plane, operation class, discipline overlay): [`TASKLET-TAXONOMY.md`](TASKLET-TAXONOMY.md).

### Mental model: layers

```blueprint-diagram
key: swimlane
alt: Diagram
```

### Install: file flow

```blueprint-diagram
key: swimlane
alt: Diagram
```

**Note:** **`versona-sampling.mdc`** ships with **`sync-forge-cursor-rules.sh sync --preset recommended`** (process-first default). This installer adds the **`forge-tasklet-*.mdc`** cognition rules; both layers can coexist.

## Install (project root)

From a repository that already contains the `blueprints/` submodule (run at **repository root**):

```bash
bash blueprints/sdlc/methodologies/forge/tasklets/install-tasklets.sh
```

Options:

| Flag | Effect |
|------|--------|
| `--dry-run` | Print planned copies only |
| `--force` | Overwrite existing files in `.cursor/rules/` |
| `--no-sampling` | Install only tasklets; skip `versona-sampling.mdc` |

Optional target directory (default: current directory):

```bash
bash blueprints/sdlc/methodologies/forge/tasklets/install-tasklets.sh /path/to/repo
```

## What gets installed

| Installed file | Purpose |
|----------------|---------|
| `.cursor/rules/forge-tasklet-extract-assumptions.mdc` | Pull explicit/implicit assumptions from text or context |
| `.cursor/rules/forge-tasklet-list-unknowns.mdc` | List unknowns, missing evidence, unresolved decisions |
| `.cursor/rules/forge-tasklet-quick-triage.mdc` | Short severity triage table (max five signals) |
| `.cursor/rules/forge-tasklet-route-request.mdc` | Suggest `@versona-*` routing table for a goal + work item |
| `.cursor/rules/forge-tasklet-bootstrap-session.mdc` | Session folder + SESSION.md frontmatter stub |
| `.cursor/rules/forge-tasklet-check-standards.mdc` | L1–L6 applicability checklist (not legal advice) |
| `.cursor/rules/forge-tasklet-log-event.mdc` | Classify event → Ember Log vs SESSION vs versona-track |
| `.cursor/rules/forge-tasklet-merge-outputs.mdc` | Mechanical merge of pasted tasklet / §5 fragments |
| `.cursor/rules/forge-tasklet-summarize-evidence.mdc` | Evidence path coverage map for verify/release |
| `.cursor/rules/versona-sampling.mdc` | Demo **meta-Versona** that runs the three tasklets and merges output |

**Skill matrix (which Versona uses which tasklet):** [`../versona/VERSONA-SKILL-MATRIX.md`](../versona/VERSONA-SKILL-MATRIX.md).

After install, tune **`globs:`** in each `.mdc` for your repo (defaults are empty = manual / @-rule invocation).

## Bundled meta-Versona

See **[`versona-sampling.mdc.template`](../versona/catalog/meta/versona-sampling.mdc.template)** — **Sampling Versona** demonstrates **meta-Versona + tasklets** with a simple, readable flow. Install copies it to `.cursor/rules/versona-sampling.mdc`.

## Relationship to execution-plane work

Tasklets in this folder are **cognition-plane** (in-IDE LLM only). **Docker / browser / API** steps belong in [`blueprints/agents/`](../../../../agents/README.md) recipes; a Versona can reference those as **execution tasklets** with a manifest — see [`agents/docs/VERSONA-EXECUTION-TASKLETS.md`](../../../../agents/docs/VERSONA-EXECUTION-TASKLETS.md). **Tooling split** (Rules, AGENTS.md, Skills, subagents, recipes): [`../VERSONA-OPERATING-MODEL.md`](../VERSONA-OPERATING-MODEL.md) §3. **Shared Skills** (session, standards, handoff, merge, evidence, diagrams): [`../../../templates/forge/cursor-skills/`](../../../templates/forge/cursor-skills/) and [`../versona/VERSONA-SKILL-MATRIX.md`](../versona/VERSONA-SKILL-MATRIX.md).

## See also

- [`../versona/README.md`](../versona/README.md) — Versona catalog
- [`../versona/VERSONA-CONTRACT.md`](../versona/VERSONA-CONTRACT.md) — output shape for full discipline Versonas
- [`../setup/README.md`](../setup/README.md) — Forge adoption and `forge-init.sh`
