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
alt: Process flow
title: Tasklet cognition layers
summary: How single-operation tasklets stack under a meta-Versona that sequences them into a bounded, reviewable report.
node: Process flow
detail: Frames how cognition tasklets and meta-Versonas relate on this page.
more: Tasklets are fixed-shape Cursor rules; discipline Versonas remain the full passes for PM, BA, Testing, and similar lenses.
node: Lane A ──► handoff ──► shared outcome
detail: Sequential tasklet invocations hand outputs toward one merged report shape.
more: A meta-Versona such as Sampling Versona runs extract-assumptions, list-unknowns, and quick-triage in order before merge.
node: Lane B ──► inspect / adapt ──► feedback
detail: Inspect-and-adapt loops refine tasklet outputs before merge or downstream Versona work.
more: Teams tune globs, merge fragments, or escalate to full discipline Versonas when tasklet scope is insufficient.
node: Note: `versona-sampling.mdc`
detail: Points to the bundled meta-Versona that demonstrates the tasklet sequence.
more: Install or sync copies the template; it merges tasklet outputs into a readable demo report, not a discipline substitute.
fallback_ascii: |
  Process flow

  Lane A ──► handoff ──► shared outcome
  Lane B ──► inspect / adapt ──► feedback

  Note: `versona-sampling.mdc`
```

### Install: file flow

```blueprint-diagram
key: swimlane
alt: Process flow
title: Tasklet install file flow
summary: How install-tasklets.sh copies cognition rules into `.cursor/rules/` with optional sampling meta-Versona.
node: Process flow
detail: Frames what the installer places on disk at repository root.
more: Run from a repo that already contains the blueprints submodule; defaults target the current directory as project root.
node: Lane A ──► handoff ──► shared outcome
detail: Installer copies forge-tasklet rules into `.cursor/rules/` as the shared outcome.
more: Nine cognition tasklets cover assumptions, unknowns, triage, routing, session bootstrap, standards, logging, merge, and evidence summary.
node: Lane B ──► inspect / adapt ──► feedback
detail: Optional flags and dry-run inspect the install plan before overwriting files.
more: `--dry-run` prints planned copies; `--force` overwrites existing rules; `--no-sampling` skips versona-sampling.mdc.
node: Note: `versona-sampling.mdc`
detail: Marks the optional meta-Versona copied alongside tasklet rules unless skipped.
more: Also ships via sync-forge-cursor-rules.sh recommended preset; both install paths can coexist in `.cursor/rules/`.
fallback_ascii: |
  Process flow

  Lane A ──► handoff ──► shared outcome
  Lane B ──► inspect / adapt ──► feedback

  Note: `versona-sampling.mdc`
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
