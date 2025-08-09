from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, UniqueConstraint
from sqlalchemy.orm import relationship
from ..database import Base


class OAuthAccount(Base):
    __tablename__ = "oauth_accounts"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    provider = Column(String, nullable=False)  # e.g., "google", "facebook"
    provider_user_id = Column(String, nullable=False)  # Unique ID from the provider
    access_token = Column(Text)
    refresh_token = Column(Text)
    expires_at = Column(DateTime)

    user = relationship("User", back_populates="oauth_accounts")

    __table_args__ = (
        UniqueConstraint('provider', 'provider_user_id', name='uq_provider_user_id'),
    )

