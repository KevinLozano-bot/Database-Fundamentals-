from datetime import datetime
from pydantic import BaseModel

class EnrollmentCreate(BaseModel):
    user_id: int
    course_id: int
    enrollment_date: datetime

class EnrollmentUpdate(BaseModel):
    user_id: int
    course_id: int
    enrollment_date: datetime
    

class EnrollmentResponse(BaseModel):
    id: int
    user_id: int
    course_id: int
    enrollment_date: datetime

    class Config:
        orm_mode = True  # Usado para que FastAPI maneje el ORM de SQLAlchemy correctamente
