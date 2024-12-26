from abc import ABC, abstractmethod

from app.application.port.inbound.auth import SignupCommand
from app.domain.user import User


class SignupUseCase(ABC):
    @abstractmethod
    def __init__(self):
        pass

    async def signup(self, command: SignupCommand) -> User:
        return self._signup(command=command)

    @abstractmethod
    async def _signup(self, command: SignupCommand) -> User:
        raise NotImplementedError
