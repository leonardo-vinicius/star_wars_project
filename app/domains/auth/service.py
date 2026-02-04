from domains.users.service import UsersService
from core.security import create_access_token
from domains.users.exceptions import InvalidCredentialsError


class AuthService:

    def __init__(self, users_service: UsersService):
        self.users_service = users_service

    def login(self, email: str, password: str) -> str:
        user = self.users_service.authenticate(email, password)

        token = create_access_token({
            "sub": str(user.id),
            "email": user.email
        })

        return token
