# SRE and observability (blueprint)

Site Reliability Engineering (SRE) and observability are complementary practices that ensure production systems are reliable, understandable, and continuously improving. SRE provides the **operational framework** (SLOs, error budgets, toil reduction); observability provides the **technical capability** to understand system behavior.

This guide covers SLOs/SLIs/error budgets, the three pillars of observability, alerting philosophy, chaos engineering, on-call practices, and incident learning.

---

## 1. SRE foundations

### SLOs, SLIs, and error budgets

| Concept | Definition | Example |
|---------|-----------|---------|
| **SLI** (Service Level Indicator) | A quantitative measure of service behavior | Request latency P99, error rate, availability |
| **SLO** (Service Level Objective) | Target value for an SLI over a time window | P99 latency < 200 ms over 30 days; availability >= 99.9% per quarter |
| **SLA** (Service Level Agreement) | Contractual commitment (SLO + consequences) | 99.9% uptime; credits issued below threshold |
| **Error budget** | Allowed unreliability = 1 - SLO | 99.9% SLO → 0.1% error budget → ~43 min downtime/month |

### Error budget policy

| Budget status | Action |
|---------------|--------|
| **Healthy** (> 50% remaining) | Normal development velocity; feature work prioritized |
| **Caution** (25–50% remaining) | Increase review rigor; prioritize reliability improvements alongside features |
| **Critical** (< 25% remaining) | Freeze non-critical changes; dedicate engineering to reliability work |
| **Exhausted** (0%) | Stop all feature work until budget recovers; post-incident analysis for each new incident |

### Toil

| Characteristic | Description |
|---------------|-------------|
| **Manual** | Requires human intervention, not automated |
| **Repetitive** | Happens over and over; not a one-time task |
| **Automatable** | Could be handled by software |
| **Reactive** | Triggered by alerts or requests, not proactive |
| **Without enduring value** | Does not improve the system permanently; must be done again |

**Target:** Keep toil below 50% of SRE team capacity; invest the remainder in automation and engineering.

---

## 2. Observability — the three pillars

### Logs

| Concern | Guidance |
|---------|----------|
| **Structured logging** | JSON or key-value format; include trace ID, span ID, request ID, user ID (anonymized) |
| **Log levels** | ERROR (action required), WARN (attention needed), INFO (operational events), DEBUG (development) |
| **Centralized aggregation** | Ship to centralized platform (ELK, Loki, CloudWatch Logs); searchable and retainable |
| **Retention policy** | Hot (7–30 days searchable), warm (30–90 days), cold (archive for compliance) |
| **Avoid** | Logging PII, secrets, or high-cardinality unbounded fields |

### Metrics

| Concern | Guidance |
|---------|----------|
| **RED method** (request-scoped) | **R**ate (requests/second), **E**rrors (error rate), **D**uration (latency distribution) |
| **USE method** (resource-scoped) | **U**tilization, **S**aturation, **E**rrors — for CPU, memory, disk, network |
| **Cardinality** | Control label cardinality; high-cardinality labels (user ID, request ID) belong in traces, not metrics |
| **Instrumentation** | Use client libraries (Prometheus, OpenTelemetry); instrument at service boundaries |
| **Dashboards** | SLO-based dashboards first; drill-down to RED/USE; avoid vanity dashboards |

### Traces

| Concern | Guidance |
|---------|----------|
| **Distributed tracing** | Propagate trace context (W3C Trace Context, B3) across all service boundaries |
| **Sampling** | Head-based (decide at entry) or tail-based (decide after completion based on attributes); 100% for errors |
| **Span attributes** | HTTP method, status, route, database operation, queue name, error details |
| **Trace-to-log correlation** | Include trace ID in all log entries; link from trace to relevant logs |
| **Tooling** | OpenTelemetry (vendor-neutral), Jaeger, Tempo, Honeycomb, Datadog |

### OpenTelemetry

| Component | Role |
|-----------|------|
| **SDK** | Instrument application code; auto-instrumentation for frameworks and libraries |
| **Collector** | Receive, process, and export telemetry (logs, metrics, traces) |
| **Exporters** | Send to backends — Prometheus, Jaeger, OTLP, vendor-specific |
| **Semantic conventions** | Standardized attribute names for consistent telemetry across services |

---

## 3. Alerting philosophy

### SLO-based alerting

Alert on **SLO burn rate** rather than individual metric thresholds:

| Alert type | Window | Use case |
|-----------|--------|----------|
| **Fast burn** | 5 min rate over 1 hr budget | Severe incident — rapid budget consumption; page on-call |
| **Slow burn** | 30 min rate over 6 hr budget | Gradual degradation — create a ticket; investigate during business hours |

### Alert design principles

