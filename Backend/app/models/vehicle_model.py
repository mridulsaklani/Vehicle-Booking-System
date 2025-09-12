from pydantic import Field, BaseModel
from beanie import Document
from app.constants.enums import TwoWheelerBrand, FourWheelerBrand, VEHICLE_TYPE


class vehicle_detail(BaseModel):
    vehicle_number: str = Field(..., min_length=8)
    vehicle_type: VEHICLE_TYPE = Field(...)
    vehicle_brand: 

class Vehicle(Document):
