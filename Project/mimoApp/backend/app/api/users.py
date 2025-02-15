from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from models.user import User  # Assuming you have a SQLAlchemy model named User
from schemas.user import UserResponse, UserCreate  # Pydantic schemas for user data
from services.user_service import get_current_user, registrer_user, get_user_by_id
from db.database import db_instance  # Se importa para usar get_session()

# Create an instance of the APIRouter for managing user-related routes
router = APIRouter(prefix="/users", tags=["Users"])

# Get the current authenticated user's data
@router.get("/me", response_model=UserResponse, status_code=status.HTTP_200_OK)
def read_users_me(current_user: User = Depends(get_current_user)):
    """
    Retrieve the current user's data.

    This endpoint returns the data of the currently authenticated user. 
    The user information is retrieved from the token and passed through 
    the `get_current_user` dependency.

    Parameters:
        - current_user (User): The current authenticated user obtained from the token.
    
    Returns:
        - UserResponse: The data of the authenticated user.
    
    Example response:
        {"id": 1, "username": "johndoe", "email": "john@example.com"}
    """
    # Converts the SQLAlchemy user object to a Pydantic UserResponse model
    return UserResponse.model_validate(current_user)

# Create a new user
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(db_instance.get_session)):  # Se usa get_session()
    """
    Create a new user.

    This endpoint allows you to create a new user by providing the necessary 
    user data in the request body. The data is passed to the `registrer_user` 
    service to handle the database insertion.

    Parameters:
        - user (UserCreate): The user data for creating the new user.
        - db (Session): The database session provided by the `get_session` dependency.

    Returns:
        - dict: A confirmation message or response indicating the user was created.
    
    Example response:
        {"message": "User Created Successfully", "user": "johndoe"}
    """
    # Calls the service to register the new user in the database
    new_user = registrer_user(db, user)
    
    return {"message": "User Created Successfully", "user": new_user.username}

# Retrieve a specific user by their ID
@router.get("/{user_id}", response_model=UserResponse, status_code=status.HTTP_200_OK)
def get_user(user_id: int, db: Session = Depends(db_instance.get_session)):  # Se usa get_session()
    """
    Retrieve a specific user by their ID.

    This endpoint retrieves the details of a user identified by their unique ID. 
    If no user is found with the given ID, a `404` error is raised.

    Parameters:
        - user_id (int): The ID of the user to retrieve.
        - db (Session): The database session provided by the `get_session` dependency.

    Returns:
        - UserResponse: The details of the user identified by the given ID.
    
    Raises:
        - HTTPException (404): If the user with the given ID is not found.
    
    Example response:
        {"id": 1, "username": "johndoe", "email": "john@example.com"}
    """
    # Calls the service to retrieve the user by ID from the database
    db_user = get_user_by_id(db, user_id)
    
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    return UserResponse.model_validate(db_user)
