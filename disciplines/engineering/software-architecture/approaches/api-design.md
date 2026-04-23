---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# API design and integration (blueprint)

API design is a cross-cutting architecture concern — every multi-component system communicates through APIs, and the quality of those APIs determines system evolvability, developer experience, and integration cost.

This guide covers **API-first design**, style selection, versioning, specification, contract testing, and event-driven integration patterns.

---

## 1. API-first design

Design the API contract **before** implementing the service. The contract is the spec; code is an implementation detail.

| Principle | Description |
|-----------|-------------|
| **Contract first** | Write the OpenAPI/AsyncAPI/protobuf definition before writing application code |
| **Consumer-driven** | Design from the consumer's perspective; validate with real callers |
| **Evolvable** | Plan for change — additive changes are safe; breaking changes require versioning |
| **Self-documenting** | The spec is the documentation; generated docs, SDKs, and mocks stay in sync |
| **Testable** | Contract tests validate conformance; mocks derived from spec for parallel development |

### Workflow

1. **Draft spec** — author OpenAPI/AsyncAPI/proto definition collaboratively (API designer + consumers).
2. **Review** — API design review (consistency, naming, error model, pagination, auth).
3. **Mock** — generate mock server from spec; consumers begin integration in parallel.
4. **Implement** — server team implements against the spec; contract tests enforce conformance.
5. **Validate** — integration tests with real consumers; load testing; security scan.
6. **Publish** — versioned spec in API catalog; generated SDK/client; developer portal documentation.

---

## 2. API styles

| Style | Transport | Format | Strengths | Trade-offs | Best fit |
|-------|-----------|--------|-----------|------------|----------|
| **REST** | HTTP | JSON (typically) | Universal, cacheable, tooling-rich, browser-friendly | Over/under-fetching, no built-in schema, chatty for complex reads | Public APIs, CRUD-heavy services, mobile/web BFFs |
| **GraphQL** | HTTP | JSON | Flexible queries, single endpoint, schema as type system, introspection | Complexity in caching, N+1 queries, authorization per field | Consumer-driven UIs with variable data needs, aggregation layer |
| **gRPC** | HTTP/2 | Protocol Buffers | High performance, streaming, strong typing, code generation | Browser support requires proxy, less tooling for debugging, binary format | Service-to-service, high-throughput internal APIs, polyglot microservices |
| **AsyncAPI / events** | Message broker | JSON/Avro/Protobuf | Temporal decoupling, scalability, event sourcing | Eventual consistency, debugging complexity, ordering guarantees | Event-driven architectures, CQRS, system integration |
| **WebSocket** | TCP (upgraded HTTP) | Custom/JSON | Full-duplex, low latency, real-time push | Stateful connections, load balancing complexity, no built-in request/response | Chat, real-time dashboards, collaborative editing, live data feeds |

### Choosing a style

| If you need… | Consider |
|-------------|----------|
| Public developer API with broad adoption | REST with OpenAPI |
| Flexible client queries with varied data needs | GraphQL |
| High-throughput internal communication | gRPC |
| Loosely coupled async integration | AsyncAPI + message broker |
| Real-time bidirectional communication | WebSocket (or SSE for server-push only) |

---

## 3. REST API design conventions

### Resource naming

| Convention | Example | Rationale |
|-----------|---------|-----------|
| Plural nouns for collections | `/users`, `/orders` | Consistent; collection vs item via URL path |
| Kebab-case for multi-word | `/order-items` | URL-safe; readable |
| Hierarchical nesting for ownership | `/users/{id}/orders` | Expresses containment; max 2 levels deep |
| Verb-free URLs | `/orders` not `/getOrders` | HTTP methods express the action |

### HTTP methods and status codes

| Method | Semantics | Idempotent | Success codes |
|--------|-----------|------------|---------------|
| **GET** | Read resource(s) | Yes | 200, 304 |
| **POST** | Create resource or trigger action | No | 201 (created), 202 (accepted), 204 (no content) |
| **PUT** | Replace resource entirely | Yes | 200, 204 |
| **PATCH** | Partial update | No (can be idempotent by design) | 200, 204 |
| **DELETE** | Remove resource | Yes | 204, 202 |

### Error model

Consistent error responses across all endpoints:

| Field | Purpose |
|-------|---------|
| `status` | HTTP status code (redundant but convenient for logging) |
| `code` | Machine-readable error code (e.g. `VALIDATION_FAILED`, `NOT_FOUND`) |
| `message` | Human-readable description |
| `details` | Array of field-level errors (for validation) |
| `traceId` | Correlation ID for debugging (links to distributed trace) |

### Pagination

| Strategy | Mechanism | Best fit |
|----------|-----------|----------|
| **Offset-based** | `?offset=20&limit=10` | Simple; allows jumping to any page; unstable under concurrent writes |
| **Cursor-based** | `?cursor=eyJ…&limit=10` | Stable pagination; no page jumps; efficient for large datasets |
| **Keyset** | `?after_id=123&limit=10` | Like cursor but using a natural key; requires indexed column |

---

## 4. API versioning

