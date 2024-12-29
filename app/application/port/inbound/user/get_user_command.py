from pydantic import Field

from app.application.port.inbound.base_command import BaseCommand


class GetUserCommand(BaseCommand):
    email: str = Field()
