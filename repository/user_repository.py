from repository.interface_user_repository import InterfaceUserRepository
from entities.user import User


class UserRepository(InterfaceUserRepository):
    def __init__(self, connection):
        self.connection = connection

    async def get_user_by_email(self, email: str):
        pass

    async def get_user_by_username(self, username: str):
        pass

    async def get_user_by_id(self, user_id: any) -> User:
        pass

    async def create_user(self, user: User) -> dict:
        create_user = {
            "email": user.email,
            "username": user.username,
            "password": user.password,
            "name": user.name,
            "lastname": user.lastname
        }
        print(create_user)
        return create_user

    async def update_user(self, user: User) -> User:
        pass

    async def delete_user(self) -> bool:
        pass
