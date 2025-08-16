from sqlalchemy.orm import Session

from app.services import teacher_service
from app.schemas import StudentCreate, MaterialCreate
from app.models import Teacher


def test_create_student_for_teacher(db_session: Session, test_teacher: Teacher) -> None:
    """Ensure a student can be created for a teacher."""

    student_data = StudentCreate(name="John Doe", email="john.doe@example.com")

    student = teacher_service.create_student_for_teacher(
        db=db_session, teacher_id=test_teacher.id, student_data=student_data
    )

    assert student is not None
    assert student.name == "John Doe"
    assert student.email == "john.doe@example.com"
    assert student.teacher_id == test_teacher.id
    assert student.id is not None


def test_get_students_for_teacher(db_session: Session, test_teacher: Teacher) -> None:
    """Retrieve all students for a given teacher."""

    teacher_service.create_student_for_teacher(
        db=db_session,
        teacher_id=test_teacher.id,
        student_data=StudentCreate(name="Student 1"),
    )
    teacher_service.create_student_for_teacher(
        db=db_session,
        teacher_id=test_teacher.id,
        student_data=StudentCreate(name="Student 2"),
    )

    students = teacher_service.get_students_for_teacher(
        db=db_session, teacher_id=test_teacher.id
    )

    assert len(students) == 2
    assert students[0].name == "Student 1"


def test_create_material_for_teacher(db_session: Session, test_teacher: Teacher) -> None:
    """Ensure a material can be created for a teacher."""

    material_data = MaterialCreate(
        title="Lesson 1", content="This is the content of lesson 1"
    )

    material = teacher_service.create_material_for_teacher(
        db=db_session, teacher_id=test_teacher.id, material_data=material_data
    )

    assert material is not None
    assert material.title == "Lesson 1"
    assert material.content == "This is the content of lesson 1"
    assert material.teacher_id == test_teacher.id
    assert material.id is not None


def test_get_materials_for_teacher(db_session: Session, test_teacher: Teacher) -> None:
    """Retrieve all materials for a given teacher."""

    teacher_service.create_material_for_teacher(
        db=db_session,
        teacher_id=test_teacher.id,
        material_data=MaterialCreate(
            title="Material 1", content="Content 1234567890"
        ),
    )
    teacher_service.create_material_for_teacher(
        db=db_session,
        teacher_id=test_teacher.id,
        material_data=MaterialCreate(
            title="Material 2", content="Another content 123456"
        ),
    )

    materials = teacher_service.get_materials_for_teacher(
        db=db_session, teacher_id=test_teacher.id
    )

    assert len(materials) == 2
    assert materials[0].title == "Material 1"

