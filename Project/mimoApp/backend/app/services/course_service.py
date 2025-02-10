from sqlalchemy.orm import Session
from backend.app.repositories.course_repo import create_course, get_all_courses
from backend.schemas.course import CourseCreate

def add_course(db: Session, course: CourseCreate):
    return create_course(db, course)

def list_course(db: Session):
    return get_all_courses(db)