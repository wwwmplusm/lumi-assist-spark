"""Service layer for teacher authentication."""

from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from .. import models, schemas


def register_teacher(db: Session, teacher_data: schemas.TeacherCreate) -> models.Teacher:
    """Create a new teacher in the database and simulate sending a magic link."""
    try:
        teacher = models.Teacher(**teacher_data.model_dump())
        db.add(teacher)
        db.commit()
        db.refresh(teacher)

        # --- STUB for sending magic link ---
        # In a real application, you would generate a temporary token,
        # persist it, and send an email containing the login URL.
        print("--- AUTH SIMULATION ---")
        print(f"Teacher registered with ID: {teacher.id}")
        print("To log in, use this ID in the 'X-Teacher-ID' header.")
        print("-----------------------")

        return teacher
    except IntegrityError as exc:
        db.rollback()
        raise HTTPException(status_code=409, detail="A teacher with this email already exists.") from exc
