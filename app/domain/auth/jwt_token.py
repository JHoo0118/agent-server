from pydantic import Field

from dataclasses import asdict, dataclass
from app.adapter.inbound.web.base_schema import BaseSchema
from app.configurator.config import settings
from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone
from fastapi import status
from fastapi.exceptions import HTTPException
from typing import ClassVar


@dataclass
class JwtToken(BaseSchema):
    access_token: str = Field()
    refresh_token: str = Field()
    credentials_exception: ClassVar[HTTPException] = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="토큰이 유효하지 않거나 만기된 토큰입니다.",
        headers={"WWW-Authenticate": "Bearer"},
    )

    @classmethod
    def from_dict(cls, dict_):
        return cls(**dict_)

    def to_dict(self):
        return asdict(self)

    @classmethod
    def generate_jwt_token(
        cls,
        access_token: str,
        refresh_token: str,
    ) -> "JwtToken":
        return cls.model_construct(
            access_token=access_token,
            refresh_token=refresh_token,
        )

    @staticmethod
    def create_access_token(data: dict) -> str:

        to_encode = JwtToken.__get_to_encode(
            data.copy(), settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
        encoded_jwt = jwt.encode(
            to_encode, settings.ACCESS_TOKEN_KEY, algorithm=settings.ALGORITHM
        )
        return encoded_jwt

    @staticmethod
    def create_refresh_token(data: dict) -> str:
        to_encode = JwtToken.__get_to_encode(
            data.copy(), settings.REFRESH_TOKEN_EXPIRE_MINUTES
        )
        encoded_jwt = jwt.encode(
            to_encode, settings.REFRESH_TOKEN_KEY, algorithm=settings.ALGORITHM
        )
        return encoded_jwt

    @staticmethod
    def get_tokens(data: dict):
        return JwtToken.create_access_token(data), JwtToken.create_refresh_token(data)

    @staticmethod
    async def verify_token(token: str, token_key: str) -> str:
        try:
            payload = jwt.decode(
                token,
                key=token_key,
                algorithms=[settings.ALGORITHM],
                audience="authenticated",
            )
            email: str = payload.get("email")
            if email is None:
                raise JwtToken.credentials_exception
            return email
        except JWTError:
            raise JwtToken.credentials_exception

    @staticmethod
    def __get_to_encode(data: dict, expire_minutes: int) -> dict:
        expires_delta = timedelta(minutes=expire_minutes)

        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        return to_encode
