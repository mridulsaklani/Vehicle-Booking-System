from fastapi import APIRouter
from app.validationSchemas.auth_validation import RegisterUser
from app.controllers.auth_controller import AuthController

auth_controller = AuthController()

router = APIRouter()

@router.post('/register')
async def register(data: RegisterUser):
    result = await auth_controller.register(data)
    return result