from datetime import datetime

from sqlalchemy import Column, Integer, String, func

from .base import Base


class User(Base):
    id = Column(Integer, primary_key=True)
    email = Column(String(191), unique=True, nullable=False)
    password = Column(String(191), nullable=False)
    created_at = Column(datetime, server_default=func.current_timestamp, nullable=True)

    def __repr__(self):
        return f"User(id={self.id}, email={self.email}, created_at={self.created_at})"
