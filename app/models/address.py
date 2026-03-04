from datetime import UTC, datetime

from sqlalchemy import Column, DateTime, Float, Integer, String

from app.db.base import Base


class Address(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True, index=True)
    street = Column(String, nullable=False)
    city = Column(String, nullable=False)
    country = Column(String, nullable=False)
    latitude = Column(Float, nullable=False, index=True)
    longitude = Column(Float, nullable=False, index=True)
    created_at = Column(
        DateTime, default=lambda: datetime.now(UTC), nullable=False
    )
    updated_at = Column(
        DateTime,
        default=lambda: datetime.now(UTC),
        onupdate=lambda: datetime.now(UTC),
        nullable=False,
    )
