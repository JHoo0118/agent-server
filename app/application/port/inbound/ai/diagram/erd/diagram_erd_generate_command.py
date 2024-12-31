from pydantic import EmailStr, Field

from app.application.port.inbound.base_command import BaseCommand


class DiagramErdGenerateCommand(BaseCommand):
    email: EmailStr = Field()
    query: str = Field()
