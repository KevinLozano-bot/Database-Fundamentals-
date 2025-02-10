from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.app.db.session import get_db
from backend.schemas.course import CourseCreate
from backend.app.services.course_service import add_course, list_course

router = APIRouter()

@router.post("/")
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    return add_course(db, course)

@router.get("/")
def get_Course(db: Session = Depends(get_db)):
    return list_course(db)
