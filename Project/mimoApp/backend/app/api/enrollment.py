from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from schemas.enrollment import EnrollmentCreate,EnrollmentResponse, EnrollmentUpdate
from services.enrollment_service import create_enrollment_handler, list_enrollments, get_enrollment, update_enrollment_handler, delete_enrollment

router = APIRouter()

# Ruta para crear una inscripción
@router.post("/", response_model=EnrollmentResponse)
def create_enrollment_handler(enrollment: EnrollmentCreate, db: Session = Depends(get_db)):
    # Verificar si la inscripción ya existe
    existing_enrollment = get_enrollment_by_user_course(db, enrollment.user_id, enrollment.course_id)
    if existing_enrollment:
        raise HTTPException(status_code=400, detail="Enrollment already exists")
    
    # Crear la inscripción
    return create_enrollment(db, enrollment)

# Ruta para obtener todas las inscripciones
@router.get("/", response_model=List[EnrollmentResponse])
def get_all_enrollments(db: Session = Depends(get_db)):
    return list_enrollments(db)

# Ruta para obtener una inscripción por ID
@router.get("/{id}", response_model=EnrollmentResponse)
def get_enrollment_by_id(enrollment_id: int, db: Session = Depends(get_db)):
    enrollment = get_enrollment(db, enrollment_id)
    if enrollment is None:
        raise HTTPException(status_code=404, detail="Enrollment not found")
    return enrollment

# Ruta para actualizar una inscripción
@router.put("/{id}", response_model=EnrollmentResponse)
def modify_enrollment(enrollment_id: int, enrollment: EnrollmentUpdate, db: Session = Depends(get_db)):
    updated_enrollment = update_enrollment(db, enrollment_id, enrollment)
    if updated_enrollment is None:
        raise HTTPException(status_code=404, detail="Enrollment not found")
    return updated_enrollment

# Ruta para eliminar una inscripción
@router.delete("/{id}")
def remove_enrollment(enrollment_id: int, db: Session = Depends(get_db)):
    enrollment = delete_enrollment(db, enrollment_id)
    if enrollment is None:
        raise HTTPException(status_code=404, detail="Enrollment not found")
    return {"message": "Enrollment deleted successfully"}
