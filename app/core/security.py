# from datetime import datetime, timedelta
# from jose import jwt
# from .config import ENV_SECRET_KEY
# from fastapi import Depends, HTTPException, status
# from fastapi.security import OAuth2PasswordBearer
# from jose import jwt, JWTError
# from database.connection import SessionLocal
# from domains.users.schemas import User

# SECRET_KEY = ENV_SECRET_KEY
# ACCESS_TOKEN_EXPIRE_MINUTES = 60
# ALGORITHM = "HS256"

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


# def create_access_token(data: dict) -> str:
#     to_encode = data.copy()
#     expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     to_encode.update({"exp": expire})
#     return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# def get_current_user(token: str = Depends(oauth2_scheme)):
#     try:
#         payload = jwt.decode(token, ENV_SECRET_KEY, algorithms=[ALGORITHM])
#         user_id: str | None = payload.get("sub")

#         if user_id is None:
#             raise HTTPException(status_code=401, detail="Token inválido")

#     except JWTError:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Token inválido ou expirado",
#             headers={"WWW-Authenticate": "Bearer"},
#         )

#     db = SessionLocal()
#     user = db.query(User).filter(User.id == int(user_id)).first()
#     db.close()

#     if not user:
#         raise HTTPException(status_code=401, detail="Usuário não encontrado")

#     return user
