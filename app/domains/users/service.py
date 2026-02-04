from datetime import datetime
from typing import Dict
import hashlib

from .models import (
    UserCreate,
    UserUpdate,
    UserInDB,
    UserResponse
)
from .exceptions import (
    EmailAlreadyExistsError,
    UserNotFoundError,
    InvalidCredentialsError
)

class UsersService:
    def __init__(self):
        self._users: Dict[int, UserInDB] = {}
        self._id_counter = 1

    def _hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode("utf-8")).hexdigest()

    def _verify_password(self, password: str, hashed: str) -> bool:
        return self._hash_password(password) == hashed

    def _to_response(self, user: UserInDB) -> UserResponse:
        return UserResponse(
            id=user.id,
            email=user.email,
            name=user.name,
            user_class=user.user_class,
            created_at=user.created_at
        )

    def create_user(self, data: UserCreate) -> UserResponse:
        if any(u.email == data.email for u in self._users.values()):
            raise EmailAlreadyExistsError("E-mail já cadastrado")

        user = UserInDB(
            id=self._id_counter,
            email=data.email,
            name=data.name,
            user_class=data.user_class,
            hashed_password=self._hash_password(data.password),
            created_at=datetime.utcnow(),
            updated_at=None
        )

        self._users[self._id_counter] = user
        self._id_counter += 1

        return self._to_response(user)

    def authenticate(self, email: str, password: str) -> UserInDB:
        for user in self._users.values():
            if user.email == email:
                if self._verify_password(password, user.hashed_password):
                    return user
                break

        raise InvalidCredentialsError("Credenciais inválidas")

    def get_user_by_id(self, user_id: int) -> UserResponse:
        user = self._users.get(user_id)
        if not user:
            raise UserNotFoundError("Usuário não encontrado")

        return self._to_response(user)

    def update_user(self, user_id: int, data: UserUpdate) -> UserResponse:
        user = self._users.get(user_id)
        if not user:
            raise UserNotFoundError("Usuário não encontrado")

        update_data = data.dict(exclude_unset=True)

        if "password" in update_data:
            user.hashed_password = self._hash_password(update_data.pop("password"))

        for field, value in update_data.items():
            setattr(user, field, value)

        user.updated_at = datetime.utcnow()

        return self._to_response(user)

    def delete_user(self, user_id: int) -> None:
        if user_id not in self._users:
            raise UserNotFoundError("Usuário não encontrado")

        del self._users[user_id]
