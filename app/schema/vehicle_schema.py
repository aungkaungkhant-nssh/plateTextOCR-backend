from pydantic import BaseModel, Field

class VehicleBase(BaseModel):
    plate_number: str

    class Config:
        populate_by_name = True
        from_attributes = True

class VehicleCreate(VehicleBase):
    pass

class VehicleResponse(VehicleBase):
    id: int

