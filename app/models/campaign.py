from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base


class Campaign(Base):
    __tablename__ = "campaigns"

    id = Column(Integer, primary_key=True)
    brand_id = Column(Integer, ForeignKey("brands.id"), nullable=False)
    title = Column(String)
    goal = Column(String)
    budget = Column(Float)

    brand = relationship("Brand", back_populates="campaigns")
    tasks = relationship("Task", back_populates="campaign")

