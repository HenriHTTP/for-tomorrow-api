from repository.user_repository import UserRepository
from entities.user import User
from services.encrypt.encrypt import Encrypt


class LoginUserUseCase:
    def __init__(self, user_repository: UserRepository):
        self._user_repository = user_repository

    async def execute(self, user: User):
        try:
            email_user = await self._user_repository.get_user_by_email(user.email)
            print(email_user)
            password_encrypt = Encrypt(user.password)
            user_database = email_user[0]
            print(user_database)
            user_password = user_database["password"]
            print(user_password)
            is_valid_password = password_encrypt.validate_data(user_password)
            print(is_valid_password)
            if is_valid_password:
                return {
                    "message": "login completed successfully",
                    "status_code": 200,
                    "error": None,
                    "success": True
                }

        except Exception as error:
            raise error
