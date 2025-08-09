from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base


class Brand(Base):
    __tablename__ = "brands"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    company_name = Column(String)

    user = relationship("User", back_populates="brand")
    campaigns = relationship("Campaign", back_populates="brand")

