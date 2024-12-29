from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from app.application.port.inbound.auth import LoginCommand

if TYPE_CHECKING:
    from app.domain.auth import JwtToken


class LoginUseCase(ABC):

    @abstractmethod
    def __init__(self):
        pass

    async def login(self, command: LoginCommand) -> JwtToken:
        return self._login(command=command)

    @abstractmethod
    async def _login(self, command: LoginCommand) -> JwtToken:
        raise NotImplementedError
