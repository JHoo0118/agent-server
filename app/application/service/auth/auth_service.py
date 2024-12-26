# import os
# import requests
from fastapi.security import OAuth2PasswordBearer

from app.application.port.inbound.auth import LoginCommand, SignupCommand
from app.application.port.outbound.auth import LoginPort, SignupPort
from app.domain.auth import JwtToken

from app.domain.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth/login")


class AuthService:

    def __init__(self, login_port: LoginPort, signup_port: SignupPort) -> None:
        self.login_port = login_port
        self.signup_port = signup_port

    async def login(self, command: LoginCommand) -> JwtToken:
        return await self.login_port.login(
            email=command.email, password=command.password
        )

    async def signup(self, command: SignupCommand) -> User:
        return await self.signup_port.signup(
            email=command.email, password=command.password, username=command.username
        )
