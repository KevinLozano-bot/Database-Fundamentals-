from sqlalchemy.orm import Session
from repositories.enrollment_repo import create_enrollment, get_all_enrollments, get_enrollment_by_id, update_enrollment, delete_enrollment
from schemas.enrollment import EnrollmentCreate, EnrollmentUpdate
from fastapi import APIRouter, Depends
from typing import List
from db.session import get_db
from models.enrollment import Enrollment

router = APIRouter()

@router.post("/enrollments/", response_model=Enrollment)
def create_enrollment_handler(enrollment: EnrollmentCreate, db: Session = Depends(get_db)):
    return create_enrollment(db, enrollment)

@router.get("/enrollments/", response_model=List[Enrollment])
def list_enrollments(db: Session = Depends(get_db)):
    return get_all_enrollments(db)

@router.get("/enrollments/{enrollment_id}", response_model=Enrollment)
def get_enrollment(enrollment_id: int, db: Session = Depends(get_db)):
    return get_enrollment_by_id(db, enrollment_id)

@router.put("/enrollments/{enrollment_id}", response_model=Enrollment)
def update_enrollment_handler(enrollment_id: int, enrollment: EnrollmentUpdate, db: Session = Depends(get_db)):
    return update_enrollment(db, enrollment_id, enrollment)

@router.delete("/enrollments/{enrollment_id}", response_model=Enrollment)
def delete_enrollment_handler(enrollment_id: int, db: Session = Depends(get_db)):
    return delete_enrollment(db, enrollment_id)
