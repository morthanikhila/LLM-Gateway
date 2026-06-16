from app.providers.base import LLMProvider


class GeminiAdapter(LLMProvider):

    def generate(self, request):
        print("Generating response using Gemini")