from responses.blog_response import BlogResponse
from .base_service import BaseService
from repositories.blog_repository import BlogRepository


class BlogService(BaseService):

    def __init__(self):
        super().__init__(repository=BlogRepository(), dto=BlogResponse)
