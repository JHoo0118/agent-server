from abc import ABC, abstractmethod

# from app.domain.auth import JwtToken


class LoginPort(ABC):
    @abstractmethod
    def __init__(self):
        pass

    async def login(self, email: str, password: str):
        return self._login(email=email, password=password)

    async def _login(self, email: str, password: str):
        raise NotImplementedError
