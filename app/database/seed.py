from datetime import date
from database import engine, SessionLocal
from models import Base, User


def create_tables():
    Base.metadata.create_all(engine)


def seed_users():
    db = SessionLocal()

    users = [
        User(
            name="Luke Skywalker",
            email="luke@rebellion.com",
            birth_date=date(1995, 5, 4),
            user_class="Jedi"
        ),
        User(
            name="Darth Vader",
            email="vader@empire.com",
            birth_date=date(1980, 3, 10),
            user_class="Sith"
        ),
        User(
            name="Leia Organa",
            email="leia@rebellion.com",
            birth_date=date(1992, 10, 21),
            user_class="Rebel"
        ),
    ]

    db.add_all(users)
    db.commit()
    db.close()


if __name__ == "__main__":
    create_tables()
    seed_users()
    print("Banco criado e usuários inseridos com sucesso!")
