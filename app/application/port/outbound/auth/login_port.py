from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.domain.auth import JwtToken


class LoginPort(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    async def login(self, email: str, password: str) -> JwtToken:
        return self._login(email=email, password=password)

    async def _login(self, email: str, password: str) -> JwtToken:
        raise NotImplementedError
