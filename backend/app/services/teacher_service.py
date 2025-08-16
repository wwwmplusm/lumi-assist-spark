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
