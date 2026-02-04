from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, EmailStr

from domains.auth.service import AuthService
from domains.users.service import UsersService
from domains.users.exceptions import InvalidCredentialsError

router = APIRouter(prefix="/auth", tags=["Auth"])

users_service = UsersService()
auth_service = AuthService(users_service)


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


@router.post("/login")
def login(data: LoginRequest):
    try:
        token = auth_service.login(data.email, data.password)
        return {"access_token": token, "token_type": "bearer"}
    except InvalidCredentialsError:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
