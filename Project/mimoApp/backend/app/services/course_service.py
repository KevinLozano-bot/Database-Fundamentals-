from sqlalchemy.orm import Session
from repositories.course_repo import (
    create_course, 
    get_all_courses, 
    get_course_by_id, 
    update_course, 
    delete_course
)
from schemas.course import CourseCreate, CourseUpdate
from models.course import Course

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

def list_courses(db: Session):
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

def get_course(db: Session, course_id: int):
    """
    Service function to get a course by its ID.

    This function interacts with the repository layer to retrieve a specific 
    course by its ID.

    Args:
        db (Session): The database session for database operations.
        course_id (int): The ID of the course to retrieve.

    Returns:
        Course: The course object corresponding to the given ID, or None if not found.
    """
    return get_course_by_id(db, course_id)

def update_course_details(db: Session, course_id: int, course: CourseUpdate):
    """
    Service function to update a course's details.

    This function interacts with the repository layer to update the details of 
    an existing course.

    Args:
        db (Session): The database session for database operations.
        course_id (int): The ID of the course to update.
        course (CourseUpdate): The updated data for the course.

    Returns:
        Course: The updated course object, or None if not found.
    """
    return update_course(db, course_id, course)

def remove_course(db: Session, course_id: int):
    """
    Service function to delete a course by its ID.

    This function interacts with the repository layer to delete a course from 
    the database.

    Args:
        db (Session): The database session for database operations.
        course_id (int): The ID of the course to delete.

    Returns:
        Course: The deleted course object, or None if not found.
    """
    return delete_course(db, course_id)

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
