from pydantic import Field

from app.adapter.inbound.web.base_schema import BaseSchema


class LoginResponse(BaseSchema):
    access_token: str = Field()
    refresh_token: str = Field()
