from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserCreate
from core.security import hash_password

def create_user(db: Session, user: UserCreate):
    """
    Creates a new user in the database.

    This function takes a `UserCreate` schema with the user's email and password, hashes the password,
    and creates a new `User` object with the hashed password. The user is then added to the database,
    and the transaction is committed. The created `User` object is returned.

    Args:
        db (Session): The database session used to interact with the database.
        user (UserCreate): The data for the user to be created, including the email and password.

    Returns:
        User: The created `User` object with the assigned database ID.
    """
    # Hash the password
    hashed_password = hash_password(user.password)
    
    # Create a new User object
    db_user = User(username=user.email.split("@")[0], email=user.email, hashed_password=hashed_password)
    
    # Add the user to the session and commit the transaction
    db.add(db_user)
    db.commit()
    
    # Refresh the object to get the latest state from the database
    db.refresh(db_user)
    
    # Return the created user
    return db_user

def get_user(db: Session, user_id: int):
    """
    Retrieves a user from the database by their ID.

    Args:
        db (Session): The database session used to interact with the database.
        user_id (int): The ID of the user to be retrieved.

    Returns:
        User: The `User` object corresponding to the given ID, or None if not found.
    """
    # Query the database for the user by their ID
    return db.query(User).filter(User.id == user_id).first()
