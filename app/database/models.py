from sqlalchemy import Column, Integer, String, Date
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    birth_date = Column(Date, nullable=False)
    user_class = Column(String(50), nullable=False)