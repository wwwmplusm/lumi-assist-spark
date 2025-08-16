"""Service layer for assignment-related business logic."""

from sqlalchemy.orm import Session
from fastapi import HTTPException
from .. import models, schemas


def create_assignment(
    db: Session, request: schemas.AssignmentCreateRequest, teacher_id: str
) -> models.Assignment:
    """Create and persist a new assignment.

    Args:
        db: Database session.
        request: Validated assignment creation data.
        teacher_id: Identifier of the teacher creating the assignment.

    Returns:
        The newly created Assignment instance.
    """

    new_assignment = models.Assignment(title=request.title, teacher_id=teacher_id)
    db.add(new_assignment)
    db.commit()
    db.refresh(new_assignment)
    return new_assignment


def update_assignment(
    db: Session,
    assignment_id: str,
    teacher_id: str,
    request: schemas.AssignmentUpdateRequest,
) -> models.Assignment | None:
    """Updates an assignment's title and canvas content."""

    assignment = (
        db.query(models.Assignment)
        .filter(
            models.Assignment.id == assignment_id,
            models.Assignment.teacher_id == teacher_id,
        )
        .first()
    )
    if assignment:
        assignment.title = request.title
        assignment.canvas_json = request.canvas_json
        db.commit()
        db.refresh(assignment)
    return assignment


def publish_assignment(
    db: Session,
    assignment_id: str,
    teacher_id: str,
    request: schemas.AssignmentPublishRequest,
) -> list[models.Submission] | None:
    """Publishes an assignment to a list of students."""

    assignment = (
        db.query(models.Assignment)
        .filter(
            models.Assignment.id == assignment_id,
            models.Assignment.teacher_id == teacher_id,
        )
        .first()
    )
    if not assignment:
        return None

    students = (
        db.query(models.Student)
        .filter(
            models.Student.id.in_(request.student_ids),
            models.Student.teacher_id == teacher_id,
        )
        .all()
    )

    if len(students) != len(request.student_ids):
        raise HTTPException(
            status_code=400,
            detail=(
                "One or more student IDs are invalid or do not belong to this teacher."
            ),
        )

    submissions: list[models.Submission] = []
    for student in students:
        submissions.append(
            models.Submission(assignment_id=assignment.id, student_id=student.id)
        )

    db.add_all(submissions)
    assignment.status = models.AssignmentStatus.PUBLISHED
    assignment.deadline = request.deadline
    db.commit()

    for sub in submissions:
        db.refresh(sub)

    return submissions
