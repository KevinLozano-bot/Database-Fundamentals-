from datetime import datetime
from pydantic import BaseModel, ConfigDict

class EnrollmentCreate(BaseModel):
    user_id: int
    course_id: int
    enrollment_date: datetime

class EnrollmentUpdate(BaseModel):
    user_id: int
    course_id: int
    enrollment_date: datetime
    

class EnrollmentResponse(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    id: int
    user_id: int
    course_id: int
    enrollment_date: datetime

    class Config:
        orm_mode = True  # Usado para que FastAPI maneje el ORM de SQLAlchemy correctamente
