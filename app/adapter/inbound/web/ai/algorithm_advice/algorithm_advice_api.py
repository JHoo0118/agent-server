from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Body, Depends, Request
from fastapi.responses import StreamingResponse

from app.application.port.inbound.ai.algorithm_advice import (
    AlgorithmAdviceGenerateCommand,
    AlgorithmAdviceGenerateUseCase,
)
from app.configurator.containers import Container

from .algorithm_advice_generate_request import AlgorithmAdviceGenerateRequest

router = APIRouter(
    prefix="/algorithm",
    tags=["ai"],
    dependencies=[],
    responses={404: {"description": "찾을 수 없습니다."}},
)


@router.post("/generate")
@inject
async def code_convert_generate(
    request: Request,
    body: AlgorithmAdviceGenerateRequest = Body(...),
    use_case: AlgorithmAdviceGenerateUseCase = Depends(
        Provide[Container.algorithm_advice_service]
    ),
) -> StreamingResponse:
    email: str = request.state.email

    lastMessage = body.messages[-1].content

    command = AlgorithmAdviceGenerateCommand(
        email=email, lang=body.lang, message=lastMessage
    )

    return StreamingResponse(use_case.generate(command))
