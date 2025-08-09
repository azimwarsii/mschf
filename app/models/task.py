from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    campaign_id = Column(Integer, ForeignKey("campaigns.id"), nullable=False)
    description = Column(Text)
    platform = Column(String)
    deliverable_type = Column(String)
    engagement_goal = Column(Integer)

    campaign = relationship("Campaign", back_populates="tasks")
    applications = relationship("Application", back_populates="task")
    contents = relationship("Content", back_populates="task")

