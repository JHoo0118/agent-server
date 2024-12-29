from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Request, Body, Depends
from app.application.port.inbound.ai.code_convert import (
    CodeConvertGenerateCommand,
    CodeConvertGenerateUseCase,
)
from .code_convert_generate_request import CodeConvertGenerateRequest
from .code_convert_generate_response import CodeConvertGenerateResponse
from app.configurator.containers import Container

router = APIRouter(
    prefix="/codeconvert",
    tags=["ai"],
    dependencies=[],
    responses={404: {"description": "찾을 수 없습니다."}},
)


@router.post("/generate")
@inject
async def code_convert_generate(
    request: Request,
    body: CodeConvertGenerateRequest = Body(...),
    use_case: CodeConvertGenerateUseCase = Depends(
        Provide[Container.code_convert_service]
    ),
):
    email: str = request.state.email

    command = CodeConvertGenerateCommand(
        email=email,
        code=body.code,
        code_type=body.code_type,
        target_code_type=body.target_code_type,
    )
    result = await use_case.generate(command)
    return CodeConvertGenerateResponse(result=result)
