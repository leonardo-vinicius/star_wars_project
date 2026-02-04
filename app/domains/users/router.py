from fastapi import APIRouter, HTTPException, status

from .models import UserCreate, UserUpdate, UserResponse
from .service import UsersService
from .exceptions import (
    EmailAlreadyExistsError,
    UserNotFoundError
)

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

users_service = UsersService()


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate):
    try:
        return users_service.create_user(user)
    except EmailAlreadyExistsError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    try:
        return users_service.get_user_by_id(user_id)
    except UserNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserUpdate):
    try:
        return users_service.update_user(user_id, user)
    except UserNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int):
    try:
        users_service.delete_user(user_id)
    except UserNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
