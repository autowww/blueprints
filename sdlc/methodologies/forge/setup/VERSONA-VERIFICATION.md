---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Verification — process-first Versona install (local / manual primary)

**Goal:** Confirm that **Cursor rules**, optional **Skills / tasklets / recipes**, and **artifact paths** match **`blueprints`** expectations after setup or submodule bump.

## 1. Tooling prerequisites

- **Python 3** on the PATH.
- **PyYAML** for **`check`**: `pip install pyyaml` (or distro package).

## 2. Cursor rules: `check`, `status`, `diff`

From the **consuming repository root** (with **`blueprints/`** and **`forge/forge.config.yaml`**), using the same **`--preset`** (and **`--with-*`**) flags you rely on in practice:

```bash
# Expected Versona files from YAML exist on disk
bash blueprints/sdlc/methodologies/forge/setup/sync-forge-cursor-rules.sh check

# Per-file: missing / drift / ok (exit 1 if any problem)
bash blueprints/sdlc/methodologies/forge/setup/sync-forge-cursor-rules.sh status --preset recommended

# Aggregate SHA diff vs blueprints templates
bash blueprints/sdlc/methodologies/forge/setup/sync-forge-cursor-rules.sh diff --preset recommended
```

**Pass criteria:** **`check`** exits **0**. **`status`** exits **0** (no missing files, no SHA mismatch for the job list). **`diff`** exits **0** when clean.

After a clean **`sync`**, expect **`.forge/cursor-rules-manifest.json`** with per-rule **`source_sha256`** / **`installed_sha256`** and **`blueprints_commit`** when **`blueprints/`** is a git checkout.

**Optional:** `… sync --preset recommended --write-adoption-manifest` writes **`.forge/versona-adoption-manifest.json`** (pointers only; not verified by **`diff`**). See [`CURSOR-RULES-ALIGNMENT.md`](CURSOR-RULES-ALIGNMENT.md) § Manifest split.

## 3. Scaffold sanity

After **`forge-init.sh`**:

- **`forge/forge.config.yaml`** exists.
- **`forge-logs/`** and **`forge-logs/versona-track/`** exist (placeholders for optional ledger / graph per [`../VERSONA-OPERATING-MODEL.md`](../VERSONA-OPERATING-MODEL.md)).

## 4. End-to-end example (one request → evidence → diagram hook)

This is a **realistic manual trace**; filenames are illustrative. Adjust **`session-id`** and **`actor`** to your convention.

1. **Intake** — User request: *“Review API story X for security and testing gaps before build.”*  
   Optional (enriched): append one line to **`forge-logs/versona-track/request-ledger.jsonl`** per [`../schemas/request-ledger-entry.schema.json`](../schemas/request-ledger-entry.schema.json).

2. **Routing** — Invoke **`versona-all`** (or **`forge-versona`**) so the model proposes **Security** + **Testing** (and **Software Engineering** if needed). Installed rules come from **`sync --preset recommended`**.

3. **Sessions** — Open folders:
   - **`forge-logs/versona/security/sec-2026-0411-api-x/`**
   - **`forge-logs/versona/testing/tst-2026-0411-api-x/`**  
   Add **`SESSION.md`**; optional **`session.manifest.json`** linking **`work_item_refs`** to the story / Spark.

4. **Events (optional)** — Append **`graph-analytics.jsonl`** lines under **`forge-logs/versona-track/`** when analytics is enabled ([`../schemas/graph-analytics-record.schema.json`](../schemas/graph-analytics-record.schema.json)).

5. **Artifacts** — Each Versona writes §5-style output under **`outputs/`** (e.g. **`section5-security.md`**, **`section5-testing.md`**) per [`../versona/ARTIFACT-CONTRACTS.md`](../versona/ARTIFACT-CONTRACTS.md). If chaining, add **`outputs/handoff.json`** for the next Versona.

6. **Evidence** — Assemble or link materials under **`forge/evidence/api-x-preflight/`** (team-defined **`pack-id`**). Use Skill / recipe stubs as needed: **`versona-evidence-pack-assemble`** ([`../../../../agents/templates/recipe/versona-evidence-pack-assemble/README.md`](../../../../agents/templates/recipe/versona-evidence-pack-assemble/README.md)).

7. **Kitchen-sink–compatible diagram** — Under the session, **`diagrams/`**: store **diagram IR** (e.g. **`threat-context.diagram.json`**) and optionally **rendered SVG**. Register files in **`artifact-manifest.json`** with **`diagram_ir`** / **`diagram_rendered`** per [`../VERSONA-OPERATING-MODEL.md`](../VERSONA-OPERATING-MODEL.md) §5. For headless export wiring, copy **`versona-kitchensink-diagram-export`** from [`../../../../agents/templates/recipe/versona-kitchensink-diagram-export/README.md`](../../../../agents/templates/recipe/versona-kitchensink-diagram-export/README.md) into **`agents/recipes/`** and align **`run.sh`** with your **`forgesdlc-kitchensink`** or site generator.

**Done when:** Routing ran the right Versonas, session **`outputs/`** exist, evidence pack is coherent, and diagram artifacts are registered (or explicitly skipped by team policy).

## 5. Optional: Cloud Agent / automation follow-up

The **primary** story above is **local Cursor + git-tracked files**. For **CI or Cloud Agent** runners:

- Reuse the same **`check` / `status` / `diff`** commands in a job after submodule checkout.
- Mount the repo so **`blueprints/`** resolves like a developer machine; gate merges on **`check`** + **`status`** for the chosen preset.
- Keep **secrets** (tokens, GRC URLs) out of **`versona-adoption-manifest.json`**; that file is **documentation-shaped**, not a vault.
- Recipes under **`agents/recipes/`** are the natural place to script **`run.sh`** invocations; see [`../../../../agents/STRUCTURE.md`](../../../../agents/STRUCTURE.md).

Do **not** require Cloud Agent adoption for teams that only use local Cursor; treat automation as **additive**.

## Related

- [`CURSOR-RULES-QUICKSTART.md`](CURSOR-RULES-QUICKSTART.md)  
- [`VERSONA-PROCESS-MODEL-MIGRATION.md`](VERSONA-PROCESS-MODEL-MIGRATION.md)  
- [`../versona/VERSONA-SKILL-MATRIX.md`](../versona/VERSONA-SKILL-MATRIX.md)  
