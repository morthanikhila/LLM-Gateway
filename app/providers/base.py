# app/providers/base.py

from abc import ABC, abstractmethod


class LLMProvider(ABC):

    @abstractmethod
    def generate(self, request):
        pass