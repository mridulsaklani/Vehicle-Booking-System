from pydantic import Field, BaseModel
from beanie import Document
from app.constants.enums import TwoWheelerBrand, FourWheelerBrand, VEHICLE_TYPE, VEHICLE_BRAND


class vehicle_detail(BaseModel):
    vehicle_number: str = Field(..., min_length=8)
    vehicle_type: VEHICLE_TYPE = Field(...)
    vehicle_brand: VEHICLE_BRAND = Field(...)


class Vehicle(Document):
    vehicle_spec: vehicle_detail
    