from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.session import get_db
from schemas.course import CourseCreate
from services.course_service import add_course, list_course

# Create an instance of a router to handle course-related routes
router = APIRouter()

@router.post("/")
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    """
    Creates a new course in the system.

    This endpoint allows you to create a new course by providing the necessary 
    course data in the request body. Once the course is successfully added, 
    the details of the created course are returned.

    Parameters:
        - course (CourseCreate): The course data to be created.
        - db (Session): Database session provided by `get_db`.

    Returns:
        - dict: The details of the newly created course.

    Example response:
        {"id": 1, "name": "Course Name", "description": "Course Description"}
    """
    # Calls the service to add the course to the database
    return add_course(db, course)

@router.get("/")
def get_Course(db: Session = Depends(get_db)):
    """
    Retrieves the list of all courses.

    This endpoint returns a list of all courses present in the system. 
    The courses will be retrieved from the database.

    Parameters:
        - db (Session): Database session provided by `get_db`.

    Returns:
        - list: A list of all courses in the system.

    Example response:
        [
            {"id": 1, "name": "Course 1", "description": "Description of Course 1"},
            {"id": 2, "name": "Course 2", "description": "Description of Course 2"}
        ]
    """
    # Calls the service to list all courses from the database
    return list_course(db)
