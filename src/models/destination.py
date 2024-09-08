"""Data model for payment destination."""

from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Optional
from uuid import UUID, uuid4

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..db import Base

if TYPE_CHECKING:
    from .transaction import Transaction


class Destination(Base):
    """Data model of a payment destination."""

    __tablename__ = "destination"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    when_created: Mapped[datetime] = mapped_column(default=func.now())
    name: Mapped[str] = mapped_column(unique=True, index=True)
    description: Mapped[Optional[str]]

    # Deleting the payment destination will delete all associated transactions.
    transactions: Mapped[list[Transaction]] = relationship(
        back_populates="destination", cascade="all, delete-orphan"
    )
