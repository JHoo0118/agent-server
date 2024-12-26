from pydantic import Field

from app.application.port.inbound.base_command import BaseCommand


class LoginCommand(BaseCommand):
    email: str = Field()
    password: str = Field()
