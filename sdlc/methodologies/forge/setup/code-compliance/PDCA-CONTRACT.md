# PDCA contract — code-footprint compliance

Machine and operator contract for `workbench/code-compliance/lib/pdca_engine.py`.

## Phases

| Phase | Input | Output | Notes |
|-------|--------|--------|-------|
| **SETUP** | Clean source repo, campaign config | Worktree, `scan-baseline.json`, `code-footprint.mdc` in worktree | `git worktree add -b <work-branch>` |
| **PLAN** | `scan-latest.json` | `plan-iteration-N.md`, target file list | One primary file per iteration (worst `poor` then `risky`) |
| **DO** | `prompt-iteration-N.md` | `agent-transcripts/iteration-N.log` | Cursor CLI `agent`; edits only in worktree |
| **CHECK** | Re-scan + `git diff --stat` | Updated `scan-latest.json` | Compare actionable counts |
| **ACT** | CHECK result | Checkpoint advance, rollback, exception, or terminal | See outcomes |

## Checkpoints

- Before each **DO**, tag `compliance-checkpoint-<N>` in the worktree.
- **Regression** (more `poor`+`risky`): `git reset --hard compliance-checkpoint-<N>`.
- **Stall** (no improvement for `max_stall_iterations`): mark path `exception_required` in `state.json` and skip on later iterations.

## Terminal outcomes

| Outcome | Condition | PR |
|---------|-----------|-----|
| `COMPLIANT` | Zero `risky`/`poor` at configured profile | Yes (default) |
| `MAX_EFFORT` | `max_iterations` or no targets left except exceptions | Only if `--pr-on-max-effort` |
| `DRY_RUN` | `--dry-run` after first PLAN | No |
| `ABORTED` | Dirty source repo | No |

## Exception registry

Paths listed in `state.json` → `exceptions` are skipped after repeated stalls. Document human follow-up in `compliance-report.md` and optional ADR.

## Campaign artifacts

```
campaigns/<campaign_id>/
  campaign.yaml
  state.json
  scan-baseline.json
  scan-latest.json
  plan-iteration-*.md
  prompt-iteration-*.md
  agent-transcripts/
  compliance-report.md
  worktrees/<repo_slug>/
```

## Resume

`--resume` continues from `state.json` (`phase`, `iteration`, `exceptions`). Do not delete `worktrees/` while resuming.
