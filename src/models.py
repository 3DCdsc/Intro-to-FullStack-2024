"""Data models for sql database."""

from datetime import datetime
from typing import Optional

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .db import Base


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    created: Mapped[datetime] = mapped_column(default=func.now())
    username: Mapped[str] = mapped_column(unique=True, index=True)
    passwd: Mapped[str]

    is_active: Mapped[bool] = mapped_column(default=True)
    nickname: Mapped[Optional[str]]

    def __repr__(self):
        self.metadata.info
        return f"User(id={self.id!r}, username={self.username!r}, created={self.created!r}, is_active={self.is_active!r}, nickname={self.nickname!r})"
