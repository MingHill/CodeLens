from __future__ import annotations

import enum
from datetime import datetime
from typing import TYPE_CHECKING, Optional

from sqlalchemy import String, DateTime, Enum, Integer, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base

if TYPE_CHECKING:
    from app.models.chunk import Chunk


class RepositoryStatus(enum.Enum):
    """Processing status for a repository."""
    PENDING = "pending"
    PROCESSING = "processing"
    READY = "ready"
    FAILED = "failed"


class Repository(Base):
    """A code repository uploaded by a user."""
    
    __tablename__ = "repositories"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    status: Mapped[RepositoryStatus] = mapped_column(
        Enum(RepositoryStatus), 
        default=RepositoryStatus.PENDING
    )
    file_count: Mapped[int] = mapped_column(Integer, default=0)
    error_message: Mapped[Optional[str]] = mapped_column(String(1000), nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, 
        server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now()
    )
    
    # Relationship to chunks (defined in Chunk model)
    chunks: Mapped[list[Chunk]] = relationship(back_populates="repository")
