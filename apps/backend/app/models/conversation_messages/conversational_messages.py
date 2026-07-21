from app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String
import uuid

class ConversationalMessages(Base):
    __tablename__ = "ConversationalMessages"
    Id: Mapped[str] = mapped_column(String,primary_key = True,default =uuid.uuid4)
    DocId:Mapped[str] = mapped_column(String(50),nullable=False)
    UserId:Mapped[str] = mapped_column(String(50),nullable=False)
    Message:Mapped[str] = mapped_column(String,nullable=False)
    Response:Mapped[str] = mapped_column(String,nullable=True)
    CreatedAt:Mapped[str] = mapped_column(String,nullable=True)