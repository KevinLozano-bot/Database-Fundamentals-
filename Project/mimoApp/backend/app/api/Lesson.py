from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from schemas.lesson import LessonCreate
from services.Lesson_services import add_lesson, list_lesson, update_lesson, delete_lesson
from models.user import User

router = APIRouter()

@router.post("/")
def create_lesson(lesson: LessonCreate, db: Session = Depends(get_db)):
    lesson = list_lesson(db, lesson)
    if lesson:
        raise HTTPException(status_code=400, detail="Lesson already exists")
    return add_lesson(db, lesson)

@router.get("/")
def get_all_lessons(db: Session = Depends(get_db)):
    return list_lesson(db)

@router.get("/{id}")
def get_lesson(id: int, db: Session = Depends(get_db)):
    lesson = list_lesson(db, id)
    if lesson is None:
        raise HTTPException(status_code=404, detail="Lesson not found")
    return lesson

@router.put("/{id}")
def modify_lesson(id: int, lesson: LessonCreate, db: Session = Depends(get_db)):
    return update_lesson(db, id, lesson)

@router.delete("/{id}")
def remove_lesson(id: int, db: Session = Depends(get_db)):
    return delete_lesson(db, id)

