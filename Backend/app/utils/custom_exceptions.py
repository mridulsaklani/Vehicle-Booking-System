from fastapi import HTTPException, status

class custom_exceptions(HTTPException):
    def __init__(self, status_code: str = None, detail: str = None):
        super().__init__(status_code=status_code or self.status_code, detail=detail or self.status_code)
        self.status_code = status_code
        self.detail = detail


class BadRequestException(custom_exceptions):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "Bad request"

class UnauthorizedException(custom_exceptions):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Unauthorized access"

class ForbiddenException(custom_exceptions):
    status_code = status.HTTP_403_FORBIDDEN
    detail = "Access forbidden"

class NotFoundException(custom_exceptions):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Resource not found"

class ConflictException(custom_exceptions):
    status_code = status.HTTP_409_CONFLICT
    detail = "Resource conflict"

class UnprocessableEntityException(custom_exceptions):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    detail = "Unprocessable entity"

class InternalServerException(custom_exceptions):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = "Internal server error"

class ServiceUnavailableException(custom_exceptions):
    status_code = status.HTTP_503_SERVICE_UNAVAILABLE
    detail = "Service unavailable"

class UserAlreadyExistException(custom_exceptions):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "User Already Exist"
    
