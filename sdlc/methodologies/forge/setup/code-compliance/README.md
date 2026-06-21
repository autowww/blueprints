# Code-footprint compliance campaigns (Forge setup)

Automated **PDCA** remediation for file-footprint standards using the workbench orchestrator and Cursor CLI.

## When to use

- A repo has **`risky`/`poor`** findings from `code_footprint_scan.py` at profile **tight**
- You want an isolated **worktree**, checkpoint **rollback**, and a **PR** with a compliance report
- You do **not** want mechanical line splits — the agent follows [`agentic-coding-standards.md`](../../../agentic-coding-standards.md) (semantic packages, `README.md`/`INDEX.md`)

## When not to use

- Generated trees (`website/`, `showcase/`) — excluded by the scanner; fix generators instead
- One-off manual splits — run the scanner and edit directly
- UX/a11y/design-contract loops — use Kitchen Sink website-ux-auditor instead

## Operator entry

From a machine with the multi-repo **`Code/`** hub:

```bash
cd /path/to/Code/workbench/code-compliance
./run-code-compliance-pdca.sh --repo <slug> --dry-run   # plan + baseline
./run-code-compliance-pdca.sh --repo <slug>             # full loop
```

See [workbench README](../../../../../workbench/code-compliance/README.md) in the workspace hub (`Code/workbench/`), when blueprints and workbench are sibling folders under `Code/`.

## Prerequisites

1. Propagate footprint rule (optional if already present):

   ```bash
   bash sdlc/methodologies/forge/setup/propagate-code-footprint-rules.sh /path/to/Code
   ```

2. Clean source checkout for the target repo.

3. `agent` and `gh` on `PATH` for full campaigns.

## Branching

Aligns with Forge Team tier: `feature/compliance-footprint-<slug>-<date>` from `main` unless `--base-branch` / `--work-branch` override. See [PDCA-CONTRACT.md](PDCA-CONTRACT.md).

## Related tools

| Tool | Role |
|------|------|
| [`code_footprint_scan.py`](../code_footprint_scan.py) | Readonly CHECK input |
| [`propagate-code-footprint-rules.sh`](../propagate-code-footprint-rules.sh) | Install `code-footprint.mdc` |
| [`sync-forge-cursor-rules.sh`](../sync-forge-cursor-rules.sh) | Full Versona sync (`--with-code-footprint-rules`) |
