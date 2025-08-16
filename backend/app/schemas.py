"""Pydantic schemas defining API contracts for the Lumi AI backend."""

from typing import Any, List
from pydantic import BaseModel
from .models import AssignmentStatus


class AssignmentCreateRequest(BaseModel):
    """Schema for creating a new assignment."""

    title: str = "Новое задание"


class AssignmentResponse(BaseModel):
    """Schema representing assignment data returned by the API."""

    assignment_id: str
    title: str
    status: AssignmentStatus
    canvas_json: List[Any]

    class Config:
        """Pydantic configuration."""

        from_attributes = True
