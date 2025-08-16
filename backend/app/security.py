from fastapi import Header, HTTPException, Depends
from sqlalchemy.orm import Session
from . import models
from .db import get_db


async def get_current_teacher(x_teacher_id: str = Header(...), db: Session = Depends(get_db)) -> models.Teacher:
    if not x_teacher_id:
        raise HTTPException(status_code=401, detail="Teacher ID header is missing")

    teacher = db.query(models.Teacher).filter(models.Teacher.id == x_teacher_id).first()
    if not teacher:
        raise HTTPException(status_code=403, detail="Invalid Teacher ID")
    return teacher


async def get_current_submission(access_token: str, db: Session = Depends(get_db)) -> models.Submission:
    """Retrieve a submission by its access token."""

    submission = (
        db.query(models.Submission)
        .filter(models.Submission.access_token == access_token)
        .first()
    )
    if not submission:
        raise HTTPException(status_code=404, detail="Invalid access token")
    return submission
