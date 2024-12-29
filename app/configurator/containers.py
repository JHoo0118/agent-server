from pathlib import Path

from argon2 import PasswordHasher
from dependency_injector import containers, providers

from app.adapter.outbound.persistence.auth import AuthAdapter, AuthRepository
from app.adapter.outbound.persistence.user import UserAdapter, UserRepository
from app.adapter.outbound.external.openai.code_convert import CodeConvertAdapter
from app.adapter.outbound.persistence.refresh_token import RefreshTokenRepository
from app.application.port.inbound.auth import LoginUseCase, SignupUseCase
from app.application.service.auth import AuthService
from app.application.service.user import UserService
from app.application.service.ai.code_convert import CodeConvertService
from app.configurator.logger import CustomizeLogger
from prisma import Prisma

# from app.application.port.outbound.auth import LoginPort


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        packages=[
            "app.adapter.outbound.persistence",
            "app.adapter.inbound.web",
        ]
    )
    config_path = Path(__file__).parent / "logger/logging_config.json"
    LOGGER = CustomizeLogger.make_logger(config_path)
    password_hasher = providers.Singleton(PasswordHasher)
    prisma = providers.Singleton(Prisma)

    auth_repository = providers.Factory(
        AuthRepository, prisma=prisma, password_hasher=password_hasher
    )
    user_repository = providers.Factory(UserRepository, prisma=prisma)
    refresh_token_repository = providers.Factory(
        RefreshTokenRepository, prisma=prisma, password_hasher=password_hasher
    )
    auth_adapter = providers.Factory(
        AuthAdapter,
        auth_repository=auth_repository,
        user_repository=user_repository,
        refresh_token_repository=refresh_token_repository,
    )

    code_convert_adapter = providers.Factory(
        CodeConvertAdapter,
    )

    user_adapter = providers.Factory(UserAdapter, user_repository=user_repository)

    auth_service = providers.Factory(
        AuthService, login_port=auth_adapter, signup_port=auth_adapter
    )
    user_service = providers.Factory(UserService, get_user_port=user_adapter)
    code_convert_service = providers.Factory(
        CodeConvertService, code_convert_generate_port=code_convert_adapter
    )

    login_use_case = providers.Factory(LoginUseCase, auth_service=auth_service)
    signup_use_case = providers.Factory(SignupUseCase, auth_service=auth_service)
