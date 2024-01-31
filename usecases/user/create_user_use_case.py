from entities.user import User
from repository.user_repository import UserRepository
from entities.user import User


class CreateUserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def execute(self, user: User):
        try:
            find_email_user = await self.user_repository.get_user_by_email(email=user.email)
            is_used_email = True if len(find_email_user) >= 1 else False
            if not is_used_email:
                await self.user_repository.create_user(user)
                return {
                    "message": "User created successfully",
                    "status_code": 200,
                    "error": "no error on user creation",
                    "success": True
                }
            else:
                return {
                    "message": "email is already used",
                    "status_code": 500,
                    "error": "email is already used, please try again",
                    "success": False
                }
        except Exception as error:
            raise error
