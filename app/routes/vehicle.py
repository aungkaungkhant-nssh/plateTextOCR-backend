from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.vehicle import Vehicle
from app.schema.vehicle_schema import VehicleCreate, VehicleResponse

router = APIRouter(prefix="/vehicles", tags=["vehicles"])

@router.post("/", response_model=VehicleResponse)
def create_vehicle(vehicle: VehicleCreate, db: Session = Depends(get_db)):
    db_vehicle = Vehicle(plate_number=vehicle.plateNumber)
    db.add(db_vehicle)
    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle





