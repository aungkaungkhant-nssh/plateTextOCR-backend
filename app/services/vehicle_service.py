from sqlalchemy.orm import Session
from app.models.vehicle import Vehicle
from app.schema.vehicle_schema import VehicleCreate, VehicleResponse

def create_vehicle(db: Session, vehicle_data: VehicleCreate) -> Vehicle:
    db_vehicle = Vehicle(plate_number=vehicle_data.plate_number)
    db.add(db_vehicle)
    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle