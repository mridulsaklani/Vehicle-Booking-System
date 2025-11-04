from typing import Optional, Dict, Any, List
from motor.motor_asyncio import AsyncIOMotorClientSession
from beanie import PydanticObjectId

class BaseRepository:
    def __init__(self, model):
        self.model = model

    async def create(self, data: dict, session: Optional[AsyncIOMotorClientSession] = None):
        document = self.model(**data)
        await document.insert(session=session)
        return document
    
    async def bulk_create(self, docs: List[Dict[str, Any]], session: Optional[AsyncIOMotorClientSession] = None):
        result = self.model.insert_many(docs, session=session)
        return result
    
    async def find_by_id(self, id: PydanticObjectId, session: Optional[AsyncIOMotorClientSession] = None):
        return await self.model.get(id, session=session)
    
    async def find_one(self, filter = Dict[str, Any], session: Optional[AsyncIOMotorClientSession] = None):
        result = await self.model.find_one(filter, session=session)
        return result
    
    async def get_all(self, page: int = 1, limit: int = 10, filters: Optional[Dict[str, Any]] = None, session: Optional[AsyncIOMotorClientSession] = None):
        skip = (page - 1) * limit
        result =  await self.model.find(filters, session=session)
        return result.skip(skip).limit(limit).to_list()
    
    async def update(self, id: PydanticObjectId, data: Dict[str, Any], session: Optional[AsyncIOMotorClientSession] = None):
        result = await self.model.find_one({"_id": id})
        if not result:
            return None
        await result.set(data, session=session)
        return result


