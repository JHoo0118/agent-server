from abc import ABC, abstractmethod

from .diagram_erd_generate_command import DiagramErdGenerateCommand


class DiagramErdGenerateUseCase(ABC):
    @abstractmethod
    def __init__(self):
        pass

    async def generate(self, command: DiagramErdGenerateCommand) -> str:
        return self._generate(command=command)

    @abstractmethod
    async def _generate(self, command: DiagramErdGenerateCommand) -> str:
        raise NotImplementedError
