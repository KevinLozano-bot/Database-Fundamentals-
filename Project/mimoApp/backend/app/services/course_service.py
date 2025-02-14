from sqlalchemy.orm import Session
from repositories.course_repo import create_course, get_all_courses
from schemas.course import CourseCreate

def add_course(db: Session, course: CourseCreate):
    """
    Service function to add a new course.

    This function interacts with the repository layer to create a new course 
    using the provided CourseCreate schema.

    Args:
        db (Session): The database session for database operations.
        course (CourseCreate): The data required to create a new course.

    Returns:
        Course: The newly created course object.
    """
    return create_course(db, course)

def list_course(db: Session):
    """
    Service function to list all courses.

    This function interacts with the repository layer to retrieve all courses 
    from the database.

    Args:
        db (Session): The database session for database operations.

    Returns:
        List[Course]: A list of all course objects.
    """
    return get_all_courses(db)
