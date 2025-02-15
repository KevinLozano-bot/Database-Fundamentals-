""" This model defines the 'users' table, which stores information about each user, such as their 
    username, email, and hashed password. It ensures that users can be uniquely identified by their 
    username and email, and stores passwords securely in a hashed format.
    """
from sqlalchemy import Column, Integer, String
from db.database import Base

class User(Base):
    """
    Attributes:
        id (int): The unique identifier for the user (primary key).
        username (str): The user's unique username.
        email (str): The user's unique email address.
        hashed_password (str): The hashed password for the user, used for authentication.
    """
    __tablename__ = "users"  # Name of the table in the database

    # Define columns in the 'users' table
    id = Column(Integer, primary_key=True, index=True)  # Primary key for the user
    username = Column(String, unique=True, index=True)  # Unique username for the user
    email = Column(String, unique=True, index=True)  # Unique email address for the user
    hashed_password = Column(String, nullable=False)  # Hashed password, cannot be null
