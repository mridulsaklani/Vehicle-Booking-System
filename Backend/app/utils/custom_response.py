from pydantic import BaseModel, Field
from typing import Any, Optional


class SuccessResponse(BaseModel):
    success: bool = Field(default=True)
    statusCode: int
    message: str
    data: Optional[Any] = None