# from fastapi import APIRouter, Depends, HTTPException, status
# from sqlalchemy.orm import Session
# from typing import List, Optional

# from core.security import get_current_user
# from database.connection import get_db
# from domains.users.service import UsersService
# from domains.users.models import (
#     UserCreate,
#     UserUpdate,
#     UserResponse
# )
# from domains.users.exceptions import (
#     EmailAlreadyExistsError,
#     UserNotFoundError
# )

# router = APIRouter(
#     prefix="/users",
#     tags=["Users"]
# )


# def get_users_service(db: Session = Depends(get_db)) -> UsersService:
#     return UsersService(db)


# @router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
# def create_user(
#     user_data: UserCreate,
#     service: UsersService = Depends(get_users_service)
# ):
#     try:
#         return service.create_user(user_data)
#     except EmailAlreadyExistsError as e:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail=str(e)
#         )


# @router.get("/{user_id}", response_model=UserResponse)
# def get_user(
#     user_id: int,
#     service: UsersService = Depends(get_users_service)
# ):
#     try:
#         return service.get_user_by_id(user_id)
#     except UserNotFoundError as e:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=str(e)
#         )


# @router.get("/", response_model=List[UserResponse])
# def list_users(
#     skip: int = 0,
#     limit: int = 100,
#     user_class: Optional[str] = None,
#     current_user=Depends(get_current_user),  # 🔐 AQUI
#     service: UsersService = Depends(get_users_service)
# ):
#     return service.list_users(skip, limit, user_class)


# @router.put("/{user_id}", response_model=UserResponse)
# def update_user(
#     user_id: int,
#     user_data: UserUpdate,
#     current_user=Depends(get_current_user),  # 🔐 AQUI
#     service: UsersService = Depends(get_users_service)
# ):
#     try:
#         return service.update_user(user_id, user_data)
#     except UserNotFoundError as e:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=str(e)
#         )
#     except EmailAlreadyExistsError as e:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail=str(e)
#         )


# @router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_user(
#     user_id: int,
#     current_user=Depends(get_current_user),
#     service: UsersService = Depends(get_users_service)
# ):
#     try:
#         service.delete_user(user_id)
#     except UserNotFoundError as e:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=str(e)
#         )