| Principle | Description |
|-----------|-------------|
| **Actionable** | Every alert should have a clear response action; if no action, it should not page |
| **Relevant** | Alert the team that can fix it; avoid broadcasting to uninvolved teams |
| **Proportional** | Severity matches impact; critical = customer-facing SLO violation; warning = potential issue |
| **Deduplicated** | Group related alerts; avoid alert storms during cascading failures |
| **Documented** | Each alert links to a runbook with diagnosis steps and remediation |

---

## 4. Chaos engineering

### Process

| Step | Activity | Output |
|------|----------|--------|
| 1. **Hypothesis** | Define steady state and expected behavior under fault | Written hypothesis |
| 2. **Scope** | Choose blast radius — start small (single pod/instance) | Experiment scope document |
| 3. **Execute** | Inject fault (network delay, pod kill, disk fill, DNS failure) | Experiment execution |
| 4. **Observe** | Monitor SLOs, alerts, dashboards during experiment | Observation log |
| 5. **Learn** | Compare actual vs expected behavior; document surprises | Findings and action items |

### Common fault injections

| Fault | What it tests |
|-------|---------------|
| **Pod/process kill** | Auto-recovery, load balancing, health checks |
| **Network latency injection** | Timeout configuration, circuit breakers, retry behavior |
| **Network partition** | Split-brain handling, data consistency, failover |
| **Disk full** | Graceful degradation, log rotation, database behavior |
| **DNS failure** | Service discovery resilience, caching behavior |
| **Clock skew** | Certificate validation, token expiry, time-dependent logic |
| **Dependency failure** | Circuit breaker activation, fallback behavior, error messaging |

---

## 5. On-call practices

| Practice | Description |
|----------|-------------|
| **Rotation schedule** | Weekly rotation; minimum team size for sustainable coverage (5+ engineers) |
| **Escalation policy** | Primary → secondary → team lead → engineering manager; auto-escalate after timeout |
| **Runbooks** | Step-by-step diagnosis and remediation for each alert; maintain alongside alert definition |
| **Handoff** | End-of-rotation summary — open issues, recent changes, upcoming risks |
| **Compensation** | On-call compensation policy; acknowledge the burden; avoid burnout |
| **Shadowing** | New on-call engineers shadow experienced engineers before solo rotation |

### Incident severity levels

| Level | Impact | Response | Example |
|-------|--------|----------|---------|
| **P1 / Critical** | Service down or data loss for many users | Immediate page; war room; status page update | Complete outage, data breach |
| **P2 / High** | Major feature degraded for significant users | Page; begin investigation within 15 min | Payment processing slow, search broken |
| **P3 / Medium** | Minor feature degraded; workaround available | Business hours; investigate same day | Export feature timeout, non-critical API errors |
| **P4 / Low** | Cosmetic or minor issue; no user impact | Queue for next sprint | Dashboard rendering glitch, non-customer log error |

---

## 6. Post-incident learning

### Blameless postmortem structure

| Section | Content |
|---------|---------|
| **Summary** | What happened, impact, duration, severity |
| **Timeline** | Chronological events from detection to resolution (with timestamps) |
| **Root cause** | Contributing factors (not a single root cause — look for systemic issues) |
| **What went well** | Detection, response, communication that worked |
| **What could be improved** | Gaps in monitoring, response, communication, tooling |
| **Action items** | Specific, assigned, time-bound improvements (not "be more careful") |
| **Lessons learned** | Broader insights for the team and organization |

### Learning culture

| Practice | Description |
|----------|-------------|
| **Blameless** | Focus on systemic factors, not individual mistakes |
| **Share widely** | Publish postmortems to the organization; learning benefits everyone |
| **Track action items** | Follow through on postmortem action items; review completion rate |
| **Recurring themes** | Identify patterns across postmortems; address systemic issues |
| **Game days** | Periodic simulated incidents to practice response and validate runbooks |

---

## External references

| Topic | URL | Why it is linked |
|-------|-----|------------------|
| Google SRE Books | https://sre.google/books/ | Foundational SRE practices — free online |
| OpenTelemetry | https://opentelemetry.io/ | Vendor-neutral observability framework |
| SLO Alerting (Google) | https://sre.google/workbook/alerting-on-slos/ | Multi-window burn rate alerting |
| Principles of Chaos Engineering | https://principlesofchaos.org/ | Chaos engineering methodology |
| Chaos Monkey (Netflix) | https://netflix.github.io/chaosmonkey/ | Pioneering chaos engineering tool |
| Incident.io Handbook | https://incident.io/guide/ | Modern incident management practices |
| Honeycomb Observability Guide | https://www.honeycomb.io/observability/ | Observability culture and practices |
