# from datetime import date
# from .service import UsersService
# from .models import UserCreate
# from .models import UserClass


# def load_users_seed(service: UsersService) -> None:
#     users = [
#         UserCreate(
#             name="Luke Skywalker",
#             birth_date=date(1995, 5, 4),
#             email="luke@rebellion.com",
#             password="ForceStrong123",
#             user_class=UserClass.JEDI,
#             favorite_character="Luke Skywalker"
#         ),
#         UserCreate(
#             name="Darth Vader",
#             birth_date=date(1980, 3, 10),
#             email="vader@empire.com",
#             password="DarkSide123",
#             user_class=UserClass.SITH,
#             favorite_character="Darth Vader"
#         ),
#         UserCreate(
#             name="Han Solo",
#             birth_date=date(1988, 7, 13),
#             email="han@falcon.com",
#             password="FalconFast123",
#             user_class=UserClass.SMUGGLER,
#             favorite_character="Han Solo"
#         ),
#         UserCreate(
#             name="Leia Organa",
#             birth_date=date(1992, 10, 21),
#             email="leia@rebellion.com",
#             password="HopeStrong123",
#             user_class=UserClass.REBEL,
#             favorite_character="Princess Leia"
#         ),
#         UserCreate(
#             name="Boba Fett",
#             birth_date=date(1985, 12, 1),
#             email="boba@bounty.com",
#             password="HunterElite123",
#             user_class=UserClass.BOUNTY_HUNTER,
#             favorite_character="Boba Fett"
#         ),
#     ]

#     for user in users:
#         service.create_user(user)
