from .ai_diagram_router import router
from .erd import router as diagram_erd_router

router.include_router(diagram_erd_router)

__all__ = ["router"]
