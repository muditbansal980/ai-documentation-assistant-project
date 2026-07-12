from fastapi import APIRouter
import uuid
from sqlalchemy import text
from app.db.session import AsyncSessionLocal
from app.models.users.user import User
from app.api.controllers.auth.register import register_user

user_Reg_Router = APIRouter()

user_Reg_Router.post(
    "/register",
    tags=["Register"]
)(register_user)

user_Reg_Router.post(
    "/login",
    tags=["Login"]
)