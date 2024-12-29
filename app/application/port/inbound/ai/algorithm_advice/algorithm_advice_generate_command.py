from pydantic import EmailStr, Field

from app.application.port.inbound.base_command import BaseCommand


class AlgorithmAdviceGenerateCommand(BaseCommand):
    email: EmailStr = Field()
    lang: str = Field()
    message: str = Field()
