from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Response, Body
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from app.application.port.inbound.auth import (
    LoginCommand,
    LoginUseCase,
    SignupCommand,
    SignupUseCase,
)
from app.configurator import Container
from .signup_request import SignupRequest
from .signup_response import SignupResponse
from .login_response import LoginResponse

ACCESS_TOKEN_MAX_AGE = 60 * 60 * 24 * 1
REFRESH_TOKEN_MAX_AGE = 60 * 60 * 24 * 7

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    dependencies=[],
    responses={404: {"description": "찾을 수 없습니다."}},
)


@router.post("/login")
@inject
async def login(
    response: Response,
    request: OAuth2PasswordRequestForm = Depends(),
    use_case: LoginUseCase = Depends(Provide[Container.auth_service]),
) -> LoginResponse:
    try:
        command = LoginCommand(email=request.username, password=request.password)
        jwt_token = await use_case.login(command)
        response.set_cookie(
            key="accessToken",
            value=jwt_token.access_token,
            max_age=ACCESS_TOKEN_MAX_AGE,
        )
        response.set_cookie(
            key="refreshToken",
            value=jwt_token.refresh_token,
            # httponly=True,
            max_age=REFRESH_TOKEN_MAX_AGE,
        )
        return LoginResponse(
            access_token=jwt_token.access_token, refresh_token=jwt_token.refresh_token
        )

    except HTTPException as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/signup")
@inject
async def sign_up(
    response: Response,
    request: SignupRequest = Body(...),
    use_case: SignupUseCase = Depends(Provide[Container.auth_service]),
) -> SignupResponse:
    command = SignupCommand(
        email=request.email, password=request.password, username=request.username
    )
    return await use_case.signup(command)
