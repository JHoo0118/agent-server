from abc import ABC, abstractmethod

from .code_convert_generate_command import CodeConvertGenerateCommand


class CodeConvertGenerateUseCase(ABC):
    @abstractmethod
    def __init__(self):
        pass

    async def generate(self, command: CodeConvertGenerateCommand) -> str:
        return self._generate(command=command)

    @abstractmethod
    async def _generate(self, command: CodeConvertGenerateCommand) -> str:
        raise NotImplementedError
