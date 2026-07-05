from app.routing.model_router import ModelRouter
from app.schemas.chat_request import ChatRequest


class ChatService:

    def __init__(self):
        self.router = ModelRouter()

    def chat(self, request: ChatRequest):

        provider = self.router.get_provider(request.model)

        return provider.generate(request)