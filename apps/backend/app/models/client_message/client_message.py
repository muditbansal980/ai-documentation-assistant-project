from app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String
import uuid
from pgvector.sqlalchemy import Vector
class ClientMessages(Base):
    __tablename__ = "ClientMessages"
    Id: Mapped[str] = mapped_column(String,primary_key = True,default =uuid.uuid4)
    DocId:Mapped[str] = mapped_column(String(50),nullable=False)
    UserId:Mapped[str] = mapped_column(String(50),nullable=False)
    Message:Mapped[str] = mapped_column(String,nullable=False)
    Embeddings = mapped_column(Vector(384),nullable=True)