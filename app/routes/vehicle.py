from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from app.database import get_db
from app.models.vehicle import Vehicle
from app.schema.vehicle_schema import VehicleCreate, VehicleResponse
from app.services.vehicle_service import create_vehicle

router = APIRouter(prefix="/vehicles", tags=["vehicles"])

@router.post("/", response_model=VehicleResponse)
def create_vehicle_endpoint(vehicle: VehicleCreate, db: Session = Depends(get_db)):
    created_vehicle = create_vehicle(db, vehicle)
    return created_vehicle;