---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Defect triage, RCA, and ISTQB-oriented test impact — prompt

**Purpose:** Operational prompt for an AI assistant acting as **QC / Testing / RCA orchestrator** in a **Forge SDLC**, **markdown-canonical** repo. Produces **traceable**, **estimable**, **testable** defect workflow artifacts.

**Related:** [`../../../disciplines/engineering/testing/README.md`](../../../disciplines/engineering/testing/README.md) (ISTQB hub) · [`../../../disciplines/engineering/testing/APPROACHES.md`](../../../disciplines/engineering/testing/APPROACHES.md) (techniques) · [`../../methodologies/forge/versona/catalog/discipline/engineering/versona-testing.mdc.template`](../../methodologies/forge/versona/catalog/discipline/engineering/versona-testing.mdc.template) · [`../../methodologies/markdown-canonical-workspace-policy.md`](../../methodologies/markdown-canonical-workspace-policy.md) · [`estimation/ESTIMATION-RULES.template.md`](estimation/ESTIMATION-RULES.template.md) · [`../../methodologies/forge/versona/ARTIFACT-CONTRACTS.md`](../../methodologies/forge/versona/ARTIFACT-CONTRACTS.md)

---

## Layout (consuming repo)

| Path | Role |
|------|------|
| `docs/defects/INDEX.md` | Registry of defect IDs and status |
| `docs/defects/DEF-NNNN/defect.md` | **Single source** for triage, repro, severity, links |
| `docs/defects/DEF-NNNN/rca.md` | Root-cause analysis (may stay **draft** until fixed) |
| `docs/defects/DEF-NNNN/test-impact.md` | ISTQB-oriented confirmation/regression plan |
| `docs/defects/DEF-NNNN/evidence/` | Screenshots, logs (optional; large binaries **gitignore** per `AGENTS.md`) |
| `docs/requirements/TRACEABILITY.md` | Link **defect id** ↔ **requirement** / **Forge Spark** |
| `docs/testing/TRACEABILITY.md` | **Optional** — tests ↔ requirements; **omit** if the repo keeps all trace rows in `docs/requirements/TRACEABILITY.md` only |

Declare the chosen pattern in **`docs/PROJECT.md`**.

---

## How to use

1. Ensure **`docs/defects/`** exists or create it from this prompt’s outputs.  
2. Copy from **“Act as QC / Testing…”** through **“G. Open evidence gaps”**.  
3. Paste defect text into the fence.  
4. Pair with **`@versona-testing`** when the team wants a formal **§5** Testing Versona session in `forge-logs/versona/`.

---

## Prompt body (copy from here)

Act as **QC / Testing / RCA orchestration** assistant for this **Forge SDLC** workspace.

Analyze the defect below and create a **defect workflow** that is **traceable**, **estimable**, and **testable**.

**Defect input:**

```
<<<PASTE DEFECT OR IMPORTED RECORD HERE>>>
```

**Workspace rules**

- **Canonical artifacts:** `.md` only (no CSV SoT).  
- **Forge terms:** relate defects to **requirement** ids, **Ingot** / **Forge Spark** ids where applicable; **Product Spark** for release/Assay context only.  
- **Estimation:** apply **`forge/estimation/ESTIMATION-RULES.md`** (defect **ambiguity**, **blast-radius**, **RCA uncertainty** multipliers) and update **`docs/requirements/ESTIMATES.md`** or defect front matter.  
- **ISTQB vocabulary:** use standard **test levels**, **test types**, and **test design techniques** per [`blueprints/disciplines/engineering/testing/APPROACHES.md`](../../../disciplines/engineering/testing/APPROACHES.md).

**Tasks**

1. **Classify** defect **type** (functional, regression, performance, security, usability, data, environment, …), **severity** (e.g. blocker / major / minor / trivial — align to team scale in `docs/PROJECT.md`), and **likely impact** (users, data, compliance, ops).

