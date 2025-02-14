from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends
from jose import jwt, JWTError
from passlib.context import CryptContext
from db.session import SessionLocal
from repositories.user_repo import create_user, get_user
from schemas.user import UserCreate
from models.user import User
from core.config import settings
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """
    Hashes a plain password using bcrypt.

    Args:
        password (str): The plain text password.

    Returns:
        str: The hashed password.
    """
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifies if a plain password matches its hashed version.

    Args:
        plain_password (str): The plain text password.
        hashed_password (str): The hashed password from the database.

    Returns:
        bool: True if the passwords match, False otherwise.
    """
    return pwd_context.verify(plain_password, hashed_password)

def registrer_user(db: Session, user: UserCreate):
    """
    Registers a new user if they don't already exist.

    Args:
        db (Session): Database session.
        user (UserCreate): User data to create a new user.

    Returns:
        User: The newly created user object.

    Raises:
        ValueError: If the user is already registered.
    """
    existing_user = get_user(db, user.email)
    if existing_user:
        raise ValueError("User already registered")

    hashed_password = hash_password(user.password)
    return create_user(
        db,
        UserCreate(
            username=user.email.split("@")[0], 
            email=user.email, 
            password=hashed_password
        )
    )

def authenticate_user(db: Session, email: str, password: str):
    """
    Authenticates a user by verifying their email and password.

    Args:
        db (Session): Database session.
        email (str): User's email.
        password (str): User's password.

    Returns:
        User | None: The authenticated user or None if authentication fails.
    """
    user = get_user(db, email)
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user

def create_access_token(data: dict, expires_delta: timedelta = None):
    """
    Creates a JWT access token.

    Args:
        data (dict): The data to encode in the token.
        expires_delta (timedelta, optional): Token expiration time.

    Returns:
        str: The encoded JWT token.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

def get_db():
    """
    Dependency for obtaining a database session.

    Yields:
        Session: Database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(
    db: Session = Depends(get_db), 
    token: str = Depends(oauth2_scheme)
) -> User:
    """
    Retrieves the currently authenticated user using JWT.

    Args:
        db (Session): Database session.
        token (str): OAuth2 token from request.

    Returns:
        User: The authenticated user object.

    Raises:
        HTTPException: If the token is invalid or user not found.
    """
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]) 
        user_id: int = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")
    except JWTError as exc:
        raise HTTPException(status_code=401, detail="Invalid token") from exc
    
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=401, detail="User not found")
    
    return user

def get_user_by_id(db: Session, user_id: int):
    """
    Retrieves a user by their ID.

    Args:
        db (Session): Database session.
        user_id (int): The ID of the user.

    Returns:
        User | None: The user object or None if not found.
    """
    return db.query(User).filter(User.id == user_id).first()
