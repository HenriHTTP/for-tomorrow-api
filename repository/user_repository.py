from pymongo.database import Database

from repository.interface_user_repository import InterfaceUserRepository
from entities.user import User


class UserRepository(InterfaceUserRepository):
    def __init__(self, connection, database, collection):
        self.connection = connection
        self.database = database
        self.collection = collection

    async def get_user_by_email(self, email: str):
        pass

    async def get_user_by_username(self, username: str):
        pass

    async def get_user_by_id(self, user_id: any):
        pass

    async def create_user(self, user: User):
        document = {
            "email": user.email,
            "username": user.username,
            "password": user.password,
            "name": user.name,
            "lastname": user.lastname
        }
        self.collection.insert_one(document)
        return document

    async def update_user(self, user: User):
        pass

    async def delete_user(self):
        pass
