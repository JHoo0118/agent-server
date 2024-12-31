from app.application.port.inbound.ai.diagram.erd import DiagramErdGenerateCommand
from app.application.port.outbound.ai.diagram.erd import DiagramErdGeneratePort


class DiagramErdService:

    def __init__(self, diagram_erd_generate_port: DiagramErdGeneratePort) -> None:
        self.diagram_erd_generate_port = diagram_erd_generate_port

    async def generate(self, command: DiagramErdGenerateCommand) -> str:
        return await self.diagram_erd_generate_port.generate(
            email=command.email, query=command.query
        )
