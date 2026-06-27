from app.providers.openai_adapter import OpenAIAdapter
from app.providers.gemini_adapter import GeminiAdapter


class ModelRouter:

    def get_provider(self, model: str):

        if model.startswith("gpt"):
            return OpenAIAdapter()

        elif model.startswith("gemini"):
            return GeminiAdapter()

        else:
            raise ValueError(f"Unsupported model: {model}")