from beanie import Document, Indexed
from pydantic import EmailStr, Field
from datetime import datetime, timedelta, timezone
from typing import Annotated
from app.constants.enums import OTP_TYPE, OTP_EXPIRY


class Otp(Document):
    email: EmailStr = Field(...)
    otp: int = Field(..., gt=100000, lt=999999)
    type: OTP_TYPE = Field(...)
    expires_at: Annotated[datetime, Indexed(expireAfterSeconds=0)] = Field(
        default_factory=lambda: datetime.now(timezone.utc) + timedelta(minutes=OTP_EXPIRY.TEN_MINUTS)
    )