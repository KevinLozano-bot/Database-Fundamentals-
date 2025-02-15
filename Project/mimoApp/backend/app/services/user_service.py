from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends
from jose import jwt, JWTError
from passlib.context import CryptContext
from db.database import db_instance
from repositories.user_repo import create_user, get_user_by_email, get_user_by_id
from schemas.user import UserCreate
from core.config import settings
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """
    Hashes a plain password using bcrypt.
    """
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifies if a plain password matches its hashed version.
    """
    return pwd_context.verify(plain_password, hashed_password)

from schemas.user import UserCreate  # Asegúrate de importar correctamente el esquema

def registrer_user(db: Session, user: UserCreate):
    """
    Registers a new user if they don't already exist.
    """
    existing_user = get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="User already registered")

    # Hash the password before creating the user
    hashed_password = hash_password(user.password)

    # Crear un diccionario con los datos de UserCreate y añadir hashed_password
    user_data = user.dict()
    user_data.pop("password")  # Eliminar el campo password porque no se almacena en la DB
    user_data["hashed_password"] = hashed_password

    # Llamar a create_user con los datos corregidos
    return create_user(db, user_data)

def authenticate_user(db: Session, email: str, password: str):
    """
    Authenticates a user by verifying their email and password.
    """
    user = get_user_by_email(db, email)
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user

def create_access_token(data: dict, expires_delta: timedelta = None):
    """
    Creates a JWT access token.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    # Store user ID in the token's sub (subject) field
    to_encode.update({"sub": str(data["user_id"])})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

def get_db():
    """
    Dependency for obtaining a database session.
    """
    yield from db_instance.get_session()


def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]) 
    user_id = payload.get("sub")
    if user_id is None:
        raise HTTPException(status_code=401, detail="Invalid token")

    
    try:
        user_id = int(user_id)
    except ValueError:
        raise HTTPException(status_code=401, detail="Invalid user ID in token")
    
    user = get_user_by_id(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user


def get_user_by_id_service(db: Session, user_id: int):
    """
    Retrieves a user by their ID using the repository layer.
    """
    return get_user_by_id(db, user_id)
