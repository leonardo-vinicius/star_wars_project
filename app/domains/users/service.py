from datetime import datetime
from typing import List, Optional
import hashlib
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from domains.users.models import (
    UserCreate,
    UserUpdate,
    UserResponse
)
from domains.users.schemas import User
from domains.users.exceptions import (
    EmailAlreadyExistsError,
    UserNotFoundError,
    InvalidCredentialsError
)

class UsersService:
    def __init__(self, db: Session):
        self.db = db

    def _hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode("utf-8")).hexdigest()

    def _verify_password(self, password: str, hashed: str) -> bool:
        return self._hash_password(password) == hashed

    def _to_response(self, user: User) -> UserResponse:
        return UserResponse(
            id=user.id,
            email=user.email,
            name=user.name,
            user_class=user.user_class,
            created_at=user.created_at
        )

    def create_user(self, data: UserCreate) -> UserResponse:
        existing_user = (
            self.db.query(User)
            .filter(User.email == data.email)
            .first()
        )

        if existing_user:
            raise EmailAlreadyExistsError("E-mail já cadastrado")

        db_user = User(
            email=data.email,
            name=data.name,
            user_class=data.user_class,
            hashed_password=self._hash_password(data.password),
            birth_date=data.birth_date,
            created_at=datetime.utcnow()
        )

        try:
            self.db.add(db_user)
            self.db.commit()
            self.db.refresh(db_user)
        except IntegrityError:
            self.db.rollback()
            raise EmailAlreadyExistsError("E-mail já cadastrado")

        return self._to_response(db_user)

    def authenticate(self, email: str, password: str) -> User:
        user = (
            self.db.query(User)
            .filter(User.email == email)
            .first()
        )

        if not user:
            raise InvalidCredentialsError("Credenciais inválidas")

        if not self._verify_password(password, user.hashed_password):
            raise InvalidCredentialsError("Credenciais inválidas")

        return user

    def get_user_by_id(self, user_id: int) -> UserResponse:
        user = (
            self.db.query(User)
            .filter(User.id == user_id)
            .first()
        )

        if not user:
            raise UserNotFoundError("Usuário não encontrado")

        return self._to_response(user)

    def get_user_by_email(self, email: str) -> Optional[UserResponse]:
        user = (
            self.db.query(User)
            .filter(User.email == email)
            .first()
        )

        if not user:
            return None

        return self._to_response(user)

    def list_users(
        self,
        skip: int = 0,
        limit: int = 100,
        user_class: Optional[str] = None
    ) -> List[UserResponse]:

        query = self.db.query(User)

        if user_class:
            query = query.filter(User.user_class == user_class)

        users = query.offset(skip).limit(limit).all()

        return [self._to_response(user) for user in users]

    def update_user(self, user_id: int, data: UserUpdate) -> UserResponse:
        user = (
            self.db.query(User)
            .filter(User.id == user_id)
            .first()
        )

        if not user:
            raise UserNotFoundError("Usuário não encontrado")

        update_data = data.dict(exclude_unset=True)

        if "password" in update_data:
            user.hashed_password = self._hash_password(
                update_data.pop("password")
            )

        for field, value in update_data.items():
            setattr(user, field, value)

        try:
            self.db.commit()
            self.db.refresh(user)
        except IntegrityError:
            self.db.rollback()
            raise EmailAlreadyExistsError("E-mail já cadastrado")

        return self._to_response(user)

    def delete_user(self, user_id: int) -> None:
        user = (
            self.db.query(User)
            .filter(User.id == user_id)
            .first()
        )

        if not user:
            raise UserNotFoundError("Usuário não encontrado")

        self.db.delete(user)
        self.db.commit()