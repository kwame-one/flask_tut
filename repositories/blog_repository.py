from .base_repository import BaseRepository
from models.blog import Blog


class BlogRepository(BaseRepository):
    def __init__(self):
        super().__init__(model=Blog)
