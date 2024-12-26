from abc import ABC, abstractmethod


from app.domain.user import User


class SignupPort(ABC):
    @abstractmethod
    def __init__(self):
        pass

    async def signup(self, email: str, password: str, username: str) -> User:
        return self._signup(email=email, password=password, username=username)

    async def _signup(self, email: str, password: str, username: str) -> User:
        raise NotImplementedError
