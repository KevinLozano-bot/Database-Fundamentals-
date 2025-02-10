from sqlalchemy.orm import Session
from backend.app.models.course import Course
from backend.schemas.course import CourseCreate

def create_course(db: Session, course: CourseCreate):    
    db_course = Course(title=course.title, description=course.description)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

def get_all_courses(db: Session):
    return db.query(Course).all()