from sqlalchemy.orm import Session
from typing import Optional, List
from ..models import User
from ..schemas import UserCreate, UserResponse
from .base_service import BaseService

class UserService(BaseService[User, UserCreate, UserCreate]):
    def __init__(self):
        super().__init__(User)

    def get_by_email(self, db: Session, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()

    def get_by_username(self, db: Session, username: str) -> Optional[User]:
        return db.query(User).filter(User.username == username).first()

    def create_user(self, db: Session, user_data: UserCreate) -> User:
        # Check if user already exists
        if self.get_by_email(db, user_data.email):
            raise ValueError("User with this email already exists")
        
        if self.get_by_username(db, user_data.username):
            raise ValueError("Username already taken")

        # Create new user
        db_user = User(
            username=user_data.username,
            email=user_data.email,
            role=user_data.role
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    def get_users_by_role(self, db: Session, role: str) -> List[User]:
        return db.query(User).filter(User.role == role).all()

    def update_user_role(self, db: Session, user_id: int, new_role: str) -> User:
        user = self.get(db, user_id)
        if not user:
            raise ValueError("User not found")
        
        user.role = new_role
        db.commit()
        db.refresh(user)
        return user