| Strategy | Mechanism | Trade-offs |
|----------|-----------|------------|
| **URL path** | `/v1/users`, `/v2/users` | Simple, explicit, cacheable; requires maintaining multiple paths |
| **Header** | `Accept: application/vnd.api+json;version=2` | Clean URLs; harder to test with curl/browser; proxy routing complexity |
| **Query param** | `/users?version=2` | Easy to test; less conventional; caching considerations |
| **No versioning (evolve)** | Additive changes only; deprecated fields removed after migration | Simplest when feasible; requires discipline; not suitable for all APIs |

### Breaking vs non-breaking changes

| Non-breaking (safe) | Breaking (requires version) |
|---------------------|----------------------------|
| Add optional field to response | Remove or rename field |
| Add optional query parameter | Change field type |
| Add new endpoint | Change URL structure |
| Add new enum value (if clients handle unknown) | Remove endpoint |
| Relax validation (accept more) | Tighten validation (reject previously valid input) |

---

## 5. API specification formats

| Format | Scope | Ecosystem |
|--------|-------|-----------|
| **OpenAPI 3.x** | REST APIs | Swagger UI, Redoc, code generators (openapi-generator), mock servers (Prism), linters (Spectral) |
| **AsyncAPI** | Event-driven / message APIs | Code generators, documentation, channel bindings for Kafka/AMQP/MQTT |
| **Protocol Buffers** (.proto) | gRPC services | grpc-gateway for REST transcoding, Buf for linting/breaking-change detection |
| **GraphQL SDL** | GraphQL APIs | Apollo, Relay, introspection, schema registry, federation |

---

## 6. Contract testing

Contract tests verify that API consumers and providers agree on the interface — catching integration issues before deployment.

| Approach | How it works | Tools |
|----------|-------------|-------|
| **Consumer-driven contracts** | Consumers define expectations; provider verifies against them | Pact, Spring Cloud Contract |
| **Provider-driven (spec)** | Provider publishes OpenAPI spec; consumers validate against it | Spectral, Dredd, Schemathesis |
| **Schema registry** | Centralized schema store with compatibility checks (backward, forward, full) | Confluent Schema Registry, Buf Schema Registry |
| **Bi-directional** | Both sides generate specs; a broker checks compatibility | Pactflow bidirectional |

### Integration into CI/CD

| Pipeline stage | Contract activity |
|----------------|-------------------|
| **PR / build** | Lint spec (Spectral), check for breaking changes (oasdiff, Buf) |
| **Integration test** | Run contract tests against mock or staging |
| **Pre-release** | Verify all consumer contracts pass against provider |
| **Post-deploy** | Smoke tests against production with contract expectations |

---

## 7. Event-driven integration patterns

| Pattern | Description | Use case |
|---------|-------------|----------|
| **Event notification** | Publish thin events (type + entity ID); consumers fetch details | Loose coupling; consumers may need different data |
| **Event-carried state transfer** | Publish full entity state in event; consumers build local read models | Reduce synchronous calls; accept eventual consistency |
| **Event sourcing** | Persist all state changes as immutable events; reconstruct state by replaying | Audit trail, temporal queries, complex domain events |
| **CQRS** | Separate write model (commands) from read model (queries) | Different read/write scaling; optimized read views |
| **Saga / choreography** | Distributed transaction via event chain; each service reacts and emits next event | Cross-service workflows without distributed locks |
| **Saga / orchestration** | Central coordinator drives workflow steps via commands | Complex workflows requiring centralized visibility and error handling |
| **Outbox pattern** | Write events to database outbox table; separate process publishes to broker | At-least-once delivery without dual-write problem |

---

## 8. API security

| Concern | Guidance |
|---------|----------|
| **Authentication** | OAuth 2.0 / OIDC for user context; API keys or mTLS for service-to-service |
| **Authorization** | Enforce at API gateway and service level; scopes for coarse-grained, ABAC/ReBAC for fine-grained |
| **Rate limiting** | Protect against abuse and DoS; communicate limits via headers (`X-RateLimit-*`, `Retry-After`) |
| **Input validation** | Validate all input against schema; reject unexpected fields; sanitize before processing |
| **CORS** | Restrict origins in production; allow credentials only where needed |
| **Transport security** | TLS 1.2+ mandatory; HSTS for web APIs; certificate pinning for mobile |

---

## External references

| Topic | URL | Why it is linked |
|-------|-----|------------------|
| OpenAPI Specification | https://spec.openapis.org/oas/latest.html | REST API description standard |
| AsyncAPI | https://www.asyncapi.com/ | Event-driven API specification |
| gRPC | https://grpc.io/ | High-performance RPC framework |
| GraphQL | https://graphql.org/ | Query language for APIs |
| Pact | https://pact.io/ | Consumer-driven contract testing |
| Spectral | https://stoplight.io/open-source/spectral | OpenAPI linting |
| API Design Patterns (JJ Geewax) | https://www.manning.com/books/api-design-patterns | API design patterns book |
| REST API Design Rulebook (Massé) | https://www.oreilly.com/library/view/rest-api-design/9781449317904/ | REST conventions reference |
