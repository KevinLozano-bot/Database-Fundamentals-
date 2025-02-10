from sqlalchemy.orm import Session
from backend.app.models.user import User
from backend.schemas.user import UserCreate
from backend.app.core.security import hash_password

def create_user(db: Session, user: UserCreate):
    hashed_password = hash_password(user.password)
    db_user = User(username=user.email.split("@")[0], email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()
