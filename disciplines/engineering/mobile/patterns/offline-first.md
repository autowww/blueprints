---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Offline-first mobile patterns (blueprint)

**Purpose:** Design mobile experiences when **connectivity is unreliable** — local truth, sync, conflicts, queues, caching, and UX. Treat offline capability as a product requirement, not an afterthought.

**Audience:** Teams adopting [`blueprints/disciplines/engineering/mobile/`](../README.md). See also [`MOBILE.md`](../MOBILE.md) § offline-first and [`mobile-architecture.md`](mobile-architecture.md).

---

## Overview

Offline-first means the app **reads and writes against local storage first**, then reconciles with the server when possible. Users expect drafts to persist, actions to queue, and clear feedback when sync fails or conflicts arise. This guide maps **states**, **storage**, **sync models**, **conflict handling**, and **testing** without binding you to a single backend protocol.

---

## Offline-first architecture

```blueprint-diagram
key: linear
alt: Diagram
```

The **sync engine** owns scheduling, retries, deduplication, and conflict detection; the **UI** observes local state.

---

## Connectivity states

| State | Detection hints | UX implications |
|-------|-----------------|-----------------|
| **Online** | Successful reachability + low latency | Full features; refresh from network |
| **Offline** | No interface / captive portal / explicit disconnect | Queue writes; show cached data; disable network-only actions |
| **Slow / intermittent** | Timeouts, high RTT, packet loss | Timeouts with retry UI; avoid blocking spinners |
| **Lie-fi** | Connected interface but no real path (DNS fail, captive) | Treat like offline after failed probe; offer retry |

Use **combined signals**: OS reachability plus **active probes** (lightweight HEAD/health check) where product-critical.

---

## Local storage comparison

| Store | Capacity | Query / index | Encryption | Platforms |
|-------|----------|---------------|------------|-----------|
| **SQLite** (Room / Core Data) | Large | SQL, relations | SQLCipher / file protection / EncryptedFile | iOS, Android, KMP |
| **Key-value** (DataStore, MMKV, UserDefaults) | Small–medium | Key lookup | Platform APIs / encrypted prefs | iOS, Android |
| **File system** | Large | App-managed | Encrypted containers | All native |
| **IndexedDB** (web / PWA) | Quota-bound | Indexes, cursors | HTTPS + optional wrapping | Web |

---

## Sync strategies

| Strategy | Behavior | Best when |
|----------|----------|-----------|
| **Optimistic** | Apply locally immediately; sync in background | High trust in merge; good UX latency |
| **Pessimistic** | Block until server ack | Financial or safety-critical commits |
| **Eventual consistency** | All replicas converge without global lock | Collaborative content with merge rules |
| **Last-write-wins (LWW)** | Timestamp or version picks winner | Simple fields; low conflict rate |
| **CRDTs** | Mathematically mergeable structures | Real-time collaboration, high conflict |

---

## Conflict resolution sequence

```blueprint-diagram
key: sequence
alt: Diagram
```

---

## Conflict resolution patterns

| Pattern | When to use |
|---------|-------------|
| **LWW** | Scalar fields; server clock trusted; rare edits |
| **Merge** | Independent fields; three-way merge possible |
| **Manual** | Legal / financial text; user must choose |
| **Operational transform** | Simultaneous editing (classic docs) |
| **CRDTs** | Concurrent edits without central serialization |

---

## Queue management

| Practice | Detail |
|----------|--------|
| **Operation queue** | Durable outbox: type, payload, idempotency key, ordering key |
| **Retry** | Exponential backoff + jitter; cap max delay |
| **Deduplication** | Idempotency keys; stable client-generated IDs |
| **Ordering** | Per-entity serialization where order matters; parallel where safe |

---

## Caching strategies

| Strategy | Read path | Write path | Risk |
|----------|-----------|------------|------|
| **Cache-first** | Local then refresh | Local + queue | Stale UI if refresh fails silently |
| **Network-first** | Network then fallback | Remote then local | Poor offline read UX |
| **Stale-while-revalidate** | Show stale, fetch in background | As above | Need timestamps / ETag |
| **Cache-only** | Never hit network (debug / airplane) | N/A | Testing only |

**Decision matrix (simplified):**

| Need | Prefer |
|------|--------|
| Best offline reads | Cache-first or SWR |
| Strong server truth | Network-first with cache fallback |
| Low server load | SWR with long TTL |

---

## Background sync

| Platform | Mechanism | Limits |
|----------|-----------|--------|
| **Android** | WorkManager (constraints, expedited where allowed) | Doze, App Standby, OEM kills |
| **iOS** | `BGAppRefreshTask`, `BGProcessingTask` | System-scheduled; not guaranteed |
| **Both** | Push-triggered sync | Payload size; user disabled background |

Respect **battery optimizations**; batch and coalesce network work.

---

## Data migration and schema evolution

Version local schemas explicitly (Room migrations, Core Data mapping models). Prefer **additive** changes, **default values**, and **lazy backfill**. Test migrations on large synthetic datasets. For sync, include **schema version** in payloads so servers can branch behavior.

---

## UX for offline

| Concern | Pattern |
|---------|---------|
| **Optimistic UI** | Show pending state; rollback on definitive failure |
| **Sync indicators** | Subtle “saved locally” / “synced” / “sync failed” |
| **Conflict UI** | Side-by-side or field-level resolution; audit trail |
| **Degradation** | Disable or explain unavailable features clearly |

---

## Testing offline scenarios

| Technique | Goal |
|-----------|------|
| **Network simulation** | Link conditioner, proxy blackholes, airplane mode in CI farms |
| **Edge cases** | Mid-sync kill, clock skew, duplicate delivery |
| **Integrity** | Checksums, round-trip tests, property-based merge tests |

---

## Anti-patterns

| Anti-pattern | Effect |
|--------------|--------|
| **Network-first mindset** | Broken UX offline; hidden failures |
| **Unbounded local storage** | OOM, slow queries, uninstall |
| **Silent data loss** | User trust destroyed |
| **Sync storms** | Battery drain; server overload after reconnect |

---

## External references

| Resource | URL |
|----------|-----|
| Offline First | https://offlinefirst.org/ |
| Local-first software (Ink & Switch) | https://www.inkandswitch.com/local-first/ |
| CRDTs (Shapiro et al.) | https://arxiv.org/abs/1410.2803 — comprehensive CRDT overview |

---

*Keep project-specific mobile architecture decisions in docs/adr/ and platform documentation in docs/development/, not in this file.*
