from sqlalchemy.orm import Session
from models.lesson import Lesson
from schemas.lesson import LessonCreate

def create_lesson(db: Session, lesson: LessonCreate):
    db_lesson = Lesson(title=lesson.title, description=lesson.description, course_id=lesson.course_id)
    db.add(db_lesson)
    db.commit()
    db.refresh(db_lesson)
    return db_lesson

def delete_lesson(db: Session, lesson_id: int):
    db_lesson = db.query(Lesson).filter(Lesson.id == lesson_id).first()
    db.delete(db_lesson)
    db.commit()
    return db_lesson

def get_all_lessons(db: Session):
    return db.query(Lesson).all()

def get_lesson_by_id(db: Session, lesson_id: int):
    return db.query(Lesson).filter(Lesson.id == lesson_id).first()

def get_lessons_by_course_id(db: Session, course_id: int):
    return db.query(Lesson).filter(Lesson.course_id == course_id).all()

def update_lesson(db: Session, lesson_id: int, lesson: LessonCreate):
    db_lesson = db.query(Lesson).filter(Lesson.id == lesson_id).first()
    db_lesson.title = lesson.title
    db_lesson.description = lesson.description
    db.commit()
    db.refresh(db_lesson)
    return db_lesson

def get_lesson_by_title(db: Session, title: str):
    return db.query(Lesson).filter(Lesson.title == title).first()
