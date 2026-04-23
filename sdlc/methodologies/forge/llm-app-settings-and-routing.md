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
- **ollama** / **openai_compatible:** Custom and local models use an explicit HTTP(S) **base URL** on the server. **`OLLAMA_BASE_URL` is required** for the native Ollama provider; **`LENSES_OPENAI_COMPAT_BASE_URL` is required** for OpenAI-compatible `/v1/chat/completions` (LM Studio, tunnels, local Ollama’s OpenAI shim, etc.). Quality order may be **user-defined** list or single model until a ladder exists.

**Secrets:** API keys for Lenses must live on the **Python server** (file under workspace-local gitignored paths or environment variables), never in browser storage. Access to settings APIs should match other privileged local APIs (loopback by default).

---

## 5. Versioning and maintenance

- **Quality order lists** change when vendors ship new models; bump a **doc version** or app changelog when defaults change.
- **Remote model refresh** (optional): periodic fetch when keys exist, with cache TTL—see mobile implementation patterns.

---

## 6. Lenses Studio — AI Setup surface (UX contract)

Lenses Studio exposes an **AI Setup** page (URL `/studio/settings/llm`; historically “LLM preferences”). The page answers four questions **in order**:

1. **Which LLM sources are in play?** Group by **source type**, not by raw credential fields first: **cloud** (OpenAI, Anthropic, Google, …), **custom** (OpenAI-compatible gateway), **local** (Ollama with explicit base URL on the server).
2. **How should Studio route work?** **Single model** (one active provider + manual or simple default), **Smart multi-model** (tier ladder + optional adaptive classifier within a provider’s pool), **Advanced routing** (full pool/tier/adaptive/refinement controls). Technical flags in settings may still map to §1–§3; product copy should use these three names.
3. **What is each model used for?** Optional **per–task-category** routes (see §6.1) let different Studio surfaces use different providers/models in parallel (MVP: one route per category per request — **not** same-task fan-out, compare, judge, or consensus).
4. **Diagnostics** — provider reachability, usage aggregates, recent failures, links to logs and technical details.

### 6.1 Studio task categories (product language)

These labels are **user-facing**. Implementations should map each category to a stable **`studio_task_id`** string on API boundaries so routing preview and runtime stay aligned.

| Studio task (label) | `studio_task_id` | Typical Studio surfaces |
|---------------------|------------------|-------------------------|
| Chat assistant | `chat_assistant` | LLM chat (demo), long-form chat-style calls |
| Search / knowledge answers | `search_knowledge` | Grounded SDLC copilot (Ask), header Ask |
| Plans / roadmaps generation | `plans_generation` | Blueprints Wizard interpretation, artifact generation, wizard refine |
| Site / blog drafting | `site_drafting` | Reserved for site/blog drafting flows when wired |
| Code / automation | `code_automation` | Reserved for automation or code-oriented flows when wired |
| Extraction / classification | `extraction_classification` | Wizard clarification suggestions and similar extractive calls |
| Vision / OCR | `vision_ocr` | Reserved for vision/OCR when wired |
| Embeddings / indexing | `embeddings_indexing` | Reserved when an embeddings path exists; may appear as settings-only until implemented |

Classifier **`task`** values in §3 (`CHAT`, `CODE`, …) describe **prompt shape** for adaptive adjustment inside a provider. They are **not** the same as `studio_task_id`; a single `studio_task_id` may still use adaptive routing when enabled.

### 6.2 Progressive disclosure

- **Zero providers connected (no effective credentials):** Guided empty state — connect at least one cloud key, custom base URL, or Ollama URL on the **server**; link to documentation and a safe “test chat” path.
- **Exactly one provider connected:** Emphasize that provider, default model, and **Test setup**; do **not** surface Smart multi-model or Advanced routing as primary choices (may remain in collapsed technical/advanced affordance if needed for support).
- **Two or more providers connected:** Show **Smart multi-model** and **Advanced routing** as first-class options; allow **per–task-category** overrides (§6.1).

### 6.3 Quality presets and transparency

Quality remains a **discrete tier** relative to the user’s **ordered pool** (§1.3, §2), not a promise of dollar cost. Product presets (e.g. Speed / Balanced / Quality / Max) **map to tier names** with short copy: moving toward “Speed” shifts selection toward **weaker/cheaper slots** in the pool; “Max” toward **stronger** slots. The UI should show a **live routing preview** (resolved model per task category or per provider) whenever presets or pools change, so the slider is not “magical.”

### 6.4 Settings file and versioning

Studio persists UI settings under **`<workspace>/.lenses-local/llm-settings.json`** (gitignored). When adding fields (e.g. `task_routes`, `routing_mode`, `fallback_route`), **bump `version`** and migrate older files on load so operators are not stranded on legacy shapes.

### 6.5 Explicit MVP boundary (multi-LLM)

**In scope (MVP):** Parallel routing **across task categories** — e.g. chat on one provider, grounded Ask on another, wizard generation on a third, Ollama for local experimentation.

**Out of scope (later):** Sending the **same** user prompt to **multiple** models in parallel, output comparison, judge models, or consensus flows — larger backend, cost, and UX surface.

---

## See also

- Situ8 reference implementation: `ModelSelectionResolver`, `AdaptiveModelMapper`, `LlmModels` (Kotlin).
- Lenses: `lenses/llm_routing.py`, `lenses/llm_resolve.py`, `lenses/llm_studio_tasks.py`, `lenses/llm_settings_store.py`, README (Studio AI Setup).
