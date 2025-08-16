"""Service layer for teacher-related operations."""

from sqlalchemy import case, func
from sqlalchemy.orm import Session

from .. import models, schemas


def create_student_for_teacher(db: Session, teacher_id: str, student_data: schemas.StudentCreate) -> models.Student:
    student = models.Student(**student_data.dict(), teacher_id=teacher_id)
    db.add(student)
    db.commit()
    db.refresh(student)
    return student


def get_students_for_teacher(db: Session, teacher_id: str) -> list[models.Student]:
    return db.query(models.Student).filter(models.Student.teacher_id == teacher_id).all()


def create_material_for_teacher(db: Session, teacher_id: str, material_data: schemas.MaterialCreate) -> models.Material:
    material = models.Material(**material_data.dict(), teacher_id=teacher_id)
    db.add(material)
    db.commit()
    db.refresh(material)
    return material


def get_materials_for_teacher(db: Session, teacher_id: str) -> list[models.Material]:
    return db.query(models.Material).filter(models.Material.teacher_id == teacher_id).all()


def get_dashboard_data(db: Session, teacher_id: str) -> list[dict]:
    """Aggregate dashboard statistics for all students of a teacher."""

    stmt = (
        db.query(
            models.Student.id,
            models.Student.name,
            func.count(models.Submission.id).label("total_submissions"),
            func.sum(
                case(
                    (models.Submission.status == models.SubmissionStatus.SUBMITTED, 1),
                    else_=0,
                )
            ).label("ungraded_submissions"),
            func.sum(
                case(
                    (models.Submission.status == models.SubmissionStatus.GRADED, 1),
                    else_=0,
                )
            ).label("graded_submissions"),
        )
        .outerjoin(models.Submission, models.Student.id == models.Submission.student_id)
        .filter(models.Student.teacher_id == teacher_id)
        .group_by(models.Student.id)
        .order_by(models.Student.name)
    )

    results = stmt.all()
    dashboard_data = [
        {
            "id": r.id,
            "name": r.name,
            "ungraded_submissions": r.ungraded_submissions or 0,
            "graded_submissions": r.graded_submissions or 0,
        }
        for r in results
    ]
    return dashboard_data
