from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from schemas.Lesson import LessonCreate
from services.Lesson_services import add_lesson, list_lesson, update_lesson, delete_lesson

# Create an instance of a router to handle lesson-related routes
router = APIRouter()

@router.post("/")
def create_lesson(lesson: LessonCreate, db: Session = Depends(get_db)):
    """
    Creates a new lesson in the system.

    This endpoint allows you to create a new lesson by providing the necessary 
    lesson data in the request body. Before creation, it checks if a lesson with 
    the same name already exists.

    Parameters:
        - lesson (LessonCreate): The lesson data to be created.
        - db (Session): Database session provided by `get_db`.

    Returns:
        - dict: The details of the newly created lesson.

    Raises:
        - HTTPException (400): If the lesson already exists.

    Example response:
        {"id": 1, "name": "Lesson 1", "description": "Description of Lesson 1"}
    """
    # Check if the lesson already exists
    existing_lesson = list_lesson(db, lesson.name)  # Assuming `name` is a unique attribute
    if existing_lesson:
        raise HTTPException(status_code=400, detail="Lesson already exists")
    
    # Calls the service to add the lesson to the database
    return add_lesson(db, lesson)

@router.get("/")
def get_all_lessons(db: Session = Depends(get_db)):
    """
    Retrieves the list of all lessons.

    This endpoint returns a list of all lessons present in the system. 
    The lessons are retrieved from the database.

    Parameters:
        - db (Session): Database session provided by `get_db`.

    Returns:
        - list: A list of all lessons in the system.

    Example response:
        [
            {"id": 1, "name": "Lesson 1", "description": "Description of Lesson 1"},
            {"id": 2, "name": "Lesson 2", "description": "Description of Lesson 2"}
        ]
    """
    # Calls the service to list all lessons from the database
    return list_lesson(db)

@router.get("/{id}")
def get_lesson(id: int, db: Session = Depends(get_db)):
    """
    Retrieves a specific lesson by its ID.

    This endpoint returns the details of a specific lesson identified by 
    its ID. If no lesson is found, an error is raised.

    Parameters:
        - id (int): The ID of the lesson to retrieve.
        - db (Session): Database session provided by `get_db`.

    Returns:
        - dict: The details of the lesson identified by the provided ID.

    Raises:
        - HTTPException (404): If the lesson is not found.

    Example response:
        {"id": 1, "name": "Lesson 1", "description": "Description of Lesson 1"}
    """
    # Retrieve the lesson by ID
    lesson = list_lesson(db, id)
    if lesson is None:
        raise HTTPException(status_code=404, detail="Lesson not found")
    return lesson

@router.put("/{id}")
def modify_lesson(id: int, lesson: LessonCreate, db: Session = Depends(get_db)):
    """
    Modifies the details of an existing lesson.

    This endpoint allows you to update the details of an existing lesson 
    by providing the new data in the request body.

    Parameters:
        - id (int): The ID of the lesson to update.
        - lesson (LessonCreate): The new lesson data.
        - db (Session): Database session provided by `get_db`.

    Returns:
        - dict: The updated details of the lesson.

    Example response:
        {"id": 1, "name": "Updated Lesson 1", "description": "Updated description"}
    """
    # Calls the service to update the lesson with the given ID
    return update_lesson(db, id, lesson)

@router.delete("/{id}")
def remove_lesson(id: int, db: Session = Depends(get_db)):
    """
    Deletes a lesson by its ID.

    This endpoint deletes a specific lesson identified by its ID.

    Parameters:
        - id (int): The ID of the lesson to delete.
        - db (Session): Database session provided by `get_db`.

    Returns:
        - dict: A confirmation message indicating the lesson was deleted.

    Example response:
        {"message": "Lesson deleted successfully"}
    """
    # Calls the service to delete the lesson by ID
    return delete_lesson(db, id)
