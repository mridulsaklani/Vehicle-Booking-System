from app.repositories.base_repository import BaseRepository
from app.models.otp_model import Otp
from pydantic import EmailStr
from datetime import datetime, timedelta, timezone
from typing import Any, Optional
from motor.motor_asyncio import AsyncIOMotorClientSession


class OTPRepository(BaseRepository):
    def __init__(self):
        super().__init__(Otp)

    async def create_otp(self, email:EmailStr, otp: int, type: str, expiry_at: int, session: Optional[AsyncIOMotorClientSession] = None):
        expiry = datetime.now(timezone.utc) + timedelta(minutes=expiry_at)
        print("expiry time: ", expiry)
        otp_doc = Otp(
            email=email,
            otp=otp,
            type=type,
            expires_at=expiry
        )
        await self.model.create(otp_doc, session)
