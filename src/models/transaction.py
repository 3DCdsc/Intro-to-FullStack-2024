"""Data model for table containing transactions."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Optional
from uuid import UUID, uuid4

from sqlalchemy import CheckConstraint, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..db import Base

if TYPE_CHECKING:
    from .destination import Destination
    from .user import User


# For why to use an Enum rather than a Literal type,
# see: https://docs.sqlalchemy.org/en/20/orm/declarative_tables.html#native-enums-and-naming
class TransactionDirection(Enum):
    PAID = "paid"
    RECEIVED = "received"


class Transaction(Base):
    """Fill in the below."""

    __tablename__ = "transaction"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    when_created: Mapped[datetime] = mapped_column(default=func.now())
    when_updated: Mapped[datetime] = mapped_column(
        default=func.now(), onupdate=func.now()
    )
    amount: Mapped[float] = mapped_column(CheckConstraint("amount >= 0"))
    direction: Mapped[TransactionDirection]
    name: Mapped[str]
    description: Mapped[Optional[str]]

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped[User] = relationship(back_populates="transactions")

    destination_id: Mapped[Optional[int]] = mapped_column(ForeignKey("destination.id"))
    destination: Mapped[Optional[Destination]] = relationship(
        back_populates="transactions"
    )
