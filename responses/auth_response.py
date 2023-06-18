from datetime import datetime

from pydantic import BaseModel


class AuthResponse(BaseModel):
    id: int
    email: str
    created_at: datetime
    token: str
