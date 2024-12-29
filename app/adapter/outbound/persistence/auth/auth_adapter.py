from app.adapter.outbound.persistence.user import UserRepository, UserMapper
from app.adapter.outbound.persistence.refresh_token import RefreshTokenRepository
from app.application.port.outbound.auth import LoginPort, SignupPort
from fastapi import status
from fastapi.exceptions import HTTPException
from prisma.errors import UniqueViolationError
from app.domain.user import User
from prisma.models import User as PrismaUser

from .auth_repository import AuthRepository

from app.domain.auth import JwtToken


class AuthAdapter(LoginPort, SignupPort):

    def __init__(
        self,
        auth_repository: AuthRepository,
        user_repository: UserRepository,
        refresh_token_repository: RefreshTokenRepository,
    ) -> None:
        self.auth_repository = auth_repository
        self.user_repository = user_repository
        self.refresh_token_repository = refresh_token_repository

    async def login(self, email: str, password: str) -> JwtToken:
        user = await self.user_repository.get_user_by_email(email=email)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="존재하지 않는 이메일이거나 비밀번호가 틀렸습니다.",
                headers={"WWW-Authenticate": "Bearer"},
            )
        elif not self.auth_repository.verify_hash(password, user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="비밀번호가 틀렸습니다.",
                headers={"WWW-Authenticate": "Bearer"},
            )

        access_token, refresh_token = JwtToken.get_tokens(
            data={"sub": user.email},
        )

        return JwtToken.generate_jwt_token(
            access_token=JwtToken.AccessToken(access_token),
            refresh_token=JwtToken.RefreshToken(access_token),
        )

    async def signup(self, email: str, password: str, username: str) -> User:
        try:
            hashed_password = self.auth_repository.get_hash(password=password)
            user: PrismaUser = await self.user_repository.create_user(
                email=email, hashed_password=hashed_password, username=username
            )

            return UserMapper.map_to_domain(user_entity=user)

        except UniqueViolationError as e:
            errTarget = (
                "이메일" if str(e.data["error"]).find("email") != -1 else "사용자명"
            )
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"이미 존재하는 {errTarget}입니다.",
            )
