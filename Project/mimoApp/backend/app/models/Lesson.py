from sqlalchemy import Column, Integer, String
from db.database import Base
from sqlalchemy import ForeignKey

class Lesson(Base):
    """
    Represents a lesson in the database, which is associated with a course.

    This model defines the 'lessons' table, with columns for storing the lesson's ID,
    title, content, and the ID of the course it belongs to. It is mapped to the 'lessons' table
    using SQLAlchemy's ORM (Object-Relational Mapping) system.

    Attributes:
        id (int): The unique identifier for the lesson (primary key).
        title (str): The title of the lesson, which must be unique.
        content (str): The content of the lesson.
        course_id (int): The ID of the course to which the lesson belongs (foreign key).
    """
    __tablename__ = "lessons"  # Name of the table in the database

    # Define columns in the 'lessons' table
    id = Column(Integer, primary_key=True, index=True)  # Primary key for the lesson
    title = Column(String, unique=True, index=True, nullable=False)  # Unique lesson title
    content= Column(String, nullable=False)  # Content of the lesson
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)  # Foreign key linking to 'courses.id'
