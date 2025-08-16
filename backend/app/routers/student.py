"""API routes for student-facing operations."""

from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import models, schemas
from ..services import submission_service
from ..db import get_db

router = APIRouter(prefix="/api/s", tags=["Student"])


@router.get("/{access_token}", response_model=schemas.StudentAssignmentView)
def handle_get_assignment_for_student(
    access_token: str, db: Session = Depends(get_db)
):
    """Fetch an assignment for a student to complete."""

    submission = submission_service.get_submission_for_student(db, access_token)
    if not submission or submission.status != models.SubmissionStatus.PENDING:
        raise HTTPException(
            status_code=404, detail="Assignment not found or already submitted"
        )

    assignment = submission.assignment
    clean_canvas = [
        {k: v for k, v in block.items() if k != "answer"}
        for block in assignment.canvas_json
    ]

    return schemas.StudentAssignmentView(
        assignment_id=assignment.id,
        title=assignment.title,
        deadline=assignment.deadline,
        status=submission.status,
        canvas_json=clean_canvas,
    )


@router.post("/{access_token}/submit")
def handle_submit_answers(
    access_token: str,
    request: schemas.StudentSubmissionRequest,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
):
    """Accept answers from a student."""

    submission = submission_service.get_submission_for_student(db, access_token)
    if not submission:
        raise HTTPException(status_code=404, detail="Invalid submission link")

    submission_service.submit_answers(db, submission, request, background_tasks)
    return {
        "message": "Assignment submitted successfully. Your results will be available soon.",
    }

