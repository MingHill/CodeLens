from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Optional

from sqlalchemy import String, Integer, Text, DateTime, ForeignKey, Index, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from pgvector.sqlalchemy import Vector

from app.core.database import Base
from app.core.config import settings

if TYPE_CHECKING:
    from app.models.repository import Repository


class Chunk(Base):
    """A chunk of source code from a repository."""
    
    __tablename__ = "chunks"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    repository_id: Mapped[int] = mapped_column(ForeignKey("repositories.id"))
    
    # Location in the source file
    file_path: Mapped[str] = mapped_column(String(500))
    start_line: Mapped[int] = mapped_column(Integer)
    end_line: Mapped[int] = mapped_column(Integer)
    
    # The actual code content
    content: Mapped[str] = mapped_column(Text)
    
    # Programming language (e.g., "python", "javascript")
    language: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    
    # Vector embedding for similarity search
    embedding: Mapped[list[float]] = mapped_column(
        Vector(settings.embedding_dimensions)
    )
    
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now()
    )
    
    # Relationship back to repository
    repository: Mapped[Repository] = relationship(back_populates="chunks")
    
    __table_args__ = (
        Index(
            "ix_chunks_embedding",
            embedding,
            postgresql_using="ivfflat",
            postgresql_with={"lists": 100},
            postgresql_ops={"embedding": "vector_cosine_ops"}
        ),
    )
