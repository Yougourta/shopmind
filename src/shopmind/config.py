"""Application configuration loaded from environment variables."""

import os
import yaml
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

PROMPTS_DIR = Path(__file__).parent / "config"

def load_prompt(prompt_name: str) -> str:
    with open(PROMPTS_DIR / f"{prompt_name}.yaml", "r", encoding="utf-8") as f:
        return f.read()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
MODEL = os.getenv("MODEL_NAME", "claude-opus-4-6")
MAX_TOKENS = os.getenv("MAX_TOKENS", 1024)
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
TAVILY_MAX_RESULTS = os.getenv("TAVILY_MAX_RESULTS", 5)
CHROMA_API_KEY = os.getenv("CHROMA_API_KEY")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
CHROMA_PERSIST_DIR = os.getenv("CHROMA_PERSIST_DIR", "./data/chroma_db")
CHROMA_COLLECTION_NAME = os.getenv("CHROMA_COLLECTION_NAME", "strollers")