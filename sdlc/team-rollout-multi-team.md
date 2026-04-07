---
nav_title: "Team rollout: Multi-team"
nav_group: onboarding
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Team rollout — Multi-team

## What it is

Coordinating the same **golden** `blueprints` commit and bump cadence across **several product repos**.

**Parent page:** [Team rollout patterns](team-rollout.md).

## When to use it

A chapter or org has several products that should share vocabulary and submodule pins.

## Prerequisites

- [Single-team](team-rollout-single-team.md) patterns in place or a clear anchor repo.

## Focus

| Aspect | Guidance |
|--------|----------|
| **Golden SHA** | Platform or architecture publishes an approved `blueprints` commit; product repos bump on a cadence ([Updating the submodule](updating-blueprints-submodule.md)). |
| **Ownership** | Named owner for bumps and communication when the SHA changes. |

## Stakeholders (typical)

| Role | Expectation |
|------|-------------|
| Platform / architecture | Publishes approved pointer and **why** it changed (security, methodology release) |
| Product teams | Bump on cadence or approved lag; no silent pins |
| Security / compliance | May require evidence of bump — tie to the same published SHA |

## Phased timeline (example)

| Phase | Focus | Success signal |
|-------|-------|----------------|
| **Align** | Agree golden SHA + owner | One channel (doc or chat) announces bumps |
| **Pilot** | Two or three repos on the new pin | Same [SETUP](SETUP.md) verify story |
| **Expand** | Remaining repos | Drift visible in CI or release notes |

## Risks and mitigations

| Risk | Mitigation |
|------|------------|
| Mixed SHAs in production | Published golden SHA + single bump ritual |
| Teams skip reading release notes | Short “what changed” with each bump |

## Anti-patterns

| Anti-pattern | Better |
|--------------|--------|
| Ad-hoc bumps per repo without announcement | Batch or calendar cadence + comms |
| Letting product repos diverge “until later” | Time-box lag with a named date |

## Example scenario (multi-product program)

| | |
|--|--|
| **Starting situation** | Five services must share vocabulary; two already pin an older SHA. |
| **Action taken** | Architecture publishes target SHA and cutoff; teams file exceptions instead of silent drift. |
| **Expected result** | All five converge; exceptions are rare and documented. |
| **What to check** | Release or CI shows bump commits aligned to the published pointer. |

## How to verify success

Repos converge on the same approved pointer; teams explain baseline vs project text.

## What to do next

- [Platform / org rollout](team-rollout-org-platform.md)
- [Team rollout patterns](team-rollout.md)
- [Updating the Blueprints submodule](updating-blueprints-submodule.md) · [Troubleshooting / FAQ](troubleshooting-faq.md)
