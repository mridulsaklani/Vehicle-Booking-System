from beanie import Document
from pydantic import BaseModel, Field, EmailStr
from app.constants.enums import IndianDistrict, IndianState, USER_ROLE, USER_STATUS
from typing import Optional


class KycDetail(BaseModel):
    aadhaar_number: str = Field(..., pattern=r'^\d{12}$', min_length=12)
    pan_number: str = Field(..., pattern=r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$')
    license_number: Optional[str] 
    driving_experience: Optional[int] = Field(min=0)


class Address(BaseModel):
    address: str = Field(...)
    state: IndianState = Field(...)
    district: IndianDistrict = Field(...)
    pincode: int = Field(..., min_length=6, max_digits=6, examples=123456)

class User(Document):
    name: str = Field(..., min_length=5, max_length=70)
    username: str = Field(..., min_length=3, max_length=20)
    hash_email: str = Field(...) 
    email: EmailStr = Field(...)
    phone: str = Field(..., min_length=10, max_length=10)
    password: str = Field(..., min_length=8)
    role: USER_ROLE = Field(...)
    kyc_detail: KycDetail
    address: Address
    status: USER_STATUS = Field(...)
    
