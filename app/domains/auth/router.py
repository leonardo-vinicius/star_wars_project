# from fastapi import APIRouter, Request, HTTPException
# from pydantic import BaseModel, EmailStr

# from domains.users.exceptions import InvalidCredentialsError

# router = APIRouter(prefix="/auth", tags=["Auth"])


# class LoginRequest(BaseModel):
#     email: EmailStr
#     password: str


# @router.post("/login")
# def login(request: Request, data: LoginRequest):
#     auth_service = request.app.state.auth_service
#     try:
#         token = auth_service.login(data.email, data.password)
#         return {"access_token": token, "token_type": "bearer"}
#     except InvalidCredentialsError:
#         raise HTTPException(status_code=401, detail="Credenciais inválidas")
