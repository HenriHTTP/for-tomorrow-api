from usecases.user.login_user.login_user_controller import LoginUserController
from repository.user_repository import UserRepository
from usecases.user.login_user.login_user_use_case import LoginUserUseCase
from services.database.database import Database
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
login_user_use_case = LoginUserUseCase(user_repository)
login_user_controller = LoginUserController(login_user_use_case)
