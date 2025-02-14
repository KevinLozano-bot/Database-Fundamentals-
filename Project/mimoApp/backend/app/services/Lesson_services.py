from sqlalchemy.orm import Session
from models.Lesson import Lesson  # Ensure you import your Lesson model correctly
from schemas.Lesson import LessonCreate

def list_lesson(db: Session, lesson_identifier: str = None):
    """
    Retrieves a lesson from the database.

    If a lesson identifier is provided, it searches for a lesson by its name.
    Otherwise, it returns the first lesson found.

    Args:
        db (Session): The database session for querying.
        lesson_identifier (str, optional): The name of the lesson to search for.

    Returns:
        Lesson | None: The first lesson found or None if not found.
    """
    query = db.query(Lesson)
    if lesson_identifier:
        query = query.filter(Lesson.name == lesson_identifier)
    return query.first()

def add_lesson(db: Session, lesson: LessonCreate):
    """
    Adds a new lesson to the database.

    This function creates a new Lesson instance using the provided data 
    and saves it to the database.

    Args:
        db (Session): The database session for operations.
        lesson (LessonCreate): The data required to create a new lesson.

    Returns:
        Lesson: The newly created lesson object.
    """
    new_lesson = Lesson(name=lesson.name, description=lesson.description)
    db.add(new_lesson)
    db.commit()
    db.refresh(new_lesson)
    return new_lesson

def update_lesson(db: Session, lesson_id: int, lesson: LessonCreate):
    """
    Updates an existing lesson in the database.

    This function searches for a lesson by its ID and updates its name 
    and description if found.

    Args:
        db (Session): The database session for operations.
        lesson_id (int): The ID of the lesson to be updated.
        lesson (LessonCreate): The new data for the lesson.

    Returns:
        Lesson | None: The updated lesson object or None if not found.
    """
    existing_lesson = db.query(Lesson).filter(Lesson.id == lesson_id).first()
    if existing_lesson:
        existing_lesson.name = lesson.name
        existing_lesson.description = lesson.description
        db.commit()
        db.refresh(existing_lesson)
        return existing_lesson
    return None

def delete_lesson(db: Session, lesson_id: int):
    """
    Deletes a lesson from the database.

    This function searches for a lesson by its ID and deletes it if found.

    Args:
        db (Session): The database session for operations.
        lesson_id (int): The ID of the lesson to be deleted.

    Returns:
        dict: A message indicating whether the lesson was deleted or not found.
    """
    lesson = db.query(Lesson).filter(Lesson.id == lesson_id).first()
    if lesson:
        db.delete(lesson)
        db.commit()
        return {"detail": "Lesson deleted"}
    return {"detail": "Lesson not found"}
