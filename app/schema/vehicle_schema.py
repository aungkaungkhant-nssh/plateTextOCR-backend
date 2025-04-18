from pydantic import BaseModel,Field

class VehicleBase(BaseModel):
    plateNumber: str = Field(..., alias="plate_number")
    class Config:
        populate_by_name = True

class VehicleCreate(VehicleBase):
    pass

class VehicleRead(VehicleBase):
    id: int

    class Config:
        orm_mode = True


class VehicleResponse(BaseModel):
    id: int
    plateNumber: str = Field(..., alias="plate_number")

    class Config:
        from_attributes = True
        populate_by_name = True