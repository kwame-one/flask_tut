from repositories.user_repository import UserRepository
from requests.login_request import LoginRequest
from requests.register_request import RegisterRequest
from responses.auth_response import AuthResponse
from services.base_service import BaseService


class AuthService(BaseService):
    def __init__(self):
        super().__init__(repository=UserRepository, dto=AuthResponse)

    def register(self, data: RegisterRequest):
        pass

    def login(self, data: LoginRequest):
        pass
