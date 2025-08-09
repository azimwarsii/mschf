from sqlalchemy.orm import Session
from typing import Optional, Dict, Any
from jose import jwt
from datetime import datetime, timedelta
import os
from ..models import User
from ..schemas import AuthResponse

class AuthService:
    def __init__(self):
        self.secret_key = os.getenv("JWT_SECRET", "supersecret")
        self.algorithm = "HS256"
        self.access_token_expire_minutes = 60

    def create_access_token(self, data: Dict[str, Any]) -> str:
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=self.access_token_expire_minutes)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, self.secret_key, algorithm=self.algorithm)
        return encoded_jwt

    def verify_token(self, token: str) -> Optional[Dict[str, Any]]:
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            return payload
        except jwt.JWTError:
            return None

    def authenticate_user(self, db: Session, email: str, password: str) -> Optional[User]:
        # This is a simplified version - in real apps, you'd hash passwords
        user = db.query(User).filter(User.email == email).first()
        if user and password == "password":  # Replace with proper password verification
            return user
        return None

    def get_current_user(self, db: Session, token: str) -> Optional[User]:
        payload = self.verify_token(token)
        if payload is None:
            return None
        
        user_id = payload.get("sub")
        if user_id is None:
            return None
        
        user = db.query(User).filter(User.id == int(user_id)).first()
        return user

    def create_auth_response(self, user: User) -> AuthResponse:
        access_token = self.create_access_token(data={"sub": str(user.id)})
        return AuthResponse(
            access_token=access_token,
            token_type="bearer",
            expires_in=self.access_token_expire_minutes * 60,
            user_info={
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "role": user.role
            }
        )
