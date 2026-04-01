# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a Jupyter-notebook-based course teaching the Anthropic Claude API, organized into five modules:

- `01_api_basics/` — API fundamentals (requests, system prompts, streaming, output control)
- `02_prompt_evals/` — Prompting techniques and evaluation frameworks
- `03_tool_use/` — Tool use / function calling
- `04_rag/` — Retrieval-Augmented Generation (chunking, embeddings, vector search, BM25, hybrid retrieval)
- `05_features/` — Extended thinking, image inputs, prompt caching, code execution

## Commands

```bash
# Initial setup (creates .venv and installs dependencies)
bash setup.sh

# Activate environment
source .venv/bin/activate

# Launch Jupyter
jupyter notebook
```

## Environment Setup

A single `.env` at the repo root is shared by all modules. Required keys:
- `ANTHROPIC_API_KEY` — needed by all modules
- `VOYAGE_API_KEY` — needed only by `04_rag/`

`setup.py` at the repo root runs `load_dotenv()` and instantiates `client = Anthropic()`. Every notebook loads it with `%run ../setup.py` (or `%run setup.py` from the root).

## Architecture Patterns

**Consistent chat helper pattern**: Every notebook builds the same two helpers, each extending the previous module's version:
- `add_message(messages, role, content)` — appends to a messages list
- `chat(messages, system=None, temperature=1.0, stop_sequences=None)` — calls `client.messages.create()` and returns the text

`05_features/` splits this into `add_user_message` / `add_assistant_message` and extends `chat()` with `thinking` and `thinking_budget` params.

**JSON extraction via prefill + stop sequences**: Seed the assistant turn with ` ```json` and set `stop_sequences=["```"]` to force structured output, then parse directly with `json.loads()`.

**LLM-as-judge**: The eval framework (`02_prompt_evals/001_exercise.ipynb`) uses Claude at `temperature=0.0` to grade outputs on a 1–10 scale, combined with deterministic syntax validators (`json.loads`, `ast.parse`, `re.compile`).

**From-scratch implementations**: `VectorIndex`, `BM25Index`, `Retriever`, and all chunking strategies in `04_rag/` are implemented without external libraries (intentionally educational — no LangChain/LlamaIndex).

**Concurrency**: `concurrent.futures.ThreadPoolExecutor` is used in `02_prompt_evals/001_exercise.ipynb` for parallel dataset generation and grading. The `04_rag/005_hybrid.ipynb` `Retriever` uses a `SearchIndex` Protocol to type-check pluggable backends.

**Model usage**:
- `claude-sonnet-4-6` — general-purpose notebooks (latest)
- `claude-haiku-4-5` — high-volume eval/grading (cost efficiency)
