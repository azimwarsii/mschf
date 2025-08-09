from pydantic import BaseModel
from typing import Optional, Dict, Any

class OAuthLogin(BaseModel):
    provider: str
    access_token: str
    provider_user_id: str
    email: str
    username: str
    refresh_token: Optional[str] = None

class AuthResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in: Optional[int] = None
    user_info: Optional[Dict[str, Any]] = None

class OAuthStatus(BaseModel):
    status: str
    available_providers: list[str] = ["google", "facebook", "github"]
