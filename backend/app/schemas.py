from pydantic import BaseModel, Field, EmailStr
from typing import Any, List, Dict
from datetime import datetime
from .models import AssignmentStatus, SubmissionStatus


# --- Base Schemas for Models ---
class Student(BaseModel):
    id: str
    name: str
    email: EmailStr | None = None

    class Config:
        from_attributes = True


class Teacher(BaseModel):
    id: str
    email: EmailStr
    name: str | None = None

    class Config:
        from_attributes = True


class Material(BaseModel):
    id: str
    title: str
    description: str | None = None
    created_at: datetime

    class Config:
        from_attributes = True


# --- Authentication Schemas ---
class TeacherCreate(BaseModel):
    email: EmailStr
    name: str | None = None


# --- Student Management Schemas ---
class StudentCreate(BaseModel):
    name: str = Field(..., min_length=1)
    email: EmailStr | None = None


# --- Material Management Schemas ---
class MaterialCreate(BaseModel):
    title: str = Field(..., min_length=1)
    content: str = Field(..., min_length=10)
    description: str | None = None


class MaterialDetail(Material):
    content: str


# --- Assignment Schemas ---
class AssignmentCreateRequest(BaseModel):
    title: str = Field("Новое задание", min_length=1, max_length=100)


class AssignmentUpdateRequest(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    canvas_json: List[Dict[str, Any]]


class AssignmentPublishRequest(BaseModel):
    student_ids: List[str]
    deadline: datetime | None = None


class AssignmentResponse(BaseModel):
    assignment_id: str
    title: str
    status: AssignmentStatus
    canvas_json: List[Dict[str, Any]]

    class Config:
        from_attributes = True


class PublishedLink(BaseModel):
    student_name: str
    link: str  # This will be constructed in the service


# --- Submission Schemas (for Student) ---
class StudentAssignmentView(BaseModel):
    assignment_id: str
    title: str
    deadline: datetime | None = None
    status: SubmissionStatus
    canvas_json: List[Dict[str, Any]]


class StudentSubmissionRequest(BaseModel):
    answers: Dict[str, Any]


class TeacherSubmissionView(BaseModel):
    student_name: str
    submitted_at: datetime | None = None
    answers: Dict[str, Any]
    ai_score: float | None = None
    ai_feedback: Dict[str, Any] | None = None
    final_score: float | None = None
    final_feedback: str | None = None


# --- AI Schemas ---
class AIGenerateRequest(BaseModel):
    source_text: str = Field(..., min_length=20)
    prompt: str | None = "Generate 3 diverse questions"


class AIGenerateResponse(BaseModel):
    blocks: List[Dict[str, Any]]
