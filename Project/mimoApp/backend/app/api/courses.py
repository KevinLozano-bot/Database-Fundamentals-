from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.database import db_instance  
from schemas.course import CourseCreate, CourseUpdate, CourseResponse
from services.course_service import (
    add_course,
    list_course,
    get_course,
    update_course,
    delete_course,
)

router = APIRouter(prefix="/courses", tags=["Courses"])

# Create a new course
@router.post("/", response_model=CourseResponse, status_code=status.HTTP_201_CREATED)
def create_course(course: CourseCreate, db: Session = Depends(db_instance.get_session)):  
    """
    Creates a new course in the system.
    
    This endpoint allows you to create a new course by providing the necessary 
    course data in the request body. Once the course is successfully added, 
    the details of the created course are returned.
    
    Parameters:
        - course (CourseCreate): The course data to be created.
        - db (Session): Database session provided by `get_session`.
        
    Returns:
        - CourseResponse: The details of the newly created course.
    """
    return add_course(db, course)

# Get all courses
@router.get("/", response_model=list[CourseResponse])
def get_all_courses(db: Session = Depends(db_instance.get_session)):  # Se usa get_session
    """
    Retrieves the list of all courses.
    
    This endpoint returns a list of all courses present in the system. 
    The courses will be retrieved from the database.
    
    Parameters:
        - db (Session): Database session provided by `get_session`.
        
    Returns:
        - list[CourseResponse]: A list of all courses in the system.
    """
    return list_course(db)

# Get a specific course by ID
@router.get("/{course_id}", response_model=CourseResponse)
def get_single_course(course_id: int, db: Session = Depends(db_instance.get_session)):  # Se usa get_session
    """
    Retrieves a course by its ID.
    
    This endpoint allows you to retrieve a specific course using its unique ID. 
    If the course is not found, a 404 Not Found error is returned.
    
    Parameters:
        - course_id (int): The ID of the course to retrieve.
        - db (Session): Database session provided by `get_session`.
        
    Returns:
        - CourseResponse: The details of the requested course.
    """
    course = get_course(db, course_id)
    if not course:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")
    return course

# Update a course by ID
@router.put("/{course_id}", response_model=CourseResponse)
def update_course_details(course_id: int, course_data: CourseUpdate, db: Session = Depends(db_instance.get_session)):  # Se usa get_session
    """
    Updates a course's details by ID.
    
    This endpoint allows you to update the details of an existing course 
    using its unique ID. If the course is not found, a 404 Not Found error 
    is returned.
    
    Parameters:
        - course_id (int): The ID of the course to update.
        - course_data (CourseUpdate): The updated course data.
        - db (Session): Database session provided by `get_session`.
        
    Returns:
        - CourseResponse: The updated course details.
    """
    course = update_course(db, course_id, course_data)
    if not course:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")
    return course

# Delete a course by ID
@router.delete("/{course_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_course_item(course_id: int, db: Session = Depends(db_instance.get_session)):  # Se usa get_session
    """
    Deletes a course by its ID.
    
    This endpoint allows you to delete a specific course using its unique ID. 
    If the course is not found, a 404 Not Found error is returned.
    
    Parameters:
        - course_id (int): The ID of the course to delete.
        - db (Session): Database session provided by `get_session`.
        
    Returns:
        - None: Returns no content upon successful deletion.
    """
    if not delete_course(db, course_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")
