from abc import ABC, abstractmethod


class DiagramErdGeneratePort(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    async def generate(
        self,
        email: str,
        query: str,
    ) -> str:
        return self._generate(
            email=email,
            query=query,
        )

    async def _generate(
        self,
        email: str,
        query: str,
    ) -> str:
        raise NotImplementedError
