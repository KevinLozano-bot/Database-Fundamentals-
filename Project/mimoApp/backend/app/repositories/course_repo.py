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
    db_course = Course(title=course.title, description=course.description)
    
    # Add the new course to the session and commit the transaction
    db.add(db_course)
    db.commit()
    
    # Refresh the object to get the latest state from the database
    db.refresh(db_course)
    
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
