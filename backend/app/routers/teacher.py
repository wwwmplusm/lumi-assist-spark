"""API routes for teacher-related operations."""

from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas
from ..services import assignment_service, teacher_service, submission_service
from ..db import get_db
from ..security import get_current_teacher

router = APIRouter(prefix="/api/teacher", tags=["Teacher"])


@router.post("/assignments", response_model=schemas.AssignmentResponse, status_code=201)
def handle_create_assignment(
    request: schemas.AssignmentCreateRequest,
    db: Session = Depends(get_db),
    teacher: models.Teacher = Depends(get_current_teacher),
) -> schemas.AssignmentResponse:
    """Handle the creation of a new assignment."""

    assignment = assignment_service.create_assignment(
        db=db, request=request, teacher_id=teacher.id
    )
    return schemas.AssignmentResponse(
        assignment_id=assignment.id,
        title=assignment.title,
        status=assignment.status,
        canvas_json=assignment.canvas_json,
    )


@router.put("/assignments/{assignment_id}", response_model=schemas.AssignmentResponse)
def handle_update_assignment(
    assignment_id: str,
    request: schemas.AssignmentUpdateRequest,
    db: Session = Depends(get_db),
    teacher: models.Teacher = Depends(get_current_teacher),
):
    """Handle updating an assignment's canvas and title."""

    updated_assignment = assignment_service.update_assignment(
        db, assignment_id=assignment_id, teacher_id=teacher.id, request=request
    )
    if not updated_assignment:
        raise HTTPException(status_code=404, detail="Assignment not found or access denied")

    return schemas.AssignmentResponse.from_orm(updated_assignment)


@router.post(
    "/assignments/{assignment_id}/publish", response_model=List[schemas.PublishedLink]
)
def handle_publish_assignment(
    assignment_id: str,
    request: schemas.AssignmentPublishRequest,
    db: Session = Depends(get_db),
    teacher: models.Teacher = Depends(get_current_teacher),
):
    """Publish an assignment and return unique links for students."""

    submissions = assignment_service.publish_assignment(
        db, assignment_id=assignment_id, teacher_id=teacher.id, request=request
    )
    if not submissions:
        raise HTTPException(status_code=404, detail="Assignment not found")

    base_url = "http://localhost:8080"
    links = [
        schemas.PublishedLink(
            student_name=sub.student.name, link=f"{base_url}/s/{sub.access_token}"
        )
        for sub in submissions
    ]
    return links


@router.get("/students", response_model=List[schemas.Student])
def handle_get_students(
    db: Session = Depends(get_db),
    teacher: models.Teacher = Depends(get_current_teacher),
):
    return teacher_service.get_students_for_teacher(db, teacher_id=teacher.id)


@router.post("/students", response_model=schemas.Student, status_code=201)
def handle_create_student(
    student_data: schemas.StudentCreate,
    db: Session = Depends(get_db),
    teacher: models.Teacher = Depends(get_current_teacher),
):
    return teacher_service.create_student_for_teacher(
        db, teacher_id=teacher.id, student_data=student_data
    )


@router.get("/materials", response_model=List[schemas.Material])
def handle_get_materials(
    db: Session = Depends(get_db),
    teacher: models.Teacher = Depends(get_current_teacher),
):
    return teacher_service.get_materials_for_teacher(db, teacher_id=teacher.id)


@router.post("/materials", response_model=schemas.MaterialDetail, status_code=201)
def handle_create_material(
    material_data: schemas.MaterialCreate,
    db: Session = Depends(get_db),
    teacher: models.Teacher = Depends(get_current_teacher),
):
    return teacher_service.create_material_for_teacher(
        db, teacher_id=teacher.id, material_data=material_data
    )


@router.get(
    "/submissions/{submission_id}", response_model=schemas.TeacherSubmissionView
)
def handle_get_submission_for_review(
    submission_id: str,
    db: Session = Depends(get_db),
    teacher: models.Teacher = Depends(get_current_teacher),
):
    """Retrieve a student's submission for teacher review."""

    submission = submission_service.get_submission_for_teacher(
        db, submission_id, teacher.id
    )
    if not submission:
        raise HTTPException(status_code=404, detail="Submission not found")

    return schemas.TeacherSubmissionView(
        student_name=submission.student.name,
        submitted_at=submission.submitted_at,
        answers=submission.answers_json,
        ai_score=submission.ai_score,
        ai_feedback=submission.ai_feedback_json,
        final_score=submission.final_score,
        final_feedback=submission.final_feedback,
    )
