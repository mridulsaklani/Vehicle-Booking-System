from beanie import Document, before_event, Insert, Replace, Update
from pydantic import BaseModel, Field, EmailStr
from app.constants.enums import IndianDistrict, IndianState, USER_ROLE, USER_STATUS
from typing import Optional
from datetime import datetime
from app.utils.hash_utils import hash_pass, validate_pass
from app.utils.encryption_utils import incrept_email, decrept_email, incrept_data, decrept_data


class KycDetail(BaseModel):
    aadhaar_number: str = Field(..., pattern=r'^\d{12}$', min_length=12)
    pan_number: str = Field(..., pattern=r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$')
    license_number: Optional[str] 
    driving_experience: Optional[int] = Field(min=0)


class Address(BaseModel):
    address: str = Field(...)
    state: IndianState = Field(...)
    district: IndianDistrict = Field(...)
    pincode: int = Field(..., gt=100000, lt=999999, examples=[123456])

class User(Document):
    name: str = Field(..., min_length=5, max_length=70)
    username: str = Field(..., min_length=3, max_length=20)
    hash_email: str = Field(...) 
    email: EmailStr = Field(...)
    email_verified: bool = Field(default=False, description="Email verification status")
    phone: str = Field(..., min_length=10, max_length=10)
    password: str = Field(..., min_length=8)
    role: USER_ROLE = Field(...)
    kyc_detail: Optional[KycDetail]
    address: Address
    email_verified_at: Optional[datetime] = Field(None, description="Email verification timestamp")


    def verify_password(self, password:str)->bool:
        return validate_pass(password, self.password)


    @before_event([Insert, Replace])
    def hash_password(self):
        if not self.password.startswith("$2b$"):
            self.password = hash_pass(self.password)

    def _is_encrypted(self, value: str) -> bool:
        try:
            decrept_email(value)
            return True
        except Exception:
            return False

    @before_event([Insert, Replace])
    def encrypt_email(self):
        if self._is_encrypted(self.email):
            return
        self.email = incrept_email(self.email)

    def decrypt_email(self):
        return decrept_email(self.email)
    
    @before_event([Insert, Replace])
    def encrypt_kyc(self):
        if self.kyc_detail:
            if not self._is_encrypted(self.kyc_detail.aadhaar_number):
                self.kyc_detail.aadhaar_number = incrept_data(self.kyc_detail.aadhaar_number)
            
            if not self._is_encrypted(self.kyc_detail.pan_number):
                self.kyc_detail.pan_number= incrept_data(self.kyc_detail.pan_number)

            if self.kyc_detail.license_number and  not self._is_encrypted(self.kyc_detail.license_number):
                self.kyc_detail.license_number = incrept_data(self.kyc_detail.license_number)

    def decrypt_kyc(self):
        if not self.kyc_detail:
            return None
        
        if self.kyc_detail:
            return KycDetail(
               aadhaar_number = decrept_data(self.kyc_detail.aadhaar_number),
               pan_number = decrept_data(self.kyc_detail.pan_number),
               license_number = decrept_data(self.kyc_detail.license_number) if self.kyc_detail.license_number else None,
               driving_experience= self.kyc_detail.driving_experience if self.kyc_detail.driving_experience else None
            )


