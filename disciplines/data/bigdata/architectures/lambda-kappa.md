---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Lambda, Kappa & unified data architectures

**Purpose:** Project-agnostic guide to **batch–stream hybrid** and **unified streaming** architectures: how they evolved, how they differ, and how to choose among them — including **lakehouse** as a common unified-storage pattern.

**Audience:** Teams using [`blueprints/disciplines/data/bigdata/`](../README.md). Pair with [`BIGDATA.md`](../BIGDATA.md) §1 (principles) for the broader decision framework.

---

## 1. Overview: from batch-only to unified streaming

Early big-data systems were **batch-only**: periodic jobs recomputed views from full or incremental dumps. That model is simple and can be very accurate for historical analytics, but **latency** is bounded by the batch interval.

**Lambda architecture** added a **speed layer** so low-latency views could coexist with a **batch layer** that recomputes authoritative state. **Kappa architecture** questioned whether two paths were necessary: if the **immutable event log** is the system of record, a **single stream-processing** stack can often replace batch by **replaying** the log.

**Unified** approaches (modern stream processors with batch APIs, or **lakehouse** table formats with ACID + time travel) aim to **one engine** and **one storage abstraction** for both reprocessing and serving, reducing operational duplication while preserving flexibility.

---

## 2. Lambda architecture (deep dive)

Lambda splits work across three conceptual layers:

| Layer | Role | Typical traits |
|-------|------|----------------|
| **Batch layer** | Precompute **complete**, **accurate** views from raw/master data | High latency (hours–days acceptable); full recomputation or large incremental windows |
| **Speed layer** | Compensate for batch lag with **incremental** or **approximate** updates | Low latency (seconds–minutes); may diverge until batch catches up |
| **Serving layer** | **Merge** batch and real-time outputs for queries | Key-value or low-latency serving; clients see a unified read API |

```blueprint-diagram
key: swimlane
alt: Diagram
```

**When it shines:** You need **provably correct historical recomputation** (e.g., late-arriving facts, complex corrections) **and** **sub-batch latency** for some use cases.

---

## 3. Kappa architecture (deep dive)

Kappa **removes the separate batch path**: stream processing consumes an **append-only log**; **reprocessing** means **resetting offsets** or **replaying** topics through the same topology (often with upgraded code).

```blueprint-diagram
key: swimlane
alt: Diagram
```

**When it shines:** The domain can be modeled as **events**, **idempotent sinks** exist, and **replay** is an acceptable substitute for heavyweight batch recompute.

---

## 4. Comparison matrix: Lambda vs Kappa vs unified

| Dimension | Lambda | Kappa | Unified (e.g., Flink batch+stream, Databricks/lakehouse) |
|-----------|--------|-------|-----------------------------------------------------------|
| **Complexity** | High (two code paths + merge) | Medium (one path; replay discipline) | Medium–high (one platform; still many knobs) |
| **Latency** | Speed layer can be very low | Low if engine supports it | Low to moderate depending on product |
| **Reprocessing** | Batch layer is natural | Replay / reset offsets | Replay, time travel, or batch modes on same stack |
| **Consistency** | Batch “wins” after merge | Depends on sink semantics + exactly-once | Table formats + transactions improve cross-batch consistency |
| **Operational overhead** | Operate batch + stream + serving merge | Operate log + stream + state | Fewer moving parts than classic Lambda; vendor/managed variance |
| **Cost** | Often higher (duplicate compute/storage patterns) | Log retention + state store costs | Consolidation can reduce waste; premium managed tiers vary |
| **Team skills** | Batch + streaming + serving | Streaming-first + operational log hygiene | Platform-specific expertise (Spark/Flink/Delta, etc.) |

---

## 5. Decision flowchart (architecture choice)

```blueprint-diagram
key: decision
alt: Diagram
```

---

## 6. Technology mapping (illustrative)

| Pattern | Example stacks (not exhaustive) |
|---------|-----------------------------------|
| **Lambda** | Hadoop batch (MapReduce / Spark) + Apache Storm (historical) + serving DB; Spark batch + Flink/Kafka Streams speed layer |
| **Kappa** | Apache Kafka + Apache Flink (or Kafka Streams) + compacted topics / materialized views |
| **Unified / lakehouse** | Databricks (Delta Lake), Apache Iceberg or Hudi on object storage + Spark/Flink/Trino; managed lakehouse offerings |

Tools evolve: treat this table as **family resemblance**, not a rigid taxonomy.

---

## 7. Lakehouse: lake + warehouse concerns

A **lakehouse** keeps **cheap object storage** as the main store while adding **warehouse-like** features: **transactions**, **schema enforcement**, **time travel**, and **incremental processing** against open table formats.

| Format | Notable strengths | Typical integration notes |
|--------|-------------------|---------------------------|
| **Delta Lake** | ACID, time travel, wide Spark/Databricks ecosystem | Strong in Spark-first shops; UniForm / multi-format bridges vary by vendor |
| **Apache Iceberg** | Partition evolution, hidden partitioning, strong catalog story | Popular for open, multi-engine (Spark, Flink, Trino) neutrality |
| **Apache Hudi** | Incremental processing, record-level upserts | Common for CDC-heavy, near-real-time lake patterns |

Lakehouse does not by itself replace **organizational** patterns (e.g., **data mesh**); it is primarily a **storage and execution** unification play.

---

## 8. Data quality by architecture

| Concern | Lambda | Kappa | Unified / lakehouse |
|---------|--------|-------|---------------------|
| **Where validation runs** | Batch jobs (authoritative); speed layer (subset / heuristic) | Stream validators; replay jobs for regression | Bronze/silver/gold or equivalent zones; stream + batch on same tables |
| **Schema enforcement** | Strong in batch; speed layer may use looser contracts | Registry + compatibility; stream–table contracts | Table constraints, constraints in engines, catalog policies |
| **Dead letter queues** | Less central; batch quarantine tables | **Critical** — poison messages and bad keys | Same as stream + batch: DLQ topics and rejected row tables |

---

## 9. Migration patterns

| From | Toward | Practical pattern |
|------|--------|-------------------|
| **Batch-only** | + streaming | Add a log at source; implement speed views; keep batch as source of truth until merge semantics are trusted |
| **Lambda** | Unified / Kappa | Strangler: move merge logic toward single store; shorten batch cycle; prove replay replaces batch for subsets |
| **Legacy DW** | Lakehouse | Land raw in object storage; incremental ELT; virtualize or migrate marts; retire duplicate copies deliberately |

---

## 10. Anti-patterns

| Anti-pattern | Why it hurts |
|--------------|--------------|
| **Lambda without a clear merge story** | Inconsistent reads; “which number is true?” becomes permanent |
| **Kappa ignoring late data** | Silent drift; dashboards disagree with finance after corrections |
| **Schema-on-read chaos in the lake** | Unbounded consumer breakage; untestable pipelines |
| **Unified platform, dual reality** | One vendor stack but teams still run shadow batch in spreadsheets |

---

## 11. External references

| Reference | Why read it |
|-----------|-------------|
| Nathan Marz, *Big Data: Principles and best practices of scalable realtime data systems* (Manning) | Original Lambda framing and motivation |
| Jay Kreps, [“Questioning the Lambda Architecture”](https://www.oreilly.com/radar/questioning-the-lambda-architecture/) (O’Reilly Radar, 2014) | Kappa-style critique and stream-log centrality |
| Databricks lakehouse papers and product docs | Unified storage + engine positioning (evaluate vendor claims against your workloads) |

---

*Keep project-specific data architecture decisions in docs/adr/ and pipeline documentation in docs/development/, not in this file.*
