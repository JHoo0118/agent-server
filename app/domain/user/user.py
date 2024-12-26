from dataclasses import asdict, dataclass
from app.adapter.inbound.web.base_schema import BaseSchema
import datetime
from typing import Any, Optional


@dataclass
class User(BaseSchema):
    email: str
    username: str
    password: str
    type: str
    disabled: bool
    remain_count: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    refreshToken: Optional[Any] = None

    @classmethod
    def from_dict(cls, dict_):
        return cls(**dict_)

    def to_dict(self):
        return asdict(self)

    @classmethod
    def generate_user(
        cls,
        email: str,
        username: str,
        password: str,
        type: str,
        disabled: bool,
        remain_count: int,
        created_at: datetime,
        updated_at: datetime,
        refreshToken: Optional[str] = None,
    ) -> "User":
        return cls.model_construct(
            email=email,
            username=username,
            password=password,
            type=type,
            disabled=disabled,
            remain_count=remain_count,
            created_at=created_at,
            updated_at=updated_at,
            refreshToken=refreshToken,
        )
