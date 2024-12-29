from fastapi import HTTPException, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.application.port.inbound.user import GetUserCommand
from app.application.service.user import UserService
from app.configurator.config import settings


class JwtBearer(HTTPBearer):

    def __init__(
        self,
        only_email: bool = True,
        auto_error: bool = True,
    ):
        from app.configurator.containers import Container

        super(JwtBearer, self).__init__(auto_error=auto_error)
        self.user_service: UserService = Container.user_service
        self.only_email = only_email

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(
            JwtBearer, self
        ).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(
                    status_code=403, detail="Invalid authentication scheme."
                )
            payload = await self.verify_jwt(credentials.credentials)
            if not payload:
                raise HTTPException(
                    status_code=409, detail="토큰이 유효하지 않거나 만기된 토큰입니다."
                )
            return payload
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    async def verify_jwt(self, token: str) -> bool:
        try:
            from app.domain.auth import JwtToken

            payload = await JwtToken.verify_token(token, settings.ACCESS_TOKEN_KEY)
            if not self.only_email:
                payload = await self.user_service.get_user_by_email(
                    GetUserCommand(email=payload)
                )
        except Exception:
            payload = None
        return payload
