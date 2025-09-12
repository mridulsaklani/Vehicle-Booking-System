from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from app.models.user_model import User

import os

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")


async def connect_db():
    client = AsyncIOMotorClient(MONGO_URI)
    database = client[DB_NAME]

    await init_beanie(database=database, document_models=[User])
    print("Database connected successfully!", client.address)
    return client




