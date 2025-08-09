from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..database import Base


class Content(Base):
    __tablename__ = "contents"

    id = Column(Integer, primary_key=True)
    creator_id = Column(Integer, ForeignKey("creators.id"), nullable=False)
    task_id = Column(Integer, ForeignKey("tasks.id"), nullable=False)
    link = Column(String)
    views = Column(Integer)
    likes = Column(Integer)
    comments = Column(Integer)
    uploaded_at = Column(DateTime(timezone=True), server_default=func.now())

    creator = relationship("Creator", back_populates="contents")
    task = relationship("Task", back_populates="contents")
    payment = relationship("Payment", back_populates="content", uselist=False)

