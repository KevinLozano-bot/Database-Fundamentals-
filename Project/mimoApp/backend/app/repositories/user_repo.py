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
    # Check if the user already exists by email
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise ValueError("User with this email already exists.")
    
    # Hash the password
    hashed_password = hash_password(user.password)
    
    # Create a new User object
    db_user = User(
        username=user.email.split("@")[0], 
        email=user.email, 
        hashed_password=hashed_password
    )
    
    # Add the user to the session and commit the transaction
    db.add(db_user)
    db.commit()
    db.refresh(db_user)  # Refresh the object to get the latest state from the database
    
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
    # Verifica que el user_id sea un número entero
    if not isinstance(user_id, int):
        raise ValueError("El user_id debe ser un número entero.")
    
    # Query the database for the user by their ID
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    """
    Retrieves a user from the database by their email.

    Args:
        db (Session): The database session used to interact with the database.
        email (str): The email of the user to be retrieved.

    Returns:
        User: The `User` object corresponding to the given email, or None if not found.
    """
    # Query the database for the user by their email
    return db.query(User).filter(User.email == email).first()

def get_all_users(db: Session):
    """
    Retrieves all users from the database.

    This function queries the database to fetch all existing users and returns them.

    Args:
        db (Session): The database session used to interact with the database.

    Returns:
        List[User]: A list of all `User` objects in the database.
    """
    # Query the database for all users
    return db.query(User).all()

def delete_user(db: Session, user_id: int):
    """
    Deletes a user from the database by their ID.

    Args:
        db (Session): The database session used to interact with the database.
        user_id (int): The ID of the user to be deleted.

    Returns:
        User: The deleted `User` object, or None if not found.
    """
    # Verifica que el user_id sea un número entero
    if not isinstance(user_id, int):
        raise ValueError("El user_id debe ser un número entero.")
    
    # Query the database for the user by their ID
    db_user = db.query(User).filter(User.id == user_id).first()
    
    # Check if the user exists
    if db_user:
        db.delete(db_user)
        db.commit()
    
    # Return the deleted user (or None if not found)
    return db_user

def update_user(db: Session, user_id: int, user: UserCreate):
    """
    Updates an existing user in the database.

    Args:
        db (Session): The database session used to interact with the database.
        user_id (int): The ID of the user to be updated.
        user (UserCreate): The new data for the user, including the email and password.

    Returns:
        User: The updated `User` object, or None if not found.
    """
    # Verifica que el user_id sea un número entero
    if not isinstance(user_id, int):
        raise ValueError("El user_id debe ser un número entero.")
    
    # Query the database for the user by their ID
    db_user = db.query(User).filter(User.id == user_id).first()
    
    # Check if the user exists
    if db_user:
        # Update the user's email and hashed password
        db_user.email = user.email
        db_user.hashed_password = hash_password(user.password)
        
        # Commit the changes
        db.commit()
        db.refresh(db_user)  # Refresh the object to get the latest state from the database
    
    # Return the updated user (or None if not found)
    return db_user

def get_user_by_id(db: Session, user_id: int):
    """
    Retrieves a user from the database by their ID.

    Args:
        db (Session): The database session used to interact with the database.
        user_id (int): The ID of the user to be retrieved.

    Returns:
        User: The `User` object corresponding to the given ID, or None if not found.
    """
    # Verifica que el user_id sea un número entero
    if not isinstance(user_id, int):
        raise ValueError("El user_id debe ser un número entero.")
    
    # Query the database for the user by their ID
    return db.query(User).filter(User.id == user_id).first()
