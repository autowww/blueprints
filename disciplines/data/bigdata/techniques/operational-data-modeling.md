---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Operational data modeling (blueprint)

Operational data modeling covers the design of data structures for **transactional, application-serving databases** — the storage that powers day-to-day product features. This complements the analytical/scale focus of the broader [Big Data discipline](../BIGDATA.md) with practical guidance for relational and NoSQL databases used in operational systems.

---

## 1. Relational modeling

### Normalization

| Normal form | Rule | Why it matters |
|-------------|------|---------------|
| **1NF** | Atomic values; no repeating groups | Eliminates multi-valued columns; enables indexing |
| **2NF** | 1NF + no partial dependencies on composite keys | Reduces data duplication in tables with composite PKs |
| **3NF** | 2NF + no transitive dependencies | Each non-key column depends only on the primary key; reduces update anomalies |
| **BCNF** | Every determinant is a candidate key | Stronger form of 3NF; handles edge cases in key dependencies |

**Practical guidance:** Most operational schemas should be in 3NF. Denormalize deliberately for read performance (and document the reason in an ADR).

### Entity-Relationship modeling

| Concept | Description |
|---------|-------------|
| **Entity** | A distinct thing tracked by the system (User, Order, Product) |
| **Attribute** | A property of an entity (name, created_at, price) |
| **Relationship** | An association between entities (User *places* Order) |
| **Cardinality** | 1:1, 1:N, M:N — determines foreign key placement and junction tables |
| **Participation** | Total (every entity must participate) vs partial (optional) |

### Naming conventions

| Convention | Example | Rationale |
|-----------|---------|-----------|
| **snake_case for tables and columns** | `order_items`, `created_at` | Wide RDBMS convention; case-insensitive across databases |
| **Singular table names** | `user`, `order` | Entity represents one thing; collection is implied |
| **Explicit join table names** | `user_role` | Alphabetical order of participating entities |
| **`_id` suffix for foreign keys** | `user_id`, `order_id` | Clear FK identification |
| **Avoid reserved words** | `user_account` not `user` | Prevents quoting issues across databases |

---

## 2. Indexing strategies

| Index type | Use case | Trade-off |
|-----------|----------|-----------|
| **B-tree** (default) | Equality and range queries, ORDER BY, unique constraints | General-purpose; write overhead per index |
| **Hash** | Exact equality lookups only | Faster equality; no range support; not all RDBMS support |
| **GIN** (Generalized Inverted) | Full-text search, JSONB containment, array overlap | Fast reads on complex types; larger index, slower writes |
| **GiST** (Generalized Search Tree) | Geometric, range, and proximity queries | Spatial and range data; less efficient for simple equality |
| **Partial / filtered** | Index subset of rows matching a condition | Smaller index; faster for filtered queries; requires predicate match |
| **Covering / include** | Store extra columns in index to avoid table lookup | Faster reads; larger index; write overhead |
| **Composite** | Multi-column index for combined predicates | Column order matters — leftmost prefix rule applies |

### Query plan analysis

| Step | Activity |
|------|----------|
| 1. **EXPLAIN ANALYZE** | Run the query with execution plan and actual timings |
| 2. **Identify bottlenecks** | Look for sequential scans on large tables, nested loops on unindexed joins, sort operations |
| 3. **Check index usage** | Verify expected indexes are used; check for index-only scans vs table lookups |
| 4. **Statistics freshness** | Ensure table statistics are current (`ANALYZE` / `UPDATE STATISTICS`) |
| 5. **Iterate** | Add/modify indexes, rewrite query, or restructure schema; re-measure |

---

## 3. Transaction isolation and concurrency

| Isolation level | Dirty reads | Non-repeatable reads | Phantom reads | Performance |
|----------------|-------------|---------------------|---------------|-------------|
| **Read Uncommitted** | Possible | Possible | Possible | Highest |
| **Read Committed** | Prevented | Possible | Possible | Good (PostgreSQL default) |
| **Repeatable Read** | Prevented | Prevented | Possible (prevented in PostgreSQL) | Moderate |
| **Serializable** | Prevented | Prevented | Prevented | Lowest (potential serialization failures) |

### Concurrency patterns

| Pattern | Description | When to use |
|---------|-------------|-------------|
| **Optimistic locking** | Check version/timestamp at write time; retry on conflict | Low contention; read-heavy workloads |
| **Pessimistic locking** | Lock row(s) with `SELECT FOR UPDATE` before modification | High contention; critical sections |
| **Advisory locks** | Application-level locks using database primitives | Coordinating distributed processes; preventing duplicate work |
| **SKIP LOCKED** | Skip rows locked by other transactions | Job queues; work distribution without contention |

---

## 4. Schema migration

### Principles

| Principle | Description |
|-----------|-------------|
| **Version controlled** | Every schema change is a numbered migration in source control |
| **Forward-only** | Avoid rollback migrations in production; use forward-fixing migrations |
| **Backward compatible** | New schema must work with both old and new application code during deployment |
| **Tested** | Migrations run in CI against a test database; verify data integrity |
| **Small and incremental** | One concern per migration; avoid combining schema and data changes |

### Expand-contract pattern

