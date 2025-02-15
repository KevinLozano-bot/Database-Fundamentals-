from sqlalchemy.orm import Session
from models.Lesson import Lesson
from schemas.Lesson import LessonCreate

def create_lesson(db: Session, lesson: LessonCreate):
    """
    Creates a new lesson in the database.

    This function accepts lesson details from the client in the form of a `LessonCreate` schema, 
    creates a new `Lesson` object, and saves it to the database. After committing the transaction,
    it returns the created `Lesson` object.

    Args:
        db (Session): The database session used to interact with the database.
        lesson (LessonCreate): The data for the lesson to be created, including its title, content, and course ID.

    Returns:
        Lesson: The created `Lesson` object with the assigned database ID.
    """
    # Create a new Lesson object using the data from the LessonCreate schema
    db_lesson = Lesson(
        title=lesson.title,
        content=lesson.content,
        course_id=lesson.course_id
    )
    
    # Add the new lesson to the session and commit the transaction
    db.add(db_lesson)
    db.commit()
    db.refresh(db_lesson)  # Refresh the object to get the latest state from the database
    
    # Return the created lesson
    return db_lesson

def delete_lesson(db: Session, lesson_id: int):
    """
    Deletes a lesson from the database.

    This function deletes a lesson from the database by its ID. After committing the transaction, 
    it returns the deleted `Lesson` object.

    Args:
        db (Session): The database session used to interact with the database.
        lesson_id (int): The ID of the lesson to be deleted.

    Returns:
        Lesson: The deleted `Lesson` object, or None if not found.
    """
    # Query the database for the lesson by its ID
    db_lesson = db.query(Lesson).filter(Lesson.id == lesson_id).first()
    
    # Check if the lesson exists
    if db_lesson:
        # Delete the lesson from the session
        db.delete(db_lesson)
        db.commit()
    
    # Return the deleted lesson (or None if not found)
    return db_lesson

def get_all_lessons(db: Session):
    """
    Retrieves all lessons from the database.

    This function queries the database to fetch all existing lessons and returns them.

    Args:
        db (Session): The database session used to interact with the database.

    Returns:
        List[Lesson]: A list of all `Lesson` objects in the database.
    """
    # Query the database for all lessons
    return db.query(Lesson).all()

def get_lesson_by_id(db: Session, lesson_id: int):
    """
    Retrieves a lesson by its ID from the database.

    Args:
        db (Session): The database session used to interact with the database.
        lesson_id (int): The ID of the lesson to be retrieved.

    Returns:
        Lesson: The `Lesson` object corresponding to the given ID, or None if not found.
    """
    # Query the database for the lesson by its ID
    return db.query(Lesson).filter(Lesson.id == lesson_id).first()

def get_lessons_by_course_id(db: Session, course_id: int):
    """
    Retrieves all lessons for a specific course.

    Args:
        db (Session): The database session used to interact with the database.
        course_id (int): The ID of the course for which lessons are to be fetched.

    Returns:
        List[Lesson]: A list of `Lesson` objects associated with the given course ID.
    """
    # Query the database for lessons with the specified course ID
    return db.query(Lesson).filter(Lesson.course_id == course_id).all()

def update_lesson(db: Session, lesson_id: int, lesson: LessonCreate):
    """
    Updates an existing lesson in the database.

    Args:
        db (Session): The database session used to interact with the database.
        lesson_id (int): The ID of the lesson to be updated.
        lesson (LessonCreate): The new data for the lesson, including its title, content, and course ID.

    Returns:
        Lesson: The updated `Lesson` object, or None if not found.
    """
    # Query the database for the lesson by its ID
    db_lesson = db.query(Lesson).filter(Lesson.id == lesson_id).first()
    
    # Check if the lesson exists
    if db_lesson:
        # Update the lesson's title, content, and course ID
        db_lesson.title = lesson.title
        db_lesson.content = lesson.content
        db_lesson.course_id = lesson.course_id
        
        # Commit the changes
        db.commit()
        db.refresh(db_lesson)  # Refresh the object to get the latest state from the database
    
    # Return the updated lesson (or None if not found)
    return db_lesson

def get_lesson_by_title(db: Session, title: str):
    """
    Retrieves a lesson by its title from the database.

    Args:
        db (Session): The database session used to interact with the database.
        title (str): The title of the lesson to be retrieved.

    Returns:
        Lesson: The `Lesson` object corresponding to the given title, or None if not found.
    """
    # Query the database for the lesson by its title
    return db.query(Lesson).filter(Lesson.title == title).first()
