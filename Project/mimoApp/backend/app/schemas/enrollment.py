from datetime import datetime
from pydantic import BaseModel

class EnrollmentCreate(BaseModel):
    user_id: int
    course_id: int
    enrollment_date: datetime  # Asegúrate de que el cliente pase una fecha en el formato correcto

class EnrollmentUpdate(BaseModel):
    user_id: int
    course_id: int
    enrollment_date: datetime

class EnrollmentResponse(BaseModel):
    id: int
    user_id: int
    course_id: int
    enrollment_date: datetime  # Esto ya es un campo de tipo `datetime`

    class Config:
        orm_mode = True  # Esto es necesario para que FastAPI maneje correctamente el ORM de SQLAlchemy
        arbitrary_types_allowed = True  # Esto permite tipos arbitrarios si es necesario
