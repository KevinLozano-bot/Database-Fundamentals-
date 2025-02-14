from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta
from db.session import get_db
from schemas.user import UserCreate
from services.user_service import registrer_user, authenticate_user, create_access_token
from core.config import settings

# Create an instance of a router to handle authentication routes
router = APIRouter()

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    """
    Registers a new user in the database.

    This endpoint receives the necessary user data to create a new user in the 
    system. The data is sent in JSON format in the request body. If the user is 
    successfully created, a message confirming the creation and the username 
    will be returned.

    Parameters:
        - user (UserCreate): Information of the user to be registered.
        - db (Session): Database session provided by `get_db`.

    Returns:
        - dict: A success message along with the username of the newly created user.

    Example response:
        {"message": "User Created Successfully", "user": "new_username"}
    """
    # Calls the service to register the user in the database
    db_user = registrer_user(db, user)
    
    # Returns a success response
    return {"message": "User Created Successfully", "user": db_user.username}

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """
    Logs in a user and returns an access token.

    This endpoint allows users to authenticate by providing their username and 
    password. If the authentication is successful, an access token is generated 
    and returned, which can be used for authenticating future requests.

    Parameters:
        - form_data (OAuth2PasswordRequestForm): Login form data, including 
        the username and password.
        - db (Session): Database session provided by `get_db`.

    Returns:
        - dict: A valid access token along with the token type.

    Exceptions:
        - HTTPException (401): If the username or password is incorrect.

    Example response:
        {"access_token": "some_access_token", "token_type": "bearer"}
    """
    # Verifies the authentication of the user
    user = authenticate_user(db, form_data.username, form_data.password)
    
    # If the user is not found or credentials are incorrect
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect email or password")
    
    # Defines the expiration time for the access token
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    # Creates an access token using the user's ID
    access_token = create_access_token(data={"sub": user.id}, expires_delta=access_token_expires)
    
    # Returns the access token
    return {"access_token": access_token, "token_type": "bearer"}
