from sqlalchemy import Column, Integer, String
from db.database import Base

class Course(Base):
    """
    Represents a course in the database.

    This model defines the 'courses' table, with columns for storing the course's ID,
    title, and description. It is mapped to the 'courses' table using SQLAlchemy's
    ORM (Object-Relational Mapping) system.

    Attributes:
        id (int): The unique identifier for the course (primary key).
        title (str): The title of the course, which must be unique.
        description (str): A description of the course content.
    """
    __tablename__ = "courses"  # Name of the table in the database

    # Define columns in the 'courses' table
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)  # Primary key for the course
    title = Column(String, unique=True, index=True, nullable=False)  # Unique course title
    description = Column(String, nullable=False)  # Course description
