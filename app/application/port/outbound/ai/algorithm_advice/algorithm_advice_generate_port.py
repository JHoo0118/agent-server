from abc import ABC, abstractmethod
from typing import AsyncGenerator


class AlgorithmAdviceGeneratePort(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    async def generate(
        self,
        email: str,
        lang: str,
        message: str,
    ) -> AsyncGenerator:
        async for token in self._generate(email, lang, message):
            yield token

    async def _generate(
        self,
        email: str,
        lang: str,
        message: str,
    ) -> AsyncGenerator:
        raise NotImplementedError
