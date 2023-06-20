from injector import Module, provider, singleton

from repositories.blog_repository import BlogRepository
from services.blog_service import BlogService


class BlogModule(Module):

    @provider
    @singleton
    def provide_blog_repository(self) -> BlogRepository:
        return BlogRepository()

    @provider
    @singleton
    def provide_blog_service(self, repository: BlogRepository) -> BlogService:
        return BlogService(repository=repository)
