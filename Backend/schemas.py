from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AttendanceCreate(BaseModel):
    employee_id: int
    employee_name: str
    status: str
    description: Optional[str] = None

class AttendanceOut(AttendanceCreate):
    id: int
    timestamp: datetime