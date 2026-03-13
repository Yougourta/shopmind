# ShopMind

An AI-powered shopping assistant agent built with Claude, LangGraph, and ChromaDB.

## Setup

1. Create and activate the virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   ```

2. Install dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

3. Copy `.env.example` to `.env` and fill in your API keys:
   ```bash
   cp .env.example .env
   ```

## Usage

```bash
python main.py
```

## Development

Run tests:
```bash
pytest
```

Run a single test file:
```bash
pytest tests/test_models.py
```

## Project Structure

```
shopmind/
├── src/
│   ├── agent.py       # LangGraph agent definition and graph
│   ├── config.py      # Settings loaded from environment
│   ├── logger.py      # Logging setup
│   ├── models.py      # Pydantic data models
│   └── tools.py       # Agent tools (search, vector store, etc.)
├── prompts/
│   ├── profiling.yaml       # User profiling prompt templates
│   └── recommendation.yaml  # Product recommendation prompt templates
├── data/              # ChromaDB persistence (gitignored)
├── tests/
└── main.py            # Entry point
```
