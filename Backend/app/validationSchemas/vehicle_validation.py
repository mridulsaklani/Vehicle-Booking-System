from pydantic import Field, BaseModel
from beanie import  PydanticObjectId
from datetime import datetime, timezone
from typing import Optional
from app.constants.enums import VEHICLE_TYPE, VEHICLE_BRAND


class VehicleDetail(BaseModel):
    vehicle_number: str = Field(..., min_length=5, max_length=15, description="Vehicle registration number")
    vehicle_type: VEHICLE_TYPE = Field(..., description="Type of vehicle")
    vehicle_brand: VEHICLE_BRAND = Field(..., description="Brand of the vehicle")
    model: Optional[str] = Field(None, description="Vehicle model")
    year: Optional[int] = Field(None, ge=1900, le=2025, description="Manufacturing year")
    seats: Optional[int] = Field(None, ge=1, le=50, description="Number of seats")


class Location(BaseModel):
    lat: float = Field(..., ge=-90, le=90, description="Latitude coordinate")
    lng: float = Field(..., ge=-180, le=180, description="Longitude coordinate")
    address: Optional[str] = Field(None, description="Human readable address")
    city: Optional[str] = Field(None, description="City name")
    state: Optional[str] = Field(None, description="State name")


class Vehicle(BaseModel):
    vehicle_spec: VehicleDetail
    location: Location
    owner_id: PydanticObjectId = Field(..., description="ID of the vehicle driver")
    is_available: bool = Field(default=True, description="Quick availability check")
    hourly_rate: Optional[float] = Field(None, ge=0, description="Hourly rental rate")
    daily_rate: Optional[float] = Field(None, ge=0, description="Daily rental rate")
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))