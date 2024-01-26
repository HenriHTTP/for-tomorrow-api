from usecases.user.create_user_controller import CreateUserController
from repository.user_repository import UserRepository
from usecases.user.create_user_use_case import CreateUserUseCase
from services.database import Database
from dotenv import load_dotenv
import os

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

host = os.getenv('HOST')
port = int(os.getenv('PORT'))
database_name = os.getenv('DATABASE_NAME')
collection_name = os.getenv('COLLECTION_NAME')

database = Database(host, port, database_name, collection_name)
user_repository = UserRepository(database.client, database.database, database.collection)
create_user_use_case = CreateUserUseCase(user_repository)
create_user_controller = CreateUserController(create_user_use_case)
