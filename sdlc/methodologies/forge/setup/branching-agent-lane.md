---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Agent lane (`agent/*`) — branch policy for autonomous coding agents

Prescriptive policy for repos that let **governed agents** (for example a Matrix-driven coding bot running in a Fleet-managed container) modify code. It sits on top of the [branching conventions](BRANCHING-STRATEGY.md) and the optional [lane model](charge-plans/branching/README.md); it does not replace them.

**Why a separate lane:** an agent has no judgment about whether `main` is safe to touch, cannot be asked a clarifying question mid-push, and may be running on a host the operator cannot log into. The lane makes every agent change a reviewable, revertible, attributable branch with a recorded approval.

---

## Lane definition

| Item | Rule |
|---|---|
| Name | `agent/<agent-id>/<task-id>-<slug>` — `<agent-id>` is the registered agent (`roadrunner`, `reviewer`); `<task-id>` is the approval request id; `<slug>` is 2–5 lowercase words joined by `-` |
| Source | A **fresh** fetch of `origin/<integration>` (normally `main`) at task start. The commit it starts from is recorded as `base_sha` in the task envelope and in the PR body |
| Who may push | Only the agent identity (bot user or scoped token) and only to `agent/**`. Humans do not push to agent branches; they review |
| Commits | `type(scope): summary` per the repo scopes, plus trailers `Forge-Task: <task-id>` and `Forge-Approval: <approval record id>` |
| Rebase | Before the first push the agent rebases on current `origin/<integration>`. A conflict stops the task (`HELD`); the agent never resolves conflicts on its own and never force-pushes |
| Pull request | Mandatory. Title = squash subject. Body = task goal, `base_sha`, verify commands and exit codes, test instructions for a human |
| Merge | Squash, executed by the **review identity** (a different agent or a human), only after (1) the operator confirms the change works, (2) the reviewer's independent verification on the pushed SHA passes, (3) no critical finding is open |
| Critical finding | Merge conflict with current integration branch; files outside the task's allowed paths; touches on denied paths (CI workflows, secrets, lockfiles unless explicitly allowed); verify failure on the reviewer's run; secrets-pattern hit; failing required check. Any of these require a **human approval record** before merge |
| Lifetime | Deleted on merge. Unmerged agent branches with no open PR expire after **14 days** |
| Forbidden | Direct push to `main`; `--force` / `--force-with-lease` after a PR exists; an agent merging its own PR; creating `charge/*` branches |

---

## Freshness

1. Clone or fetch `origin/<integration>`; record `base_sha`.
2. Work on `agent/...` only.
3. Before push: `git fetch origin <integration>` → `git rebase origin/<integration>`.
4. If the rebase stops: abort, report `HELD(stale_conflict)` with the conflicting paths. A human (or a new approved task) decides.
5. The reviewer repeats the mergeability check at review time; a branch that went stale between push and review is `HELD`, not merged.

Submodule-producing repos: after an agent change is merged, each consumer bump is its **own** approved task, never an implicit side effect (same rule as the lane model's "manifest or submodule pin updates are explicit Sparks").

---

## Approval and record

Approval for the agent to **start** is a record bound to the exact task (goal, repo, base ref, allowed paths, verify commands), not a chat sentence. Confirmation that the result **works** is a separate, lighter signal from the operator after testing the branch locally. Neither replaces the other. See the platform [approval model](https://platform.forgesdlc.com/docs-approval-model.html).

---

## Host-side protection (GitHub example)

- Ruleset on `main`: require pull request, one approval, required status check (`ci`); block force-push and deletion.
- Ruleset on `agent/**`: allow create/update for the bot actor only; block deletion by anyone other than the reviewer identity and repo admins.

Apply per repository; keep the ruleset JSON next to the repo's `docs/GIT-WORKFLOW.md`.

---

## Relationship to the lane model

| Lane | Agent lane interaction |
|---|---|
| `iter/*` | An agent task may target `iter/<x>` as its integration branch when the repo records that in `forge/branching.yml`; the lane rules above are unchanged |
| `spark/*` | Humans only. Agents do not create `spark/*` |
| `spike/*` | Humans only |
| `release/*`, `hotfix/*` | Agents may not target these without a repo-specific policy entry |

Record the choice in `forge/branching.yml` under `agent_lane:` (`integration`, `agent_ids`, `allow_paths`, `deny_paths`, `ttl_days`).
