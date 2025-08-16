"""API routes for teacher-related operations."""

from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas
from ..services import assignment_service, teacher_service
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
