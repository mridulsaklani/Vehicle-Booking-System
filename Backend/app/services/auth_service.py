from app.utils.hash_utils import hash_email
from app.repositories.user_repository import UserRepository
from app.utils.custom_exceptions import BadRequestException, UserAlreadyExistException
from app.config.database_config import client


class AuthService:
    def __init__(self):
        self.repository = UserRepository()

    async def register(self, payload: dict):
        session = await client.start_session()
        try:
           session.start_transaction()
           hashed_mail = hash_email(payload.get("email"))

           is_exist = await self.repository.is_user_exist(hashed_mail, session)
           if is_exist:
               raise UserAlreadyExistException()
           
           

        







        except Exception as e:
            await session.abort_transaction()
            print(e)
            raise BadRequestException(detail=str(e))
        
        finally: 
            await session.end_session()