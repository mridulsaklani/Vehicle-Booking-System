from beanie import Document
from pydantic import EmailStr, Field
from app.constants.enums import OTP_TYPE



class Otp(Document):
    email: EmailStr = Field(...)
    otp: int = Field(..., gt=100000, lt=999999)
    type: OTP_TYPE = Field(...)
    