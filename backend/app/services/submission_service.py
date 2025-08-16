"""Service layer for submission-related logic."""

from datetime import datetime
from fastapi import BackgroundTasks, HTTPException
from sqlalchemy.orm import Session, joinedload

from .. import models, schemas
from . import ai_service


def get_submission_for_student(db: Session, access_token: str) -> models.Submission | None:
    """Fetch a submission using the student's unique access token."""

    return (
        db.query(models.Submission)
        .options(joinedload(models.Submission.assignment))
        .filter(models.Submission.access_token == access_token)
        .first()
    )


def submit_answers(
    db: Session,
    submission: models.Submission,
    answers: schemas.StudentSubmissionRequest,
    background_tasks: BackgroundTasks,
) -> models.Submission:
    """Save student answers and trigger AI grading in the background."""

    if submission.status != models.SubmissionStatus.PENDING:
        raise HTTPException(status_code=400, detail="Submission has already been made.")

    submission.answers_json = answers.answers
    submission.status = models.SubmissionStatus.SUBMITTED
    submission.submitted_at = datetime.utcnow()
    db.commit()

    background_tasks.add_task(grade_submission_by_ai, db, submission.id)

    db.refresh(submission)
    return submission


def grade_submission_by_ai(db: Session, submission_id: str) -> None:
    """Placeholder for slow AI grading logic."""

    submission = db.query(models.Submission).get(submission_id)
    if not submission:
        return

    simulated_feedback = ai_service.evaluate_open_answer_stub(
        "prompt", "correct", "student answer"
    )

    submission.ai_score = simulated_feedback["score"]
    submission.ai_feedback_json = simulated_feedback["feedback"]
    db.commit()


def get_submission_for_teacher(
    db: Session, submission_id: str, teacher_id: str
) -> models.Submission | None:
    """Fetch a submission for teacher review."""

    return (
        db.query(models.Submission)
        .join(models.Assignment)
        .filter(
            models.Submission.id == submission_id,
            models.Assignment.teacher_id == teacher_id,
        )
        .first()
    )


def finalize_grade(
    db: Session, submission: models.Submission, grade_data: schemas.FinalGradeRequest
) -> models.Submission:
    """Apply the teacher's final grade and feedback to a submission."""

    if submission.status == models.SubmissionStatus.PENDING:
        raise HTTPException(
            status_code=400,
            detail="Cannot grade a submission that has not been submitted.",
        )

    submission.final_score = grade_data.final_score
    submission.final_feedback = grade_data.final_feedback
    submission.status = models.SubmissionStatus.GRADED
    submission.graded_at = datetime.utcnow()
    db.commit()
    db.refresh(submission)
    return submission


def get_all_submissions_for_student(db: Session, student_id: str) -> list[models.Submission]:
    """Fetch all submissions along with assignments for a student."""

    return (
        db.query(models.Submission)
        .options(joinedload(models.Submission.assignment))
        .filter(models.Submission.student_id == student_id)
        .all()
    )

