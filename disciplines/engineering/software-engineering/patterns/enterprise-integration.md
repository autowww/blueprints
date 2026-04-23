---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Enterprise Integration Patterns (EIP)

*Enterprise Integration Patterns* (Hohpe & Woolf) names **recurring solutions for messaging-based integration**: how producers and consumers communicate through **channels**, how messages are **routed** and **transformed**, and how endpoints **adapt** protocols and reliability models. The ideas apply to queues, brokers, and log-based streaming alike.

**Parent context:** A short representative list appears in [`../SOFTWARE-ENGINEERING.md`](../SOFTWARE-ENGINEERING.md) § **3. Design patterns — Enterprise integration (representative)**.

---

## Overview

Distributed systems integrate when **autonomy**, **latency tolerance**, and **failure isolation** matter more than a single in-process call graph. Messaging trades **immediate consistency** for **decoupling**, **buffering**, and **horizontal scale** — at the cost of operational complexity and eventual consistency discipline.

---

## Core concepts

| Concept | Definition | Typical responsibility |
|---------|------------|------------------------|
| **Message** | Self-contained unit of data + metadata (headers, correlation IDs) | Business event, command, or document snapshot |
| **Channel** | Logical path between sender and receiver | Queue, topic, partition, subscription |
| **Router** | Decides next hop(s) from message content or context | Content-based routing, splitting, aggregating |
| **Translator** | Maps one message shape or protocol to another | Anti-corruption layer at boundaries |
| **Endpoint** | Code that connects an application to messaging | Polling consumer, event-driven listener, gateway |

---

## Producer → channel → router → transformer → consumer

```blueprint-diagram
key: linear
alt: Diagram
```

In practice, **router** and **translator** may live in the same service (integration tier) or be split across **middleware** and **domain** layers.

---

## Pattern categories (selected)

### Messaging channels

| Pattern / style | Role | Watch-out |
|-----------------|------|-----------|
| **Point-to-point** | Exactly one consumer gets the work | Poison messages need DLQ strategy |
| **Publish-subscribe** | Many subscribers receive copies | Fan-out volume; subscription management |
| **Dead-letter channel** | Isolate messages that cannot be processed | Must alert, replay, or discard with audit |

### Message routing

| Pattern | Role | Example force |
|---------|------|---------------|
| **Content-based router** | Route by payload or headers | Multi-tenant pipelines |
| **Splitter** | One message → many messages | Order lines → line handlers |
| **Aggregator** | Many messages → one correlated message | Scatter/gather workflows |
| **Resequencer** | Restore order after parallel processing | Out-of-order shards |

### Message transformation

| Pattern | Role |
|---------|------|
| **Envelope wrapper** | Standard outer shell for heterogeneous payloads |
| **Content enricher** | Add missing data from external lookup |
| **Normalizer** | Canonicalize many formats to one internal model |

### Messaging endpoints

| Pattern | Role |
|---------|------|
| **Polling consumer** | Pull from channel on a loop / schedule |
| **Event-driven consumer** | Push / callback when message arrives |
| **Competing consumers** | N workers share a queue for scale-out |

### Guaranteed delivery and retry semantics (conceptual)

| Semantic | Meaning | Typical building blocks |
|----------|---------|-------------------------|
| **At-most-once** | May lose under crash | Fire-and-forget; metrics-only paths |
| **At-least-once** | Duplicates possible; consumer must be idempotent | ACK after processing + retries |
| **Exactly-once** | End-to-end illusion; expensive | Transactional outbox + idempotent sink + careful fencing |

Most practical stacks implement **at-least-once** messaging plus **idempotent handlers** — treat “exactly-once” claims as **scoped** to a subsystem, not physics.

---

## Message channel shapes (EIP vocabulary)

| Channel style | Intent | Example |
|---------------|--------|---------|
| **Point-to-point** | One consumer processes each message | Work queue, task backlog |
| **Publish-subscribe** | Broadcast to interested parties | Domain events, fan-out notifications |
| **Datatype channel** | Typed stream so payloads stay homogeneous | `OrderCreated` vs `PaymentCaptured` topics |
| **Invalid message channel** | Side channel for bad payloads | Schema validation failures |
| **Dead-letter channel** | Quarantine after max retries | Ops dashboards, manual replay |

Naming channels after **business capabilities** ages better than naming them after deploying teams.

---

## Additional routing & management patterns

| Pattern | Role |
|---------|------|
| **Message filter** | Drop messages that fail predicate early |
| **Dynamic router** | Rules/config choose destination without redeploy |
| **Process manager** | Track multi-step correlation (saga-style state machine in middleware) |
| **Wire tap** | Non-invasive copy to observability pipeline |
| **Message store** | Audit log of messages in flight (debugging, compliance) |

