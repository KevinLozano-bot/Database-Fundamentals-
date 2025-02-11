from pydantic import BaseModel
from typing import Optional

class LessonCreate(BaseModel):
    title: str
    description: str

class LessonResponse(BaseModel):
    id: int
    title: str
    description: str

    class Config:
        orm_mode = True  # Usado para que FastAPI maneje el ORM de SQLAlchemy correctamente

class LessonUpdate(BaseModel):
    title: Optional[str] = None  # Los campos son opcionales en una actualización
    description: Optional[str] = None


