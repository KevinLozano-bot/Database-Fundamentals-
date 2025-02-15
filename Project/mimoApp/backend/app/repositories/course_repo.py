from sqlalchemy.orm import Session
from models.course import Course
from schemas.course import CourseCreate

def create_course(db: Session, course: CourseCreate):    
    """
    Creates a new course in the database.

    This function accepts course details from the client in the form of a `CourseCreate` schema, 
    creates a new `Course` object, and saves it to the database. After committing the transaction, 
    it returns the created `Course` object.

    Args:
        db (Session): The database session used to interact with the database.
        course (CourseCreate): The data for the course to be created, including its title and description.

    Returns:
        Course: The created `Course` object with the assigned database ID.
    """
    # Create a new Course object using the data from the CourseCreate schema
    db_course = Course(
        title=course.title, 
        description=course.description
    )
    
    # Add the new course to the session and commit the transaction
    db.add(db_course)
    db.commit()
    db.refresh(db_course)  # Refresh the object to get the latest state from the database
    
    # Return the created course
    return db_course

def get_all_courses(db: Session):
    """
    Retrieves all courses from the database.

    This function queries the database to fetch all existing courses and returns them.

    Args:
        db (Session): The database session used to interact with the database.

    Returns:
        List[Course]: A list of all `Course` objects in the database.
    """
    # Query the database for all courses
    return db.query(Course).all()

def get_course_by_id(db: Session, course_id: int):
    """
    Retrieves a course from the database by its ID.

    Args:
        db (Session): The database session used to interact with the database.
        course_id (int): The ID of the course to be retrieved.

    Returns:
        Course: The `Course` object corresponding to the given ID, or None if not found.
    """
    # Query the database for the course by its ID
    return db.query(Course).filter(Course.id == course_id).first()

def update_course(db: Session, course_id: int, course: CourseCreate):
    """
    Updates an existing course in the database.

    This function searches for a course by its ID and updates its title and description if found.

    Args:
        db (Session): The database session used to interact with the database.
        course_id (int): The ID of the course to be updated.
        course (CourseCreate): The updated data for the course.

    Returns:
        Course | None: The updated `Course` object, or None if not found.
    """
    # Query the database for the course by its ID
    db_course = db.query(Course).filter(Course.id == course_id).first()
    
    # Check if the course exists
    if db_course:
        # Update the course details
        db_course.title = course.title
        db_course.description = course.description
        db.commit()
    
    # Return the updated course (or None if not found)
    return db_course

def delete_course(db: Session, course_id: int):
    """
    Deletes a course from the database by its ID.

    Args:
        db (Session): The database session used to interact with the database.
        course_id (int): The ID of the course to be deleted.

    Returns:
        Course: The deleted `Course` object, or None if not found.
    """
    # Query the database for the course by its ID
    db_course = db.query(Course).filter(Course.id == course_id).first()
    
    # Check if the course exists
    if db_course:
        db.delete(db_course)
        db.commit()
    
    # Return the deleted course (or None if not found)
    return db_course