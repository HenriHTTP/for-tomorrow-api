from entities.user import User
from repository.user_repository import UserRepository
from entities.user import User


class CreateUserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def execute(self, user: User):
        try:
            await self.user_repository.create_user(user)
        except Exception as error:
            raise error
