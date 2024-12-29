from abc import ABC, abstractmethod


class GetUserPort(ABC):
    @abstractmethod
    def __init__(self):
        pass

    async def get_user_by_email(self, email: str):
        return self._get_user_by_email(email=email)

    async def _get_user_by_email(self, email: str):
        raise NotImplementedError
