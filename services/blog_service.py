from abc import ABC

from injector import inject

from responses.blog_response import BlogResponse
from .base_service import BaseService
from repositories.blog_repository import BlogRepository


class BlogService(BaseService, ABC):
    @inject
    def __init__(self, repository: BlogRepository):
        super().__init__(repository=repository)

    def get_dto(self):
        return BlogResponse
