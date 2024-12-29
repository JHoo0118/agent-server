from .ai_api import router
from .algorithm_advice import router as algorithm_advice_router
from .code_convert import router as code_convert_router

router.include_router(code_convert_router)
router.include_router(algorithm_advice_router)

__all__ = ["router"]
