from pydantic import BaseModel

class VehicleBase(BaseModel):
    plate_number: str

class VehicleCreate(VehicleBase):
    pass

class VehicleRead(VehicleBase):
    id: int

    class Config:
        orm_mode = True