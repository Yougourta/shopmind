"""Application configuration loaded from environment variables."""

import os
from dotenv import load_dotenv

load_dotenv()

MODEL = os.getenv("MODEL", "claude-opus-4-6")
MAX_TOKENS = os.getenv("MAX_TOKENS", 1024)
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
TAVILY_MAX_RESULTS = os.getenv("TAVILY_MAX_RESULTS", 5)
CHROMA_API_KEY = os.getenv("CHROMA_API_KEY")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
