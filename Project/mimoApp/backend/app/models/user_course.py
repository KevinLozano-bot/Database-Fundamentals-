"""   
    This model defines the 'user_courses' table, with columns for storing the relationship 
    between users and courses, and whether the user has completed the course. It also ensures 
    referential integrity between users and courses via foreign keys."""
from sqlalchemy import Column, ForeignKey, Integer, Boolean
from backend.app.db.base import Base

class UserCourse(Base):
    """
    Attributes:
        id (int): The unique identifier for the user-course relationship (primary key).
        user_id (int): The ID of the user enrolled in the course (foreign key).
        course_id (int): The ID of the course the user is enrolled in (foreign key).
        completed (bool): Whether the user has completed the course.
    """
    __tablename__ = "user_courses"  # Name of the table in the database

    # Define columns in the 'user_courses' table
    id = Column(Integer, primary_key=True, index=True)  # Primary key for the user-course relationship
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))  # Foreign key linking to 'users.id'
    course_id = Column(Integer, ForeignKey("courses.id", ondelete="CASCADE"))  # Foreign key linking to 'courses.id'
    completed = Column(Boolean, default=False)  # Whether the user has completed the course, default is False

