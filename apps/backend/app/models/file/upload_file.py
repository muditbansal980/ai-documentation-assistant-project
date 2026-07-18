from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Integer, String
from app.db.base import Base
import uuid
class Document(Base):
    __tablename__ = "Document"

    Id:Mapped[str] = mapped_column(String,primary_key=True, default=uuid.uuid4)
    UserId:Mapped[str] = mapped_column(String(50),nullable=False)
    OriginalFileName:Mapped[str] = mapped_column(String(100),nullable=False)
    StoragePath:Mapped[str] = mapped_column(String(200),nullable=False)
    MimeType:Mapped[str] = mapped_column(String(50),nullable=False)
    FileSize:Mapped[int] = mapped_column(Integer,nullable=False)
    Status:Mapped[str] = mapped_column(String(20),nullable=False)
    