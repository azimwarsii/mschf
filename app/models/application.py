from sqlalchemy import Column, Integer, ForeignKey, Enum
from sqlalchemy.orm import relationship
from ..database import Base
import enum


class ApplicationStatus(str, enum.Enum):
    pending = "pending"
    approved = "approved"
    rejected = "rejected"


class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True)
    creator_id = Column(Integer, ForeignKey("creators.id"), nullable=False)
    task_id = Column(Integer, ForeignKey("tasks.id"), nullable=False)
    status = Column(Enum(ApplicationStatus), default=ApplicationStatus.pending)

    creator = relationship("Creator", back_populates="applications")
    task = relationship("Task", back_populates="applications")

