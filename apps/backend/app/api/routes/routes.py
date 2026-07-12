from fastapi import APIRouter
from app.api.routes.demo.demo import demo_router
from app.api.routes.auth.register import user_Reg_Router
router = APIRouter()
router.include_router(
    demo_router,
    prefix="/demo",
)
router.include_router(
    user_Reg_Router,
    prefix="/auth", 
)