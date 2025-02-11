from sqlalchemy.orm import Session
from repositories.enrollment_repo import create_enrollment, get_all_enrollments, get_enrollment_by_id, update_enrollment, delete_enrollment, get_enrollmet_by_user_course
from schemas.enrollment import EnrollmentCreate, EnrollmentUpdate, EnrollmentResponse
from fastapi import APIRouter, Depends, HTTPException
from typing import List
from db.session import get_db

router = APIRouter()

# Crear inscripción
@router.post("/enrollments/", response_model=EnrollmentResponse)
def create_enrollment_handler(enrollment: EnrollmentCreate, db: Session = Depends(get_db)):
    # Verificar si la inscripción ya existe
    existing_enrollment = get_enrollmet_by_user_course(db, enrollment.user_id, enrollment.course_id)
    if existing_enrollment:
        raise HTTPException(status_code=400, detail="Enrollment already exists")
    
    # Crear y retornar la inscripción
    return create_enrollment(db, enrollment)

# Obtener todas las inscripciones
@router.get("/enrollments/", response_model=List[EnrollmentResponse])
def list_enrollments(db: Session = Depends(get_db)):
    enrollments = get_all_enrollments(db)
    return enrollments

# Obtener inscripción por ID
@router.get("/enrollments/{enrollment_id}", response_model=EnrollmentResponse)
def get_enrollment(enrollment_id: int, db: Session = Depends(get_db)):
    enrollment = get_enrollment_by_id(db, enrollment_id)
    if enrollment is None:
        raise HTTPException(status_code=404, detail="Enrollment not found")
    return enrollment

# Actualizar inscripción
@router.put("/enrollments/{enrollment_id}", response_model=EnrollmentResponse)
def update_enrollment_handler(enrollment_id: int, enrollment: EnrollmentUpdate, db: Session = Depends(get_db)):
    updated_enrollment = update_enrollment(db, enrollment_id, enrollment)
    if updated_enrollment is None:
        raise HTTPException(status_code=404, detail="Enrollment not found")
    return updated_enrollment

# Eliminar inscripción
@router.delete("/enrollments/{enrollment_id}", response_model=EnrollmentResponse)
def delete_enrollment_handler(enrollment_id: int, db: Session = Depends(get_db)):
    enrollment = delete_enrollment(db, enrollment_id)
    if enrollment is None:
        raise HTTPException(status_code=404, detail="Enrollment not found")
    return {"message": "Enrollment deleted successfully"}
