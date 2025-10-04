from base_repository import BaseRepository
from app.models.user_model import User
from motor.motor_asyncio import AsyncIOMotorClientSession
from typing import Optional

class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__(User)

    async def is_user_exist(self, hash_mail: str, session: Optional[AsyncIOMotorClientSession] = None):
        result = await self.find_one({"hash_email": hash_mail}, session)
        return result
        

        