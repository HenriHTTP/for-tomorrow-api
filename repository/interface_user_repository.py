from abc import ABC, abstractmethod
from entities.user import User


class InterfaceUserRepository(ABC):
    @abstractmethod
    async def get_user_by_email(self, email: str):
        pass

    @abstractmethod
    async def get_user_by_username(self, username: str):
        pass

    @abstractmethod
    async def get_user_by_id(self, user_id: any):
        pass

    @abstractmethod
    async def create_user(self, user: User):
        pass

    @abstractmethod
    async def update_user(self, user: User):
        pass

    @abstractmethod
    async def delete_user(self):
        pass
