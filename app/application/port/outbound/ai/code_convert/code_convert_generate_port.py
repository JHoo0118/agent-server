from abc import ABC, abstractmethod


class CodeConvertGeneratePort(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    async def generate(
        self, email: str, code: str, code_type: str, target_code_type: str
    ) -> str:
        return self._generate(
            email=email,
            code=code,
            code_type=code_type,
            target_code_type=target_code_type,
        )

    async def _generate(
        self, email: str, code: str, code_type: str, target_code_type: str
    ) -> str:
        raise NotImplementedError
