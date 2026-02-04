from database.db import engine, Base
from database import models

def create_database():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    create_database()