Safe schema changes for zero-downtime deployments:

| Phase | Activity | Code state |
|-------|----------|------------|
| **Expand** | Add new column/table alongside existing | Code writes to both old and new; reads from old |
| **Migrate** | Backfill data from old to new column/table | Code writes to both; reads from new |
| **Contract** | Drop old column/table; remove dual-write code | Code uses only new schema |

### Migration tooling

| Tool | Language/framework | Approach |
|------|-------------------|----------|
| **Flyway** | JVM, SQL | SQL-based migrations, version tracking |
| **Liquibase** | JVM | XML/YAML/SQL changesets, rollback support |
| **Alembic** | Python (SQLAlchemy) | Code-generated migrations, branch management |
| **Prisma Migrate** | TypeScript/JavaScript | Schema-first, declarative migrations |
| **golang-migrate** | Go | SQL file migrations, database-agnostic |
| **dbmate** | Any | Plain SQL migrations, lightweight, database-agnostic |

---

## 5. NoSQL data modeling

### Document databases (MongoDB, DynamoDB, Firestore)

| Pattern | Description | When to use |
|---------|-------------|-------------|
| **Embedding** | Nest related data within a single document | 1:1 or 1:few relationships; data accessed together; bounded growth |
| **Referencing** | Store IDs and fetch separately | M:N relationships; unbounded growth; data updated independently |
| **Bucket pattern** | Group time-series data into fixed-size buckets | IoT telemetry, logs, time-based queries |
| **Polymorphic pattern** | Different document shapes in same collection with a type discriminator | Flexible schemas; product catalogs; event stores |

### Key-value stores (Redis, DynamoDB)

| Pattern | Description | Use case |
|---------|-------------|----------|
| **Cache-aside** | Application reads cache first; on miss, reads database and populates cache | Read-heavy, latency-sensitive |
| **Write-through** | Writes go to cache and database simultaneously | Strong consistency between cache and database |
| **TTL-based expiration** | Keys expire after configurable time | Session storage, rate limiting, temporary data |
| **Sorted sets** | Ordered collections with score-based ranking | Leaderboards, priority queues, time-based feeds |

### Graph databases (Neo4j, Amazon Neptune)

| When to choose graph | When to avoid graph |
|---------------------|---------------------|
| Relationships are the primary query target | Simple key-value or document lookups |
| Traversal depth is variable (friends-of-friends, shortest path) | Fixed-depth joins (standard SQL) |
| Schema evolves frequently | Write-heavy, high-throughput transactional workloads |
| Social networks, recommendation, fraud detection, knowledge graphs | OLAP/analytical workloads (better in columnar stores) |

### Time-series databases (TimescaleDB, InfluxDB, QuestDB)

| Concern | Guidance |
|---------|----------|
| **Schema design** | Wide vs narrow table; tags vs fields; time partitioning |
| **Retention policies** | Automatic downsampling (raw → hourly → daily); tiered storage |
| **Query patterns** | Aggregation over time windows; last-known-value; gap filling |
| **Ingestion** | Batch vs streaming; out-of-order handling; write amplification |

---

## 6. Polyglot persistence

Using multiple database types, each optimized for its access pattern:

| Access pattern | Database type | Example |
|---------------|---------------|---------|
| **Transactional CRUD** | Relational (PostgreSQL, MySQL) | User accounts, orders, inventory |
| **Full-text search** | Search engine (Elasticsearch, Meilisearch) | Product search, log search |
| **Caching** | Key-value (Redis, Memcached) | Session store, API response cache |
| **Graph traversal** | Graph (Neo4j, Neptune) | Recommendations, social graph |
| **Time-series** | Time-series (TimescaleDB, InfluxDB) | Metrics, IoT telemetry, financial ticks |
| **Document / flexible schema** | Document (MongoDB, DynamoDB) | Content management, product catalogs |
| **Analytical** | Columnar (ClickHouse, BigQuery) | Business intelligence, event analytics |

### Synchronization strategies

| Strategy | Description | Consistency |
|----------|-------------|-------------|
| **Dual write** | Application writes to both stores | Inconsistent on failure (avoid without outbox) |
| **Change data capture (CDC)** | Capture database changes and propagate to secondary stores | Eventually consistent; reliable |
| **Event sourcing** | Events are the source of truth; projections build views in each store | Eventually consistent; auditable |
| **ETL / scheduled sync** | Periodic batch transfer from primary to secondary | Latency = batch interval; simple |

---

## External references

| Topic | URL | Why it is linked |
|-------|-----|------------------|
| Use The Index, Luke | https://use-the-index-luke.com/ | SQL indexing and performance — practical and thorough |
| PostgreSQL Documentation | https://www.postgresql.org/docs/ | Authoritative reference for advanced SQL features |
| Designing Data-Intensive Applications | https://dataintensive.net/ | Distributed data systems — the essential reference |
| Database Internals (Petrov) | https://www.databass.dev/ | How databases work under the hood |
| MongoDB Data Modeling | https://www.mongodb.com/docs/manual/data-modeling/ | Document database modeling patterns |
| DynamoDB Book (Alex DeBrie) | https://www.dynamodbbook.com/ | DynamoDB single-table design patterns |
