from abc import ABC, abstractmethod
from typing import AsyncGenerator

from .algorithm_advice_generate_command import AlgorithmAdviceGenerateCommand


class AlgorithmAdviceGenerateUseCase(ABC):
    @abstractmethod
    def __init__(self):
        pass

    async def generate(self, command: AlgorithmAdviceGenerateCommand) -> AsyncGenerator:
        return self._generate(command=command)

    @abstractmethod
    async def _generate(
        self, command: AlgorithmAdviceGenerateCommand
    ) -> AsyncGenerator:
        raise NotImplementedError
