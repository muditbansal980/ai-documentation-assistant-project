from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Integer, String
from app.db.base import Base
import uuid
class User(Base):
    __tablename__ = "User"

    Id:Mapped[str] = mapped_column(String,primary_key=True, default=uuid.uuid4)
    Username:Mapped[str] = mapped_column(String(50),nullable=False,unique=True)
    Email:Mapped[str] = mapped_column(String(100),nullable=False,unique=True)
    Password:Mapped[str] = mapped_column(String(100),nullable=True)
class UserLogin(Base):
    __tablename__ = "User"
    