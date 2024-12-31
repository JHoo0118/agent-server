from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Body, Depends, Request

from app.application.port.inbound.ai.diagram.erd import (
    DiagramErdGenerateCommand,
    DiagramErdGenerateUseCase,
)
from app.configurator.containers import Container

from .diagram_erd_generate_request import DiagramErdGenerateRequest
from .diagram_erd_generate_response import DiagramErdGenerateResponse

router = APIRouter(
    prefix="/erd",
    tags=["ai"],
    dependencies=[],
    responses={404: {"description": "찾을 수 없습니다."}},
)


@router.post("/generate")
@inject
async def diagram_erd_generate(
    request: Request,
    body: DiagramErdGenerateRequest = Body(...),
    use_case: DiagramErdGenerateUseCase = Depends(
        Provide[Container.diagram_erd_service]
    ),
):
    email: str = request.state.email

    command = DiagramErdGenerateCommand(
        email=email,
        query=body.query,
    )
    image = await use_case.generate(command)
    return DiagramErdGenerateResponse(image=image)
