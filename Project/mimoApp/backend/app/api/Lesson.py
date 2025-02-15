from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.database import db_instance  # Ahora se usa db_instance con get_session
from schemas.Lesson import LessonCreate
from services.Lesson_services import add_lesson, list_lesson, update_lesson, delete_lesson


router = APIRouter(prefix="/lessons", tags=["Lessons"])

# Create a new lesson
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_lesson(lesson: LessonCreate, db: Session = Depends(db_instance.get_session)):  # Se usa get_session
    """
    Creates a new lesson in the system.

    This endpoint allows you to create a new lesson by providing the necessary 
    lesson data in the request body. Before creation, it checks if a lesson with 
    the same name already exists.

    Parameters:
        - lesson (LessonCreate): The lesson data to be created.
        - db (Session): Database session provided by `get_session`.

    Returns:
        - dict: The details of the newly created lesson.

    Raises:
        - HTTPException (400): If the lesson already exists.
    """
    # Check if the lesson already exists
    existing_lesson = list_lesson(db)
    if any(l.name == lesson.name for l in existing_lesson):  # Verifica el nombre
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Lesson already exists")
    
    # Calls the service to add the lesson to the database
    return add_lesson(db, lesson)

# Get all lessons
@router.get("/", status_code=status.HTTP_200_OK)
def get_all_lessons(db: Session = Depends(db_instance.get_session)):  # Se usa get_session
    """
    Retrieves the list of all lessons.

    This endpoint returns a list of all lessons present in the system. 
    The lessons are retrieved from the database.

    Parameters:
        - db (Session): Database session provided by `get_session`.

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

# Get a specific lesson by ID
@router.get("/{id}", status_code=status.HTTP_200_OK)
def get_lesson(id: int, db: Session = Depends(db_instance.get_session)):  # Se usa get_session
    """
    Retrieves a specific lesson by its ID.

    This endpoint returns the details of a specific lesson identified by 
    its ID. If no lesson is found, an error is raised.

    Parameters:
        - id (int): The ID of the lesson to retrieve.
        - db (Session): Database session provided by `get_session`.

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
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lesson not found")
    return lesson

# Update a lesson by ID
@router.put("/{id}", status_code=status.HTTP_200_OK)
def modify_lesson(id: int, lesson: LessonCreate, db: Session = Depends(db_instance.get_session)):  # Se usa get_session
    """
    Modifies the details of an existing lesson.

    This endpoint allows you to update the details of an existing lesson 
    by providing the new data in the request body.

    Parameters:
        - id (int): The ID of the lesson to update.
        - lesson (LessonCreate): The new lesson data.
        - db (Session): Database session provided by `get_session`.

    Returns:
        - dict: The updated details of the lesson.

    Raises:
        - HTTPException (404): If the lesson is not found.

    Example response:
        {"id": 1, "name": "Updated Lesson 1", "description": "Updated description"}
    """
    # Calls the service to update the lesson with the given ID
    updated_lesson = update_lesson(db, id, lesson)
    if updated_lesson is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lesson not found")
    return updated_lesson

# Delete a lesson by ID
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_lesson(id: int, db: Session = Depends(db_instance.get_session)):  # Se usa get_session
    """
    Deletes a lesson by its ID.

    This endpoint deletes a specific lesson identified by its ID.

    Parameters:
        - id (int): The ID of the lesson to delete.
        - db (Session): Database session provided by `get_session`.

    Returns:
        - dict: A confirmation message indicating the lesson was deleted.

    Raises:
        - HTTPException (404): If the lesson is not found.

    Example response:
        {"message": "Lesson deleted successfully"}
    """
    # Calls the service to delete the lesson by ID
    if not delete_lesson(db, id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lesson not found")
