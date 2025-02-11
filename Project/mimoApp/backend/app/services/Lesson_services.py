from sqlalchemy.orm import Session
from repositories.Lesson_repo import create_lesson, get_all_lessons
from schemas.Lesson import LessonCreate

def add_lesson(db: Session, lesson: LessonCreate):
    return create_lesson(db, lesson)

def list_lesson(db: Session):
    return get_all_lessons(db)

def update_lesson(db: Session, id: int, lesson: LessonCreate):
    return update_lesson(db, id, lesson)

def delete_lesson(db: Session, id: int):
    return delete_lesson(db, id)