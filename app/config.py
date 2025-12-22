import os
from dotenv import load_dotenv

load_dotenv()

ENV = os.getenv("ENV", "dev")

DATABASE_URL = os.getenv("DATABASE_URL")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
API_KEY = os.getenv("API_SECRET_KEY")

AI_ENABLED = os.getenv("AI_ENABLED", "false").lower() == "true"


if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set")

if not API_KEY:
    raise RuntimeError("API_KEY is not set")
