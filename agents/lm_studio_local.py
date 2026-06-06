import os

from anthropic import Anthropic
from dotenv import load_dotenv

LM_STUDIO_BASE_URL = "LM_STUDIO_BASE_URL"
LM_STUDIO_API_KEY_ENV = "LM_STUDIO_API_KEY"
# GEMMA_MODEL_NAME = "gemma"
GEMMA_MODEL_NAME = "qwen3.5-9b"

load_dotenv()

def create_local_chat_model() -> Anthropic:
    lm_studio_api_key = os.getenv(LM_STUDIO_API_KEY_ENV)
    lm_studio_base_url = os.getenv(LM_STUDIO_BASE_URL)

    if not lm_studio_api_key:
        raise ValueError(f"Missing required environment variable: {LM_STUDIO_API_KEY_ENV}")
    if not lm_studio_base_url:
        raise ValueError(f"Missing required environment variable: {LM_STUDIO_BASE_URL}")

    return Anthropic(
        api_key=lm_studio_api_key,
        base_url=lm_studio_base_url,
    )


llm_local = create_local_chat_model()
