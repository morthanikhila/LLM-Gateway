from app.providers.base import LLMProvider


class OpenAIAdapter(LLMProvider):

    def generate(self, request):
        print("Generating response using OpenAI")