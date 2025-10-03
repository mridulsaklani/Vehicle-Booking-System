from app.utils.hash_utils import hash_email
from app.repositories.user_repository import UserRepository
from app.utils.custom_exceptions import BadRequestException


class AuthService:
    def __init__(self):
        self.repository = UserRepository()

    async def register(payload: dict):
        try:
           hashed_mail = hash_email(payload.get("email"))

           
        







        except Exception as e:
            print(e)
            raise BadRequestException(detail=str(e))