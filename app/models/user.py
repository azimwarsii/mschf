from sqlalchemy import Column, Integer, String, DateTime, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..database import Base
import enum


# User roles
class UserRole(str, enum.Enum):
    brand = "brand"
    creator = "creator"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=True)
    email = Column(String, unique=True, index=True, nullable=True)
    role = Column(Enum(UserRole), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    brand = relationship("Brand", back_populates="user", uselist=False)
    creator = relationship("Creator", back_populates="user", uselist=False)
    oauth_accounts = relationship("OAuthAccount", back_populates="user", cascade="all, delete-orphan")

