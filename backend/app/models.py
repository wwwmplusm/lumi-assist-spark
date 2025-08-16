import enum
import uuid
from datetime import datetime
from sqlalchemy import (Column, String, JSON, Enum as SQLEnum, DateTime,
                        ForeignKey, Text, Float, Boolean)
from sqlalchemy.orm import relationship
from .db import Base


def uid():
    return str(uuid.uuid4())


class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(String, primary_key=True, default=uid)
    email = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    students = relationship("Student", back_populates="teacher", cascade="all, delete-orphan")
    materials = relationship("Material", back_populates="teacher", cascade="all, delete-orphan")
    assignments = relationship("Assignment", back_populates="teacher", cascade="all, delete-orphan")


class Student(Base):
    __tablename__ = "students"
    id = Column(String, primary_key=True, default=uid)
    teacher_id = Column(String, ForeignKey("teachers.id"), nullable=False)
    name = Column(String, nullable=False)
    email = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    teacher = relationship("Teacher", back_populates="students")
    submissions = relationship("Submission", back_populates="student", cascade="all, delete-orphan")


class Material(Base):
    __tablename__ = "materials"
    id = Column(String, primary_key=True, default=uid)
    teacher_id = Column(String, ForeignKey("teachers.id"), nullable=False)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    teacher = relationship("Teacher", back_populates="materials")


class AssignmentStatus(str, enum.Enum):
    DRAFT = "draft"
    PUBLISHED = "published"


class Assignment(Base):
    __tablename__ = "assignments"
    id = Column(String, primary_key=True, default=uid)
    teacher_id = Column(String, ForeignKey("teachers.id"), nullable=False)
    title = Column(String, nullable=False)
    status = Column(SQLEnum(AssignmentStatus), default=AssignmentStatus.DRAFT, nullable=False)
    canvas_json = Column(JSON, default=list, nullable=False)
    deadline = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    teacher = relationship("Teacher", back_populates="assignments")
    submissions = relationship("Submission", back_populates="assignment", cascade="all, delete-orphan")


class SubmissionStatus(str, enum.Enum):
    PENDING = "pending"
    SUBMITTED = "submitted"
    GRADED = "graded"


class Submission(Base):
    __tablename__ = "submissions"
    id = Column(String, primary_key=True, default=uid)
    assignment_id = Column(String, ForeignKey("assignments.id"), nullable=False)
    student_id = Column(String, ForeignKey("students.id"), nullable=False)
    status = Column(SQLEnum(SubmissionStatus), default=SubmissionStatus.PENDING, nullable=False)
    access_token = Column(String, unique=True, default=uid, nullable=False)
    answers_json = Column(JSON, nullable=True)
    ai_score = Column(Float, nullable=True)
    ai_feedback_json = Column(JSON, nullable=True)
    final_score = Column(Float, nullable=True)
    final_feedback = Column(Text, nullable=True)
    submitted_at = Column(DateTime, nullable=True)
    graded_at = Column(DateTime, nullable=True)

    assignment = relationship("Assignment", back_populates="submissions")
    student = relationship("Student", back_populates="submissions")
