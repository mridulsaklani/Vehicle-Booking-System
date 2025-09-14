from pydantic import BaseModel, Field, EmailStr, field_validator
from app.constants.enums import USER_ROLE, IndianState, IndianDistrict
import re
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

class RegisterUser(BaseModel):
    name: str = Field(..., min_length=5, max_length=100)
    username: str = Field(..., min_length=3, max_length=20)
    email: EmailStr = Field(...)
    phone: str = Field(..., min_length=10, max_length=10)
    password: str = Field(..., min_length=8)
    role: USER_ROLE
    kyc_detail: KycDetail
    address: Address

    @field_validator('phone')
    @classmethod
    def validate_phone(cls, v):
       
        if not v.isdigit():
            raise ValueError('Phone number must contain only digits')
        return v

    @field_validator('username')
    @classmethod
    def validate_username(cls, v):
       
        if not re.match(r'^[a-zA-Z0-9_]+$', v):
            raise ValueError('Username can only contain letters, numbers, and underscores')
        return v

    @field_validator('password')
    @classmethod
    def validate_password(cls, v):
       
        if not re.search(r'[A-Z]', v):
            raise ValueError('Password must contain at least one uppercase letter')
        if not re.search(r'[a-z]', v):
            raise ValueError('Password must contain at least one lowercase letter')  
        if not re.search(r'\d', v):
            raise ValueError('Password must contain at least one digit')
        return v

