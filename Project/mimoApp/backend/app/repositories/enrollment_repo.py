from sqlalchemy.orm import Session
from models.enrollment import Enrollment
from schemas.enrollment import EnrollmentCreate

def create_enrollment(db: Session, enrollment: EnrollmentCreate):
    new_enrollment = Enrollment(**enrollment.dict())
    db.add(new_enrollment)
    db.commit()
    db.refresh(new_enrollment)
    return new_enrollment

def get_all_enrollments(db: Session):
    return db.query(Enrollment).all()

def get_enrollment_by_id(db: Session, enrollment_id: int):
    return db.query(Enrollment).filter(Enrollment.id == enrollment_id).first()

def update_enrollment(db: Session, enrollment_id: int, enrollment: EnrollmentCreate):
    enrollment_to_update = db.query(Enrollment).filter(Enrollment.id == enrollment_id).first()
    enrollment_to_update.user_id = enrollment.user_id
    enrollment_to_update.course_id = enrollment.course_id
    enrollment_to_update.enrollment_date = enrollment.enrollment_date
    db.commit()
    db.refresh(enrollment_to_update)
    return enrollment_to_update

def delete_enrollment(db: Session, enrollment_id: int):
    enrollment_to_delete = db.query(Enrollment).filter(Enrollment.id == enrollment_id).first()
    db.delete(enrollment_to_delete)
    db.commit()
    return enrollment_to_delete
