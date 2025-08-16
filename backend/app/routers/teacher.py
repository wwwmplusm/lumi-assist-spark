"""API routes for teacher-related operations."""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas
from ..services import assignment_service
from ..db import get_db

router = APIRouter(prefix="/api/assignments", tags=["Assignments"])


@router.post("/", response_model=schemas.AssignmentResponse, status_code=201)
def handle_create_assignment(
    request: schemas.AssignmentCreateRequest, db: Session = Depends(get_db)
) -> schemas.AssignmentResponse:
    """Handle the creation of a new assignment."""

    assignment = assignment_service.create_assignment(db=db, request=request)
    return schemas.AssignmentResponse(
        assignment_id=assignment.id,
        title=assignment.title,
        status=assignment.status,
        canvas_json=assignment.canvas_json,
    )
