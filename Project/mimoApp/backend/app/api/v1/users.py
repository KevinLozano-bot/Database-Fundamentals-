from fastapi import APIRouter, Depends
from backend.schemas.user import UserResponse
from backend.app.services.user_service import get_current_user

router = APIRouter()

@router.get("/me", response_model=UserResponse)
def read_users_me(current_user: UserResponse = Depends(get_current_user)):
    return current_user