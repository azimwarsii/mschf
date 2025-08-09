from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..dependencies import get_db
from ..models import User
from ..schemas import UserCreate, UserResponse
from ..services import UserService

router = APIRouter()
user_service = UserService()

@router.post("/users/", response_model=UserResponse)
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    try:
        user = user_service.create_user(db, user_data)
        return user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/users/", response_model=list[UserResponse])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = user_service.get_multi(db, skip=skip, limit=limit)
    return users

@router.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = user_service.get(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
