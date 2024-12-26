from pydantic import Field, EmailStr

from app.application.port.inbound.base_command import BaseCommand


class SignupCommand(BaseCommand):
    email: EmailStr = Field()
    password: str = Field()
    username: str = Field()
