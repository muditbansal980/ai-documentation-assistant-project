from fastapi import APIRouter
from sqlalchemy import text
from app.db.session import AsyncSessionLocal
demo_router = APIRouter(tags=["Home"])
@demo_router.get(
    "/",
)
async def home():
    return {"hello":"hello world"}

@demo_router.get("/db")
async def db_check():
        async with AsyncSessionLocal() as session:
            result = await session.execute(
                text("SELECT 1")
            )
    
            return {
                "database": result.scalar()
            }