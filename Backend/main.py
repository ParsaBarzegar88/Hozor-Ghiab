from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency برای دریافت session دیتابیس
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/attendance/", response_model=schemas.AttendanceOut, status_code=status.HTTP_201_CREATED)
def create_attendance(attendance: schemas.AttendanceCreate, db: Session = Depends(get_db)):
    db_attendance = models.Attendance(**attendance.dict())
    db.add(db_attendance)
    db.commit()
    db.refresh(db_attendance)
    return db_attendance

@app.get("/attendance/", response_model=List[schemas.AttendanceOut])
def read_all_attendance(db: Session = Depends(get_db)):
    return db.query(models.Attendance).all()

@app.get("/attendance/{attendance_id}", response_model=schemas.AttendanceOut)
def read_attendance(attendance_id: int, db: Session = Depends(get_db)):
    attendance = db.query(models.Attendance).filter(models.Attendance.id == attendance_id).first()
    if not attendance:
        raise HTTPException(status_code=404, detail="Attendance record not found")
    return attendance

@app.put("/attendance/{attendance_id}", response_model=schemas.AttendanceOut)
def update_attendance(attendance_id: int, attendance: schemas.AttendanceCreate, db: Session = Depends(get_db)):
    db_attendance = db.query(models.Attendance).filter(models.Attendance.id == attendance_id).first()
    if not db_attendance:
        raise HTTPException(status_code=404, detail="Attendance record not found")
    
    for field, value in attendance.dict().items():
        setattr(db_attendance, field, value)
    
    db.commit()
    db.refresh(db_attendance)
    return db_attendance

@app.delete("/attendance/{attendance_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_attendance(attendance_id: int, db: Session = Depends(get_db)):
    attendance = db.query(models.Attendance).filter(models.Attendance.id == attendance_id).first()
    if not attendance:
        raise HTTPException(status_code=404, detail="Attendance record not found")
    
    db.delete(attendance)
    db.commit()
    return