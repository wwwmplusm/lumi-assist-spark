"""Database models for the Lumi AI backend."""

from __future__ import annotations

import enum
import uuid
from sqlalchemy import Column, String, JSON, Enum as SQLEnum
from .db import Base


def uid() -> str:
    """Generate a unique identifier."""
    return str(uuid.uuid4())


class AssignmentStatus(str, enum.Enum):
    """Enumeration of possible assignment statuses."""

    DRAFT = "draft"
    PUBLISHED = "published"


class Assignment(Base):
    """ORM model representing an assignment."""

    __tablename__ = "assignments"

    id: Column[str] = Column(String, primary_key=True, default=uid)
    title: Column[str] = Column(String, nullable=False)
    status: Column[AssignmentStatus] = Column(
        SQLEnum(AssignmentStatus), nullable=False, default=AssignmentStatus.DRAFT
    )
    canvas_json: Column[list] = Column(JSON, nullable=False, default=list)
    # In a real app, you'd have a ForeignKey to a Teacher model
    # teacher_id = Column(String, ForeignKey("teachers.id"))
