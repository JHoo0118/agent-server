from typing import AsyncGenerator

from app.application.port.inbound.ai.algorithm_advice import (
    AlgorithmAdviceGenerateCommand,
)
from app.application.port.outbound.ai.algorithm_advice import (
    AlgorithmAdviceGeneratePort,
)


class AlgorithmAdviceService:
    def __init__(
        self, algorithm_advice_generate_port: AlgorithmAdviceGeneratePort
    ) -> None:
        self.algorithm_advice_generate_port = algorithm_advice_generate_port
        pass

    async def generate(self, command: AlgorithmAdviceGenerateCommand) -> AsyncGenerator:
        async for token in self.algorithm_advice_generate_port.generate(
            email=command.email, message=command.message, lang=command.lang
        ):
            yield token
