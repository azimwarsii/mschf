from sqlalchemy.orm import Session
from typing import Optional, Dict, Any
from ..models import User, OAuthAccount
from ..schemas import OAuthLogin, AuthResponse
from .auth_service import AuthService

class OAuthService:
    def __init__(self):
        self.auth_service = AuthService()

    def get_oauth_account(self, db: Session, provider: str, provider_user_id: str) -> Optional[OAuthAccount]:
        return db.query(OAuthAccount).filter(
            OAuthAccount.provider == provider,
            OAuthAccount.provider_user_id == provider_user_id
        ).first()

    def create_oauth_account(self, db: Session, user_id: int, oauth_data: OAuthLogin) -> OAuthAccount:
        oauth_account = OAuthAccount(
            user_id=user_id,
            provider=oauth_data.provider,
            provider_user_id=oauth_data.provider_user_id,
            access_token=oauth_data.access_token,
            refresh_token=oauth_data.refresh_token
        )
        db.add(oauth_account)
        db.commit()
        db.refresh(oauth_account)
        return oauth_account

    def get_or_create_user_from_oauth(self, db: Session, oauth_data: OAuthLogin) -> User:
        # Check if OAuth account already exists
        oauth_account = self.get_oauth_account(db, oauth_data.provider, oauth_data.provider_user_id)
        
        if oauth_account:
            # Update access token
            oauth_account.access_token = oauth_data.access_token
            if oauth_data.refresh_token:
                oauth_account.refresh_token = oauth_data.refresh_token
            db.commit()
            return oauth_account.user

        # Check if user with same email exists
        user = db.query(User).filter(User.email == oauth_data.email).first()
        
        if not user:
            # Create new user
            user = User(
                username=oauth_data.username,
                email=oauth_data.email,
                role="user"
            )
            db.add(user)
            db.commit()
            db.refresh(user)

        # Create OAuth account link
        self.create_oauth_account(db, user.id, oauth_data)
        
        return user

    def process_oauth_login(self, db: Session, oauth_data: OAuthLogin) -> AuthResponse:
        # Validate required fields
        if not all([oauth_data.provider, oauth_data.access_token, oauth_data.provider_user_id]):
            raise ValueError("Missing required OAuth fields")

        # Get or create user
        user = self.get_or_create_user_from_oauth(db, oauth_data)
        
        # Create authentication response
        return self.auth_service.create_auth_response(user)

    def get_user_oauth_accounts(self, db: Session, user_id: int) -> list[OAuthAccount]:
        return db.query(OAuthAccount).filter(OAuthAccount.user_id == user_id).all()

    def disconnect_oauth_account(self, db: Session, user_id: int, provider: str) -> bool:
        oauth_account = db.query(OAuthAccount).filter(
            OAuthAccount.user_id == user_id,
            OAuthAccount.provider == provider
        ).first()
        
        if oauth_account:
            db.delete(oauth_account)
            db.commit()
            return True
        return False
