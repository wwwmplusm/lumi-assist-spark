"""Service layer for assignment-related business logic."""

from sqlalchemy.orm import Session
from .. import models, schemas


def create_assignment(db: Session, request: schemas.AssignmentCreateRequest) -> models.Assignment:
    """Create and persist a new assignment.

    Args:
        db: Database session.
        request: Validated assignment creation data.

    Returns:
        The newly created Assignment instance.
    """

    new_assignment = models.Assignment(title=request.title)
    db.add(new_assignment)
    db.commit()
    db.refresh(new_assignment)
    return new_assignment
