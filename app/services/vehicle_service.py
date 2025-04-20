from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.models.vehicle import Vehicle
from app.schema.vehicle_schema import  VehicleResponse
from fastapi import  File,UploadFile
from app.helpers.extract_image import extract_plate_number_from_image;




async def create_vehicle(db: Session, file: UploadFile = File(...))-> VehicleResponse:
    plate_number= await extract_plate_number_from_image(file);

    # Optional: check if already exists
    existing = db.query(Vehicle).filter_by(plate_number=plate_number).first()
    if existing:
        return JSONResponse(content={"message": "Plate already exists"}, status_code=200)

    # Save to database
    db_vehicle = Vehicle(plate_number=plate_number)
    db.add(db_vehicle)
    db.commit()
    db.refresh(db_vehicle)

    return db_vehicle
