#!/usr/bin/env bash
# Frozen template — copy to agents/recipes/<name>/ and customize if needed.
# Sends a unified diff to an OpenAI-compatible chat completions endpoint; writes Markdown.
set -euo pipefail

usage() {
  echo "Usage: $0 [--diff-file PATH] [--out PATH]"
  echo "  Reads unified diff from --diff-file or stdin. Writes Markdown to --out or stdout."
  echo "  Requires LLM_API_KEY or OPENAI_API_KEY. See README.md."
  exit 1
}

DIFF_FILE=""
OUT_FILE=""
while [[ $# -gt 0 ]]; do
  case "$1" in
    --diff-file)
      DIFF_FILE="${2:?}"
      shift 2
      ;;
    --out)
      OUT_FILE="${2:?}"
      shift 2
      ;;
    -h|--help)
      usage
      ;;
    *)
      echo "Unknown option: $1" >&2
      usage
      ;;
  esac
done

KEY="${LLM_API_KEY:-${OPENAI_API_KEY:-}}"
if [[ -z "$KEY" ]]; then
  echo "llm-diff-review: set LLM_API_KEY or OPENAI_API_KEY" >&2
  exit 1
fi

API_URL="${LLM_API_URL:-https://api.openai.com/v1/chat/completions}"
MODEL="${LLM_MODEL:-gpt-4o-mini}"

TMP_DIFF="$(mktemp)"
PAYLOAD=""
RESP=""
cleanup() { rm -f "$TMP_DIFF" "${PAYLOAD:-}" "${RESP:-}"; }
trap cleanup EXIT

if [[ -n "$DIFF_FILE" ]]; then
  if [[ ! -f "$DIFF_FILE" ]]; then
    echo "llm-diff-review: diff file not found: $DIFF_FILE" >&2
    exit 1
  fi
  cp "$DIFF_FILE" "$TMP_DIFF"
else
  cat >"$TMP_DIFF"
fi

if [[ ! -s "$TMP_DIFF" ]]; then
  echo "llm-diff-review: empty diff; nothing to review" >&2
  exit 1
fi

SYSTEM_PROMPT='You are a senior code reviewer. Given a unified diff, produce a concise Markdown report with sections: Summary, Risks, Suggestions, and Tests / verification notes. Use bullet lists. Do not invent files or changes not shown in the diff. If the diff is huge, focus on the riskiest hunks first.'

PAYLOAD="$(mktemp)"

jq -n \
  --arg model "$MODEL" \
  --arg sys "$SYSTEM_PROMPT" \
  --rawfile diff "$TMP_DIFF" \
  '{
    model: $model,
    messages: [
      {role: "system", content: $sys},
      {role: "user", content: ("Unified diff:\n\n" + $diff)}
    ],
    temperature: 0.2
  }' >"$PAYLOAD"

RESP="$(mktemp)"

HTTP_CODE="$(curl -sS -o "$RESP" -w '%{http_code}' \
  -X POST "$API_URL" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $KEY" \
  -d @"$PAYLOAD")"

if [[ "$HTTP_CODE" != "200" ]]; then
  echo "llm-diff-review: API HTTP $HTTP_CODE" >&2
  cat "$RESP" >&2
  exit 1
fi

if jq -e '.error' "$RESP" >/dev/null 2>&1; then
  echo "llm-diff-review: API error body:" >&2
  jq . "$RESP" >&2
  exit 1
fi

CONTENT="$(jq -r '.choices[0].message.content // empty' "$RESP")"
if [[ -z "$CONTENT" ]]; then
  echo "llm-diff-review: empty model response" >&2
  exit 1
fi

if [[ -n "$OUT_FILE" ]]; then
  mkdir -p "$(dirname "$OUT_FILE")"
  printf '%s\n' "$CONTENT" >"$OUT_FILE"
  echo "llm-diff-review: wrote $OUT_FILE"
else
  printf '%s\n' "$CONTENT"
fi
