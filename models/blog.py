from datetime import datetime
from typing import Optional

from sqlalchemy import String, Text, func
from sqlalchemy.orm import mapped_column, Mapped

from .base import Base


class Blog(Base):
    __tablename__ = "blogs"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(191))
    content: Mapped[str] = mapped_column(Text())
    created_at: Mapped[Optional[datetime]] = mapped_column(insert_default=func.current_timestamp(), nullable=True)

    def __repr__(self):
        return f"Blog(id={self.id}, name={self.title}, content={self.content}, created_at={self.created_at})"
