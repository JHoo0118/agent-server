from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from .jwt_bearer import JwtBearer
from app.application.service.user import UserService
from app.configurator.containers import Container


class JwtMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI):
        super().__init__(app)
        self.jwt_bearer = JwtBearer()
        self.user_service: UserService = Container.user_service

    async def dispatch(self, request: Request, call_next):
        try:
            if request.url.path.startswith(
                "/api/ai"
            ) and not request.url.path.startswith("/api/ai/docs/summary"):
                email: str = await self.jwt_bearer(request)
                request.state.email = email
            # await self.userService.recalculate_remain_count(email)
            response = await call_next(request)
            return response
        except Exception as e:
            return JSONResponse(
                status_code=400,
                content={"detail": str(e.detail if hasattr(e, "detail") else e)},
            )
