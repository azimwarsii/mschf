from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base


class Creator(Base):
    __tablename__ = "creators"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    niche = Column(String)
    engagement_score = Column(Float)

    user = relationship("User", back_populates="creator")
    applications = relationship("Application", back_populates="creator")
    contents = relationship("Content", back_populates="creator")

