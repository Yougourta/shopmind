"""Logging configuration and setup."""

import logging
from logging.handlers import RotatingFileHandler
from config import LOG_LEVEL

# Logger
logger = logging.getLogger()
logger.setLevel(LOG_LEVEL)

# Console handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# Add handlers to logger
logger.addHandler(console_handler)

# Suppress verbose logs from libraries
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("anthropic").setLevel(logging.WARNING)
logging.getLogger("openai").setLevel(logging.WARNING)