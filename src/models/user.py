"""Data model for user table."""

from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Optional
from uuid import UUID, uuid4

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..db import Base

if TYPE_CHECKING:
    from .transaction import Transaction


class User(Base):
    """Data model of a user.

    The attributes below correspond to the columns in the `user` table (think spreadsheet).
    """

    __tablename__ = "user"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    when_created: Mapped[datetime] = mapped_column(default=func.now())
    username: Mapped[str] = mapped_column(unique=True, index=True)
    password: Mapped[str]

    is_active: Mapped[bool] = mapped_column(default=True)
    nickname: Mapped[Optional[str]]

    # See: https://docs.sqlalchemy.org/en/20/orm/cascades.html
    # Deleting the user will delete all associated transactions.
    transactions: Mapped[list[Transaction]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )
