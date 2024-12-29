from pydantic import EmailStr, Field

from app.application.port.inbound.base_command import BaseCommand


class CodeConvertGenerateCommand(BaseCommand):
    email: EmailStr = Field()
    code: str = Field()
    code_type: str = Field()
    target_code_type: str = Field()
