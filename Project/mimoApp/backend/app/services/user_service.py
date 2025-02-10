from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from fastapi import HTTPException
from jose import jwt, JWTError
from passlib.context import CryptContext
from backend.app.repositories.user_repo import create_user, get_user
from backend.schemas.user import UserCreate
from backend.app.core.config import settings


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def registrer_user(db: Session, user: UserCreate):
    existing_user = get_user(db, user.email)
    if existing_user:
        raise ValueError("User already registered")
    
    hashed_password = hash_password(user.password)
    return create_user(db, UserCreate(username=user.email.split("@")[0], email=user.email, hashed_password=hashed_password))


def authenticate_user(db: Session, email: str, password: str):
    user = get_user(db, email)
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.upated({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

def get_current_user(db: Session, token: str):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        user_id: int = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")
    except JWTError as exc:
        raise HTTPException(status_code=401, detail="Invalid token") from exc  # Conservar la excepción original
    
    user = get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return user