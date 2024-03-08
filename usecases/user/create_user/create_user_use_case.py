from repository.user.user_repository import UserRepository
from entities.user import User


class CreateUserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.__user_repository = user_repository

    async def execute(self, user: User) -> dict | ValueError:
        try:
            await self.__email_is_already_used(user)
            await self.__username_is_already_used(user)
            await self.__user_repository.insert_user(user)
            return {
                "message": "User created successfully",
                "status_code": 200,
                "error": None,
                "success": True
            }
        except Exception as error:
            raise ValueError(error)

    async def __email_is_already_used(self, user: User) -> None:
        find_email_user = await self.__user_repository.get_user_by_email(email=user.email)
        is_used_email = True if len(find_email_user) >= 1 else False
        if is_used_email:
            error = "email is already used, please try again"
            raise ValueError(error)

    async def __username_is_already_used(self, user: User) -> None:
        find_username_user = await self.__user_repository.get_user_by_username(username=user.username)
        is_used_username = True if len(find_username_user) >= 1 else False
        if is_used_username:
            error = "username is already used, please try again"
            raise ValueError(error)
