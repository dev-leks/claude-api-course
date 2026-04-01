# Claude API Course

A Jupyter-notebook-based course covering the Anthropic Claude API from fundamentals to advanced retrieval patterns.

## Modules

| Folder | Topics |
|--------|--------|
| `01_api_basics/` | API requests, system prompts, streaming, output control |
| `02_prompt_evals/` | Prompting techniques, evaluation frameworks, LLM-as-judge |
| `03_tool_use/` | Tool use / function calling |
| `04_rag/` | Chunking, embeddings, vector search, BM25, hybrid retrieval |
| `05_features/` | Extended thinking, image inputs, prompt caching, code execution |
| `06_mcp/` | MCP (Model Context Protocol) — building an MCP server and client CLI app |

## Setup

```bash
# 1. Clone the repo
git clone <repo-url>
cd claude-api-course

# 2. Create environment file
cp .env.example .env
# Fill in your API keys in .env

# 3. Install dependencies (creates .venv and installs all packages)
bash setup.sh
```

## Running Notebooks

Open any notebook in VS Code (with the Jupyter extension) or JupyterLab and select the `.venv` kernel.

Each notebook starts with `%run ../setup.ipynb` (or `%run setup.ipynb` for root-level notebooks) which loads environment variables and creates the Anthropic client.

## Required API Keys

- `ANTHROPIC_API_KEY` — required by all modules
- `VOYAGE_API_KEY` — required by the `04_rag/` module only
