from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Boolean, Float, Enum, Table
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base
import enum


class UserRole(str, enum.Enum):
    brand = "brand"
    creator = "creator"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    role = Column(Enum(UserRole), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    brand = relationship("Brand", back_populates="user", uselist=False)
    creator = relationship("Creator", back_populates="user", uselist=False)


class Brand(Base):
    __tablename__ = "brands"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    company_name = Column(String)

    user = relationship("User", back_populates="brand")
    campaigns = relationship("Campaign", back_populates="brand")


class Creator(Base):
    __tablename__ = "creators"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    niche = Column(String)
    engagement_score = Column(Float)

    user = relationship("User", back_populates="creator")
    applications = relationship("Application", back_populates="creator")
    contents = relationship("Content", back_populates="creator")


class Campaign(Base):
    __tablename__ = "campaigns"

    id = Column(Integer, primary_key=True)
    brand_id = Column(Integer, ForeignKey("brands.id"))
    title = Column(String)
    goal = Column(String)
    budget = Column(Float)

    brand = relationship("Brand", back_populates="campaigns")
    tasks = relationship("Task", back_populates="campaign")


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    campaign_id = Column(Integer, ForeignKey("campaigns.id"))
    description = Column(Text)
    platform = Column(String)
    deliverable_type = Column(String)
    engagement_goal = Column(Integer)

    campaign = relationship("Campaign", back_populates="tasks")
    applications = relationship("Application", back_populates="task")
    contents = relationship("Content", back_populates="task")


class ApplicationStatus(str, enum.Enum):
    pending = "pending"
    approved = "approved"
    rejected = "rejected"

class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True)
    creator_id = Column(Integer, ForeignKey("creators.id"))
    task_id = Column(Integer, ForeignKey("tasks.id"))
    status = Column(Enum(ApplicationStatus), default=ApplicationStatus.pending)

    creator = relationship("Creator", back_populates="applications")
    task = relationship("Task", back_populates="applications")


class Content(Base):
    __tablename__ = "contents"

    id = Column(Integer, primary_key=True)
    creator_id = Column(Integer, ForeignKey("creators.id"))
    task_id = Column(Integer, ForeignKey("tasks.id"))
    link = Column(String)
    views = Column(Integer)
    likes = Column(Integer)
    comments = Column(Integer)
    uploaded_at = Column(DateTime(timezone=True), server_default=func.now())

    creator = relationship("Creator", back_populates="contents")
    task = relationship("Task", back_populates="contents")
    payment = relationship("Payment", back_populates="content", uselist=False)


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True)
    content_id = Column(Integer, ForeignKey("contents.id"))
    amount = Column(Float)
    paid = Column(Boolean, default=False)

    content = relationship("Content", back_populates="payment")
