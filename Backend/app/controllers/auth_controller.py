from app.validationSchemas.auth_validation import RegisterUser
from fastapi import HTTPException

from app.services.auth_service import AuthService
from app.utils.custom_response import SuccessResponse
from app.utils.custom_exceptions import BadRequestException, InternalServerException

class AuthController:
    def __init__(self):
       self.auth_service = AuthService()

    async def register(self, data: RegisterUser):
        try:
           response = await self.auth_service.register(data)
           return SuccessResponse(statusCode=201, message="User created successfully", data=response)

        except Exception:
            raise InternalServerException()
        
