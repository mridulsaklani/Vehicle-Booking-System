from app.utils.hash_utils import hash_email
from app.repositories.user_repository import UserRepository
from app.repositories.otp_repository import OTPRepository
from app.utils.custom_exceptions import BadRequestException, UserAlreadyExistException, FailedOTPSend, InternalServerException
from app.config.database_config import client
from fastapi import HTTPException
from app.utils.otp_utils import generate_otp
from app.constants.enums import OTP_TYPE, OTP_EXPIRY, USER_ROLE
from app.validationSchemas.auth_validation import RegisterUser



class AuthService:
    def __init__(self):
        self.repository = UserRepository()
        self.otpRepo = OTPRepository()

    async def register(self, payload: RegisterUser):
        session = await client.start_session()
        try:
           session.start_transaction()
           
           hashed_mail = hash_email(payload.email)

           is_exist = await self.repository.is_user_exist(hashed_mail, session)
           if is_exist:
               raise UserAlreadyExistException()
           data = payload.model_dump()
           data["hash_email"] = hashed_mail
           data["role"] = USER_ROLE.USER

           otp = generate_otp()

           send_otp = await self.otpRepo.create_otp(email=payload.email, otp=otp, type=OTP_TYPE.VERIFICATION, expiry_at=OTP_EXPIRY.TEN_MINUTS.value, session=session)

           if not send_otp:
               raise FailedOTPSend()
           
           create = await self.repository.create(data, session)

           if not create:
               raise HTTPException(status_code=400, detail=f"{payload.name} User account not created")
           
           await session.commit_transaction()
           return create


        except Exception as e:
            await session.abort_transaction()
            print(e)
            raise InternalServerException(detail=str(e))
        
        finally: 
            await session.end_session()