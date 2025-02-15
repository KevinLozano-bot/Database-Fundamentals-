from sqlalchemy.orm import Session
from repositories.Lesson_repo import (
    create_lesson, 
    get_all_lessons, 
    get_lesson_by_id, 
    get_lesson_by_title,
    update_lesson, 
    delete_lesson,
    get_lessons_by_course_id
)
from schemas.Lesson import LessonCreate, LessonUpdate
from models.Lesson import Lesson
from fastapi import HTTPException

def add_lesson(db: Session, lesson: LessonCreate):
    """
    Service function to add a new lesson.

    This function interacts with the repository layer to create a new lesson 
    using the provided LessonCreate schema.

    Args:
        db (Session): The database session for database operations.
        lesson (LessonCreate): The data required to create a new lesson.

    Returns:
        Lesson: The newly created lesson object.
    """
    return create_lesson(db, lesson)

def list_lessons(db: Session):
    """
    Service function to list all lessons.

    This function interacts with the repository layer to retrieve all lessons 
    from the database.

    Args:
        db (Session): The database session for database operations.

    Returns:
        List[Lesson]: A list of all lesson objects.
    """
    return get_all_lessons(db)

def get_lesson(db: Session, lesson_id: int):
    """
    Service function to get a lesson by its ID.

    This function interacts with the repository layer to retrieve a specific 
    lesson by its ID.

    Args:
        db (Session): The database session for database operations.
        lesson_id (int): The ID of the lesson to retrieve.

    Returns:
        Lesson: The lesson object corresponding to the given ID, or None if not found.
    """
    return get_lesson_by_id(db, lesson_id)

def get_lessons_by_course(db: Session, course_id: int):
    """
    Service function to get all lessons for a specific course.

    This function interacts with the repository layer to retrieve all lessons 
    associated with a specific course ID.

    Args:
        db (Session): The database session for database operations.
        course_id (int): The ID of the course to retrieve lessons for.

    Returns:
        List[Lesson]: A list of lesson objects for the specified course.
    """
    return get_lessons_by_course_id(db, course_id)

def update_lesson_details(db: Session, lesson_id: int, lesson: LessonUpdate):
    """
    Service function to update a lesson's details.

    This function interacts with the repository layer to update the details of 
    an existing lesson.

    Args:
        db (Session): The database session for database operations.
        lesson_id (int): The ID of the lesson to update.
        lesson (LessonUpdate): The updated data for the lesson.

    Returns:
        Lesson: The updated lesson object, or None if not found.
    """
    return update_lesson(db, lesson_id, lesson)

def remove_lesson(db: Session, lesson_id: int):
    """
    Service function to delete a lesson by its ID.

    This function interacts with the repository layer to delete a lesson from 
    the database.

    Args:
        db (Session): The database session for database operations.
        lesson_id (int): The ID of the lesson to delete.

    Returns:
        dict: A message indicating whether the lesson was deleted or not found.
    """
    return delete_lesson(db, lesson_id)

def get_lesson_by_title(db: Session, title: str):
    """
    Service function to get a lesson by its title.

    This function interacts with the repository layer to retrieve a lesson by 
    its title.

    Args:
        db (Session): The database session for database operations.
        title (str): The title of the lesson to retrieve.

    Returns:
        Lesson: The lesson object corresponding to the given title, or None if not found.
    """
    return get_lesson_by_title(db, title)

def list_lesson(db:Session):
    """
    Service function to list all lessons.

    This function interacts with the repository layer to retrieve all lessons 
    from the database.

    Args:
        db (Session): The database session for database operations.

    Returns:
        List[Lesson]: A list of all lesson objects.
    """
    return get_all_lessons(db)