---

## Outbox and inbox (reliability companions)

| Pattern | Problem solved |
|---------|----------------|
| **Transactional outbox** | Atomically commit domain state + “message to send”; separate relay publishes — avoids dual-write races |
| **Inbox / dedup** | Process at-least-once deliveries exactly once in application terms |

These are not excuses to skip **idempotency** — they align **database commits** with **broker publishes**.

---

## Decision matrix: synchronous API vs async messaging vs event streaming

| Force | Favor synchronous API | Favor async messaging (queue) | Favor event streaming (log) |
|-------|----------------------|------------------------------|----------------------------|
| **Caller needs immediate answer** | Strong | Weak | Weak |
| **Burst tolerance / smoothing** | Weak | Strong | Strong |
| **Many interested subscribers** | Weak (N calls) | Medium (topics) | Strong (replay, fan-out) |
| **Ordering / replay semantics** | N/A | Per-queue contracts | Strong (offset, retention) |
| **Operational simplicity** | Often simplest | Medium | Higher (ops, schema evolution) |

---

## Technology mapping (pattern support — high level)

| Platform | Point-to-point / work queues | Pub/sub | Delay / scheduling | Dead-letter | Ordering guarantees |
|----------|------------------------------|---------|-------------------|-------------|---------------------|
| **RabbitMQ** | Queues, routing keys | Exchanges, bindings | Plugins / TTL patterns | DLX | Per-queue; complex topologies |
| **Apache Kafka** | Consumer groups as competing consumers | Topics, partitions | Not core (patterns exist) | Quarantine topics / apps | Per-partition order |
| **AWS SQS / SNS** | SQS standard/FIFO | SNS fan-out | Delay queues (SQS) | DLQ (SQS) | FIFO option |
| **Azure Service Bus** | Queues | Topics/subscriptions | Scheduled messages | Dead-letter subpath | Sessions for ordered groups |
| **Google Pub/Sub** | Subscriptions (push/pull) | Topics | Ordering keys (limited) | Dead-letter topics | Ordering keys |

Exact features change with cloud revisions — treat this table as a **conversation starter with your platform docs**, not a SLA.

---

## Saga: choreography vs orchestration

| Style | Idea | Pros | Cons |
|-------|------|------|------|
| **Choreography** | Each service reacts to events; no central brain | Loose coupling; no single orchestrator SPOF | Harder global visibility; discovery of flows |
| **Orchestration** | Coordinator sends commands / tracks state | Clear story of progress; easier compensations | Orchestrator complexity; can become a god service |

### Orchestrated saga (simplified sequence)

```blueprint-diagram
key: sequence
alt: Diagram
```

Choreographed sagas replace the `O` messages with **domain events** each service subscribes to; compensations are still **explicitly designed**, not magical.

### Choreographed saga (simplified sequence)

```blueprint-diagram
key: sequence
alt: Diagram
```

Observability becomes critical: you need **correlation IDs** and **process views** because there is no single orchestrator object to inspect.

---

## Schema evolution and contracts

| Practice | Why |
|----------|-----|
| **Versioned events** | Consumers deploy at different cadences |
| **Backward-compatible readers** | Unknown fields ignored; required fields minimized |
| **Schema registry** | Kafka/Avro/Protobuf governance |
| **Consumer-driven contracts** | Prevent breaking fan-out silently |

Integration failures often arrive as **schema skew**, not broker outages.

---

## Anti-patterns

| Anti-pattern | Symptom | Fix direction |
|--------------|---------|---------------|
| **Distributed monolith** | “Microservices” that must deploy together | Align boundaries with ownership and data |
| **Chatty integration** | Many tiny synchronous hops across the network | Batch, cache, or move work behind a queue |
| **Missing idempotency** | Retries duplicate side effects | Idempotent keys, dedup stores, outbox pattern |

---

## External references

| Resource | Link / note |
|----------|-------------|
| Hohpe & Woolf — *Enterprise Integration Patterns* | Canonical pattern language |
| EnterpriseIntegrationPatterns.com | [https://www.enterpriseintegrationpatterns.com/](https://www.enterpriseintegrationpatterns.com/) — online catalog |
| Confluent documentation | [https://docs.confluent.io/](https://docs.confluent.io/) — Kafka-centric streaming and patterns |

---

*Keep project-specific engineering standards in `docs/development/` and architecture decisions in `docs/adr/`, not in this file.*
