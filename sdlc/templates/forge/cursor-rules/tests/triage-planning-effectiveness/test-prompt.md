# Test prompt (fixed input)

Feed these two scenarios, in order, in a clean chat. Do not add extra instructions — the point is to observe what the rules alone elicit.

---

## Scenario A — L-sized feature (should trigger a full plan)

> I want to add optional end-to-end encryption for user notes in our app: encrypt note bodies at rest on the client, add a key-management flow, migrate existing plaintext notes, update the settings UI, and document it. Please plan this.

Expected rule-driven behavior: a triage line sizing this around **L** (cross-cutting, migration, multi-surface), then a detailed plan following the planning-standards structure (phases, tests, dual wiki updates, PDCA remediation, drift-prevention gate, rollback), and a proposal to tier models (cheap subagent for mechanical/migration edits, high-tier for the crypto/key-management design).

---

## Scenario B — S-sized change (should NOT be over-planned)

> Rename the function `getCwd` to `getCurrentWorkingDirectory` across the repo.

Expected rule-driven behavior: a triage line sizing this around **S** (a few files, mechanical rename), an explicit statement that it will execute directly with **no** strategy subagent, and optionally a note that the mechanical edits suit the cheap tier / built-in search. It should **not** produce a heavyweight 10-section plan or spawn a strategy pass — the gate must prevent over-investment.
