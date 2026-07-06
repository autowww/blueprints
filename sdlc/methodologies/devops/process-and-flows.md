---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# DevOps — major processes & flow maps

## 1. CI/CD pipeline (conceptual)

```blueprint-diagram
key: linear
alt: CI/CD pipeline (conceptual)
title: CI/CD commit-to-deploy pipeline
summary: How each commit advances through build, test, scan, and deploy with gated progression.
node: Start
detail: A commit or merge triggers the automated pipeline run.
more: Every commit initiates the sequence; small, frequent commits keep feedback loops short and reviewable.
node: Core steps (see walkthrough below)
detail: Build, test, scan, and deploy execute in governed sequence.
more: Failures at any stage block progression; teams treat the pipeline as the single source of deployment readiness.
node: Outcome
detail: A deployable artifact or blocked release decision is recorded.
fallback_ascii: |
  CI/CD pipeline (conceptual)

  Start
      |
      v
  Core steps (see walkthrough below)
      |
      v
  Outcome
```

## 2. DevOps infinity loop

```blueprint-diagram
key: linear
alt: DevOps infinity loop
title: DevOps continuous feedback loop
summary: How operational signals cycle back into planning, build, test, release, and monitoring.
node: Start
detail: A delivery or operational signal enters the DevOps cycle.
node: Core steps (see walkthrough below)
detail: Planning, code, infrastructure, test, release, and monitor stages interconnect.
more: DevOps is not linear; monitoring informs the next planning cycle and production-like testing shapes the next build.
node: Outcome
detail: Improved delivery posture feeds the next loop iteration.
fallback_ascii: |
  DevOps infinity loop

  Start
      |
      v
  Core steps (see walkthrough below)
      |
      v
  Outcome
```

## 3. Incident response flow

```blueprint-diagram
key: decision
alt: Incident response flow
title: Governed incident response gate
summary: How severity and readiness checkpoints route incidents toward coordinated response or escalation.
node: Current state
detail: An active alert or production incident enters structured response.
more: Teams replace ad-hoc firefighting with defined roles; severity sets the initial response level.
node: Checkpoint / gate
detail: Confirm severity, scope, and whether the response bar is met.
more: Incident commanders coordinate complex events; post-mortems capture learning from significant incidents.
node: refine or escalate
detail: Rework triage or escalate when the gate does not clear.
node: Continue flow
detail: Proceed with coordinated mitigation and communication per severity.
fallback_ascii: |
  Incident response flow

  Current state
      |
      v
  Checkpoint / gate
      |
      +-- no ──► refine or escalate
      |
     yes
      v
  Continue flow
```

## 4. Deployment strategy decision

```blueprint-diagram
key: decision
alt: Deployment strategy decision
title: Deployment strategy selection gate
summary: How risk tolerance and rollback needs route releases toward rolling, canary, blue-green, or flag-based paths.
node: Current state
detail: Capture release scope, risk profile, and rollback requirements.
node: Checkpoint / gate
detail: Test whether the candidate strategy meets tolerance and observability needs.
more: Rolling updates are simplest; canary uses subset traffic; blue-green enables instant rollback; flags decouple deploy from user-visible release.
node: refine or escalate
detail: Revisit strategy choice or escalate when the gate fails.
node: Continue flow
detail: Proceed with the selected deployment approach into release execution.
fallback_ascii: |
  Deployment strategy decision

  Current state
      |
      v
  Checkpoint / gate
      |
      +-- no ──► refine or escalate
      |
     yes
      v
  Continue flow
```

## 5. Phases A–F (DevOps emphasis)

| Blueprint phase | DevOps emphasis | Key practice |
|-----------------|-----------------|-------------|
| A Shape | Include operability requirements (SLOs, monitoring needs) | Shift-left on operational thinking |
| B Plan | Pipeline design; deployment strategy; environment planning | IaC from the start |
| C Build | CI: automated build, test, scan on every commit | Trunk-based development; small, frequent commits |
| D Verify | Automated test pyramid; security scanning; performance testing | Quality gates in the pipeline |
| E Release | CD: automated deployment; canary/blue-green; feature flags | Make deployments boring |
| F Learn | Monitoring, alerting, incident response, post-mortems | Production feedback closes the loop |

## 6. DORA metrics collection

```blueprint-diagram
key: linear
alt: DORA metrics collection
title: DORA metrics collection flow
summary: How teams gather delivery signals aligned with DORA research-backed metrics and capabilities.
node: Start
detail: Operational and delivery events enter the metrics collection flow.
node: Core steps (see walkthrough below)
detail: Instrument pipelines and production to capture delivery capability signals.
more: DORA State of DevOps defines research-backed metrics and capabilities teams can adopt for bounded comparison.
node: Outcome
detail: Reviewable metrics support prioritizing DevOps capability improvements.
fallback_ascii: |
  DORA metrics collection

  Start
      |
      v
  Core steps (see walkthrough below)
      |
      v
  Outcome
```

## 7. Flow details (walkthrough)

**CI/CD pipeline** — Every commit triggers an automated pipeline. Build, test, scan, deploy in sequence. Failures at any stage block progression. The pipeline is the **single source of truth** for deployment readiness.

**Infinity loop** — DevOps is not a linear process; it is a continuous cycle. Planning incorporates operational learnings. Code includes infrastructure. Testing includes production-like environments. Monitoring informs the next planning cycle.

**Incident response** — Structured, not ad-hoc. Severity determines response level. Incident commanders coordinate complex responses. Post-mortems extract learning from every significant incident.

**Deployment strategies** — Choose based on risk tolerance. Rolling updates are simplest. Canary releases test with a subset of traffic. Blue-green provides instant rollback. Feature flags decouple deployment from user-visible release.

## 8. Authoritative sources & further reading

- [Wikipedia — DevOps](https://en.wikipedia.org/wiki/DevOps) — Stable overview of practices and culture.
- [Wikipedia — CI/CD](https://en.wikipedia.org/wiki/CI/CD) — Continuous integration and delivery.
- [DORA — State of DevOps](https://dora.dev/) — Research-backed metrics and capabilities.
- [Google SRE Book](https://sre.google/sre-book/table-of-contents/) — Free online; SRE practices and principles.

Full curated list: [`REFERENCE-LINKS.md`](../REFERENCE-LINKS.md).

## 9. Internal links

- [Ceremonies](ceremonies-prescriptive.md) · [Overview](https://forgesdlc.com/methodologies-devops.html)
