from sqlalchemy import Column, Integer, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True)
    content_id = Column(Integer, ForeignKey("contents.id"), nullable=False)
    amount = Column(Float)
    paid = Column(Boolean, default=False)

    content = relationship("Content", back_populates="payment")

