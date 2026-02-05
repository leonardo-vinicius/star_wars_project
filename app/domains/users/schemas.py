from sqlalchemy import Column, Integer, String, DateTime, Date, Enum as SQLEnum
from sqlalchemy.sql import func
from database.base import Base
from domains.users.models import UserClass


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    name = Column(String(100), nullable=False)
    user_class = Column(SQLEnum(UserClass), nullable=False, default=UserClass.CIVILIAN)
    birth_date = Column(Date, nullable=True)
    hashed_password = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return f"<User(id={self.id}, email={self.email}, name={self.name})>"