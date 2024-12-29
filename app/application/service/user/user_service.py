from fastapi.security import OAuth2PasswordBearer
from app.domain.auth import JwtToken
from app.application.port.outbound.user import GetUserPort
from app.application.port.inbound.user import GetUserCommand

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth/login")


class UserService:

    def __init__(
        self,
        get_user_port: GetUserPort,
    ) -> None:
        self.get_user_port = get_user_port

    async def get_user_by_email(self, command: GetUserCommand) -> JwtToken:
        return await self.get_user_port.get_user_by_email(email=command.email)
