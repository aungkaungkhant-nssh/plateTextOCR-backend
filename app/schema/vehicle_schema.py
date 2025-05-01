from pydantic import BaseModel, Field
from datetime import datetime

class VehicleBase(BaseModel):
    plate_number: str

    class Config:
        populate_by_name = True
        from_attributes = True

class VehicleCreate(VehicleBase):
    pass

class VehicleResponse(VehicleBase):
    id: int
    punishment_count: int
    punishment_amount: int
    created_at: datetime
    updated_at: datetime

