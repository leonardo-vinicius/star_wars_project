from domains.users.service import UsersService
from domains.auth.service import AuthService

users_service = UsersService()
auth_service = AuthService(users_service)