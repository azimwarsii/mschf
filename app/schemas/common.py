from pydantic import BaseModel
from typing import Optional, Any

class StatusResponse(BaseModel):
    status: str
    message: Optional[str] = None

class ErrorResponse(BaseModel):
    detail: str
    error_code: Optional[str] = None

class SuccessResponse(BaseModel):
    message: str
    data: Optional[Any] = None
