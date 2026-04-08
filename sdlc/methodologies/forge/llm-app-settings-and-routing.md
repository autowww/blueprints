---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# LLM app settings and model routing

**Status:** Normative for Forge-family apps that expose user-tunable LLM behavior (e.g. Situ8, Lenses Studio).  
**Goal:** Reusable definitions for quality/cost tradeoffs, automatic model selection, optional adaptive routing, and refinement passes—without tying docs to a single vendor’s pricing page.

---

## 1. Concepts

### 1.1 Quality order (per provider)

Each provider exposes a **curated list of model ids** in **best-first** order: index **0** is the strongest model in that list (often highest typical cost/latency); the last index is the weakest/cheapest in the list. Lists are **vendor-specific** and must be **versioned** when provider APIs add or rename models.

Apps may **union** this list with remotely discovered ids (e.g. OpenAI `/v1/models`); unknown ids are appended in a stable order (e.g. lexicographic) after known ids.

### 1.2 User pool

The user enables a **subset** of models (checkboxes / swimlanes). **Auto** mode only considers models in **(pool ∩ catalog)** where *catalog* is the union of bundled defaults and remote ids.

### 1.3 Quality tier (cost / quality “slider”)

Cloud quality is represented as a discrete **tier** (not continuous dollars):

| Tier (name) | Role in auto mode |
|-------------|-------------------|
| TOP … EXTRA_LOW | Maps linearly to an index along the **ordered pool** (see §2). |

**NONE** is reserved for “offline / invalid for this cloud path” in apps that support offline inference; web servers like Lenses may omit it.

**Semantics:** Moving the slider toward **EXTRA_LOW** prefers **cheaper/weaker** models in the pool; toward **TOP** prefers **stronger** models—**relative** to the ordered list, not an absolute price guarantee.

### 1.4 Manual vs auto

- **Manual:** One **main model id** per active provider; requests use that id unless overridden per call.
- **Auto:** Requires **advanced UI** and **auto** enabled. Resolves an id from **tier + ordered pool** (§2).

### 1.5 Adaptive autoselection (optional)

When **adaptive** is on (and auto + advanced):

1. A **small classifier** call classifies the user prompt into **task** and **complexity** (see §3).
2. An **adjustment** step shifts the tier-derived index within the pool toward stronger or cheaper models (same spirit as Situ8’s `AdaptiveModelMapper`).

**Tradeoff:** Adds **latency** and **token cost** for the classifier hop; users must be told in UI.

### 1.6 Refinement downshift (policy extension)

For **second and later** passes in the same conversation or workflow (e.g. polish, compact, “refine again”), apps may apply a **refinement policy**:

- **Index downshift:** Move **N** steps toward **cheaper** (increase index in best-first order) within the pool, capped at the last model.
- Optionally lower **max output tokens** for refinement-only calls.

This is **not** always how mobile intake refine works; it is an explicit **policy** for cost-sensitive loops.

---

## 2. Tier to index mapping (auto mode)

Let `ordered` = filtered quality order restricted to the user pool, length `n`.

If `n == 0`, fall back to the **main manual** model id for that provider.

If `n == 1`, use that single id.

Otherwise map tier to slot `s` in `0..5` (TOP → EXTRA_LOW), then:

`idx = floor(s * (n - 1) / 5)` clamped to `0..n-1`.

Return `ordered[idx]`.

This matches the linear mapping used in Situ8’s `ModelSelectionResolver.pickFromOrdered`.

---

## 3. Classifier output (adaptive)

Classifier returns structured JSON only, e.g.:

- **task:** `CHAT` | `CODE` | `REASONING` | `CREATIVE` | `SUMMARIZE` | `OTHER`
- **complexity:** `TRIVIAL` | `MODERATE` | `HEAVY`

Adjustment rules (conceptually): heavier tasks / complexity may shift toward **stronger** models (lower index); trivial / summarize may shift toward **cheaper** (higher index). Exact deltas are implementation-defined per app but should stay **within the pool**.

---

## 4. Lenses Studio (forge-lenses) mapping

Lenses supports multiple providers: **anthropic**, **openai**, **gemini**, **ollama**, **openai_compatible**.

- **openai** / **gemini:** Full tier ladder + optional adaptive classifier (same pattern as Situ8).
- **anthropic:** Maintain a **documented best-first list** for auto mode; if a ladder is not curated, fall back to **manual** main model only.
- **ollama** / **openai_compatible:** Local or custom endpoints; quality order may be **user-defined** list or single model until a ladder exists.

**Secrets:** API keys for Lenses must live on the **Python server** (file under workspace-local gitignored paths or environment variables), never in browser storage. Access to settings APIs should match other privileged local APIs (loopback by default).

---

## 5. Versioning and maintenance

- **Quality order lists** change when vendors ship new models; bump a **doc version** or app changelog when defaults change.
- **Remote model refresh** (optional): periodic fetch when keys exist, with cache TTL—see mobile implementation patterns.

---

## See also

- Situ8 reference implementation: `ModelSelectionResolver`, `AdaptiveModelMapper`, `LlmModels` (Kotlin).
- Lenses: `lenses/llm_routing.py`, `lenses/llm_settings_store.py`, README (Studio LLM).
