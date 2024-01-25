from usecases.user.create_user_controller import CreateUserController
from repository.user_repository import UserRepository
from usecases.user.create_user_use_case import CreateUserUseCase

user_repository = UserRepository(1234)
create_user_use_case = CreateUserUseCase(user_repository)
create_user_controller = CreateUserController(create_user_use_case)
