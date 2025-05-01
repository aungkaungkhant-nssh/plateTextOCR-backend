from sqlalchemy import Column, Integer, String,DateTime
from app.database import Base
from sqlalchemy.sql import func

class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, index=True)
    plate_number = Column(String, unique=True)
    punishment_count = Column(Integer, default=0)
    punishment_amount = Column(Integer, default=0)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())