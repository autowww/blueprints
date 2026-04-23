---
nav_title: Governance cadence for Blueprints rollout and submodule bumps
nav_group: onboarding
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Governance cadence for Blueprints rollout and submodule bumps

## What it is

**Phased rollout**, **office hours**, and **risk** handling that apply across single-team, multi-team, and platform rollouts.

**Parent page:** [Team rollout patterns](team-rollout.md).

## When to use it

Whenever more than a one-off email is needed to keep adoption healthy.

## Stakeholders (typical)

| Role | In cadence |
|------|------------|
| Tech lead / chapter | Brings recurring questions from teams |
| Platform owner | Owns golden SHA and bump comms |
| Enablement | Runs office hours and links to [Project setup checklist](SETUP.md) verify steps |

## Phased rollout

| Phase | Focus | Success signal |
|-------|---------|----------------|
| **Pilot** | One anchor repo + one squad | [Project setup checklist](SETUP.md) verify steps pass without one-off forks |
| **Expand** | Additional repos copy pin + scripts | Teams can state where baseline vs project text lives |
| **Standardize** | Golden SHA + office hours | New services reach parity without custom `blueprints/` edits |

### Rollout wave (sketch)

```blueprint-diagram-ascii
key: roadmap
alt: Pilot one anchor, expand with office hours, then standardize on golden SHA
expand: true
  Week 0–2        Week 3–6         Steady state
 [ Pilot ]  -->  [ Expand ]  -->  [ Standardize ]
   one repo      more repos       golden SHA + rituals
```

## Office hours

Short weekly slot for `forge-init`, Cursor rule sync, and “frozen vs project `sdlc/`” questions ([Blueprint policy](POLICY.md)).

## Risks and mitigations

| Risk | Mitigation |
|------|------------|
| Silent drift — teams interpret ceremonies differently | Shared **read order** + link to one methodology slice you standardize on |
| Submodule chaos — mixed SHAs in production repos | Published golden SHA + [Updating the submodule](updating-blueprints-submodule.md) as the shared ritual |
| Change fatigue | Keep office hours short; prioritize **verify** steps over reading volume |

## Anti-patterns

| Anti-pattern | Better |
|--------------|--------|
| Governance as paperwork only | Tie each phase to a **verify** or **bump** ritual people already do |
| Skipping pilot | Run [single-team](team-rollout-single-team.md) or small multi-team pilot before org-wide mandates |

## Example scenario (quarterly bump)

| | |
|--|--|
| **Starting situation** | Golden SHA moves quarterly; teams historically bumped ad hoc. |
| **Action taken** | Office hour the week after publish; one slide: “what changed” + link to [Updating the submodule](updating-blueprints-submodule.md). |
| **Expected result** | Most teams bump inside two weeks; stragglers are visible. |
| **What to check** | Exception list shrinks or is explicit. |

## How to verify success

Teams use the same rituals for bumps and questions; drift is visible and corrected in office hours.

## What to do next

- [Team rollout patterns](team-rollout.md)
- [Troubleshooting / FAQ](troubleshooting-faq.md)
