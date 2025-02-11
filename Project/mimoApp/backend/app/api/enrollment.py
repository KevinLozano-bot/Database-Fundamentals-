from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from schemas.enrollment import EnrollmentCreate
from services.enrollment_service import create_enrollment_handler, list_enrollments, get_enrollment, update_enrollment_handler, delete_enrollment

router = APIRouter()

@router.post("/")
def create_enrollment(enrollment: EnrollmentCreate, db: Session = Depends(get_db)):
    enrollment = get_enrollment(db, enrollment)
    if enrollment:
        raise HTTPException(status_code=400, detail="Enrollment already exists")
    return create_enrollment_handler(db, enrollment)

@router.get("/")
def get_all_enrollments(db: Session = Depends(get_db)):
    return list_enrollments(db)

@router.get("/{id}")
def get_enrollment_by_id(enrollment_id: int, db: Session = Depends(get_db)):
    enrollment = get_enrollment(db, enrollment_id)
    if enrollment is None:
        raise HTTPException(status_code=404, detail="Enrollment not found")
    return enrollment

@router.put("/{id}")
def modify_enrollment(enrollment_id: int, enrollment: EnrollmentCreate, db: Session = Depends(get_db)):
    return update_enrollment_handler(db, enrollment_id, enrollment)

@router.delete("/{id}")
def remove_enrollment(enrollment_id: int, db: Session = Depends(get_db)):
    return delete_enrollment(db, enrollment_id)
