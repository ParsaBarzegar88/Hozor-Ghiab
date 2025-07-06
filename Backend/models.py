from sqlalchemy import Column, Integer, String, DateTime
from database import Base

class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer)
    employee_name = Column(String)
    status = Column(String)  # present, absent, late
    timestamp = Column(DateTime, server_default='now()')
    description = Column(String, nullable=True)