2. **Search** for existing same/similar defects in:  
   - `docs/defects/INDEX.md`  
   - `docs/defects/**`  
   - `docs/requirements/TRACEABILITY.md`  
   - Related **requirement** / **Forge Spark** Markdown under `docs/requirements/**`

3. Choose **exactly one** canonicalization **action** **A–G** from [`markdown-canonical-workspace-policy.md`](../../methodologies/markdown-canonical-workspace-policy.md), mapped to intent:  
   - **A** — keep existing defect; reject or **reference** duplicate incoming  
   - **B** — **update** existing defect with new evidence  
   - **C** — **merge** incoming into existing defect record  
   - **D** — **distinct** defect; **cross-link** related  
   - **E** — **split** into multiple defects  
   - **F** — **replace** obsolete defect record (deprecate old)  
   - **G** — consolidate multiple stale records into one new **DEF-** id  

4. List **missing evidence** and add an **evidence checklist** (logs, version, build, account state, screenshots, network trace).

5. **Create or update** `defect.md` with YAML front matter and body fields including:  
   - `id` (`DEF-NNNN`)  
   - `related_requirements`  
   - `related_ingots` / `related_forge_sparks`  
   - `environment`  
   - **reproduction steps**  
   - **expected vs actual**  
   - `suspected_component`  
   - `repos`  
   - `est_fib` / `est_tshirt` / `risk_multiplier` (per estimation rules)  
   - `canonicalization` (**A–G** + target id if merged)

6. **Draft `rca.md`** structure:  
   - **Symptom**  
   - **Probable causes** (hypotheses)  
   - **Most likely root cause** (confidence)  
   - **Why escape was possible** (test/process gap)  
   - **Corrective action** (fix)  
   - **Preventive action** (CI, lint, monitoring, training)

7. **Estimate** using workspace model; flag **high uncertainty** until repro confirmed.

8. **Test design (ISTQB):** in `test-impact.md`, propose **confirmation** and **regression** coverage using techniques where relevant:  
   - **Equivalence partitioning**  
   - **Boundary value analysis**  
   - **Decision tables**  
   - **State transition** testing  
   - **Exploratory** testing (charter + timebox)  
   - **Checklist-based** testing  

9. **Suites:** list **existing** automated/manual suites to **rerun**; propose **missing** suites (name, scope, owner, automation feasibility).

10. **Files to touch** (create/update as needed):  
    - `docs/defects/INDEX.md`  
    - `docs/defects/DEF-XXXX/defect.md`  
    - `docs/defects/DEF-XXXX/rca.md`  
    - `docs/defects/DEF-XXXX/test-impact.md`  
    - `docs/testing/TRACEABILITY.md` **or** only `docs/requirements/TRACEABILITY.md` (per repo convention)  
    - Related **requirement** / **Spark** / **task** files  
    - `docs/requirements/ESTIMATES.md` (defect row)  
    - `imports/cursor-history/IMPORT-LEDGER.md` if defect came from import  

**Execution mode:** Apply **direct** Markdown edits when possible; else output **exact** paths and full Markdown.

**Return**

**A. Defect triage result**  
**B. Canonicalization decision** (**A–G** + rationale)  
**C. RCA draft** (structured)  
**D. Test-impact proposal** (ISTQB-aligned)  
**E. Estimation** (Fibonacci/t-shirt/tokens + multipliers)  
**F. Markdown file changes** (path + action)  
**G. Open evidence gaps**

---

## Maintainer notes

- **Versona split:** This prompt **orchestrates** artifacts; **`versona-testing`** owns **testing strategy §5** depth; **`versona-se`** / **`versona-architecture`** for fix design; **`versona-pm`** for **priority** and **release**; **`versona-estimation`** for **sizing method** calibration.  
- **Security defects:** invoke **`versona-security`** when impact crosses abuse / data exposure.  
- **Ember Log:** significant **acceptance of risk** or **scope** change belongs in `ember-logs/YYYY-MM-DD.md`.
