from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class BlogResponse(BaseModel):
    id: int
    title: str
    content: str
    created_at: Optional[datetime]

    class Config:
        orm_mode = True
