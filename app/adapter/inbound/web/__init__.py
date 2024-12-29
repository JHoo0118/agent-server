from fastapi import APIRouter

from app.adapter.inbound.web.ai import router as aiRouter
from app.adapter.inbound.web.auth import router as authRouter

api = APIRouter()
api.include_router(authRouter)
api.include_router(aiRouter)

__all__ = ["api"]
