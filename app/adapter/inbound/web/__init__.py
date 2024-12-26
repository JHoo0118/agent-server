from fastapi import APIRouter

from app.adapter.inbound.web.auth import router as authRouter

api = APIRouter()
api.include_router(authRouter)

__all__ = ["api"]
