import datetime
from dataclasses import asdict, dataclass
from typing import Final, Optional

from app.adapter.inbound.web.base_schema import BaseSchema


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
    refreshToken: Optional[str]

    @classmethod
    def from_dict(cls, dict_):
        return cls(**dict_)

    def to_dict(self):
        return asdict(self)

    @classmethod
    def generate_user(
        cls,
        email: "User.Email",
        username: "User.Username",
        password: "User.Password",
        type: "User.Type",
        disabled: "User.Disabled",
        remain_count: "User.RemainCount",
        created_at: "User.CreatedAt",
        updated_at: "User.UpdatedAt",
        refreshToken: Optional["User.RefreshToken"] = None,
    ) -> "User":
        return cls.model_construct(
            email=email.email,
            username=username.username,
            password=password.password,
            type=type.type,
            disabled=disabled.disabled,
            remain_count=remain_count.remain_count,
            created_at=created_at.created_at,
            updated_at=updated_at.updated_at,
            refreshToken=refreshToken.refreshToken if refreshToken else None,
        )

    @dataclass(frozen=True)
    class Email:
        email: Final[str]

        def __init__(self, value: str):
            object.__setattr__(self, "email", value)

    @dataclass(frozen=True)
    class Username:
        username: Final[str]

        def __init__(self, value: str):
            object.__setattr__(self, "username", value)

    @dataclass(frozen=True)
    class Password:
        password: Final[str]

        def __init__(self, value: str):
            object.__setattr__(self, "password", value)

    @dataclass(frozen=True)
    class Type:
        type: Final[str]

        def __init__(self, value: str):
            object.__setattr__(self, "type", value)

    @dataclass(frozen=True)
    class Disabled:
        disabled: Final[bool]

        def __init__(self, value: bool):
            object.__setattr__(self, "disabled", value)

    @dataclass(frozen=True)
    class RemainCount:
        remain_count: Final[int]

        def __init__(self, value: int):
            object.__setattr__(self, "remain_count", value)

    @dataclass(frozen=True)
    class CreatedAt:
        created_at: Final[datetime.datetime]

        def __init__(self, value: datetime.datetime):
            object.__setattr__(self, "created_at", value)

    @dataclass(frozen=True)
    class UpdatedAt:
        updated_at: Final[datetime.datetime]

        def __init__(self, value: datetime.datetime):
            object.__setattr__(self, "updated_at", value)

    @dataclass(frozen=True)
    class RefreshToken:
        refreshToken: Final[Optional[str]]

        def __init__(self, value: Optional[str]):
            object.__setattr__(self, "refreshToken", value)
