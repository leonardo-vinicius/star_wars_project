# from datetime import datetime
# from typing import Optional
# from pydantic import BaseModel, EmailStr, Field
# from enum import Enum


# class UserClass(str, Enum):
#     JEDI = "Jedi"
#     SITH = "Sith"
#     SMUGGLER = "Smuggler"
#     REBEL = "Rebel"
#     IMPERIAL = "Imperial"
#     CIVILIAN = "Civilian"


# class UserBase(BaseModel):
#     email: EmailStr
#     name: str = Field(..., min_length=2, max_length=100)
#     user_class: UserClass


# class UserCreate(UserBase):
#     password: str = Field(..., min_length=6)


# class UserUpdate(BaseModel):
#     name: Optional[str] = None
#     user_class: Optional[UserClass] = None
#     password: Optional[str] = None


# class UserInDB(UserBase):
#     id: int
#     hashed_password: str
#     created_at: datetime
#     updated_at: Optional[datetime] = None


# class UserResponse(BaseModel):
#     id: int
#     email: EmailStr
#     name: str
#     user_class: UserClass
#     created_at: datetime
