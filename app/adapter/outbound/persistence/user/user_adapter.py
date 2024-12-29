from app.application.port.outbound.user import GetUserPort

from .user_repository import UserRepository


class UserAdapter(GetUserPort):

    def __init__(
        self,
        user_repository: UserRepository,
    ) -> None:
        self.user_repository = user_repository

    async def get_user_by_email(self, email: str):
        return self.user_repository.get_user_by_email(email=email)
