from models.user_model import User
from schemas.user_schema import UserAuth

class UserService:
    @staticmethod
    async def create_user(user: UserAuth):
        usuario = User(
            username = user.username,
            email = user.email,
            hash_password = user.password
        )