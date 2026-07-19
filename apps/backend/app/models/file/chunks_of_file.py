from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Integer, String
from app.db.base import Base
import uuid
from pgvector.sqlalchemy import Vector 

class DocumentChunks(Base):
    __tablename__ = "DocumentChunks"

    Id: Mapped[str] = mapped_column(String, primary_key=True, default=uuid.uuid4)
    DocumentId: Mapped[str] = mapped_column(String(50), nullable=False)
    PageNumber: Mapped[int] = mapped_column(Integer, nullable=False)
    ChunkNumber: Mapped[int] = mapped_column(Integer, nullable=False)
    ChunkText: Mapped[str] = mapped_column(String, nullable=False)
    Embedding = mapped_column(Vector(384), nullable=True) 