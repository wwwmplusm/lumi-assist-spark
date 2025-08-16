from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import schemas
from ..services import auth_service
from ..db import get_db

router = APIRouter(prefix="/api/auth", tags=["Auth"])


@router.post("/register", response_model=schemas.Teacher, status_code=201)
def handle_register_teacher(
    teacher_data: schemas.TeacherCreate, db: Session = Depends(get_db)
):
    """Register a new teacher and simulate sending a login link."""
    return auth_service.register_teacher(db, teacher_data)
