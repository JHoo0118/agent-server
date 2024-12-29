from app.application.port.inbound.ai.code_convert import CodeConvertGenerateCommand
from app.application.port.outbound.ai.code_convert import CodeConvertGeneratePort


class CodeConvertService:

    def __init__(self, code_convert_generate_port: CodeConvertGeneratePort) -> None:
        self.code_convert_generate_port = code_convert_generate_port

    async def generate(self, command: CodeConvertGenerateCommand) -> str:
        return await self.code_convert_generate_port.generate(
            email=command.email,
            code=command.code,
            code_type=command.code_type,
            target_code_type=command.target_code_type,
        )
