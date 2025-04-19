from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schema.vehicle_schema import VehicleResponse
from app.services.vehicle_service import create_vehicle
from fastapi import File,UploadFile



router = APIRouter(prefix="/vehicles", tags=["vehicles"])

@router.post("/")
async def create_vehicle_endpoint(file: UploadFile = File(...), db: Session = Depends(get_db))->VehicleResponse:
    created_vehicle =await create_vehicle(db, file)
    return created_vehicle;