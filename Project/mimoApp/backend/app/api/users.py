from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.user import User  # Suponiendo que tienes un modelo de SQLAlchemy llamado User
from schemas.user import UserResponse  # Este debe ser un esquema de Pydantic válido
from services.user_service import get_db,get_current_user
router = APIRouter()

@router.get("/me", response_model=UserResponse)
def read_users_me(current_user: User = Depends(get_current_user)):
    return UserResponse.model_validate(current_user)  # Para Pydantic v2