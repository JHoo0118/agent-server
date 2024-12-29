from abc import ABC, abstractmethod

from app.application.port.inbound.ai.code_convert import CodeConvertGenerateCommand


class CodeConvertGenerateUseCase(ABC):
    @abstractmethod
    def __init__(self):
        pass

    async def generate(self, command: CodeConvertGenerateCommand) -> str:
        return self._generate(command=command)

    @abstractmethod
    async def _generate(self, command: CodeConvertGenerateCommand) -> str:
        raise NotImplementedError
