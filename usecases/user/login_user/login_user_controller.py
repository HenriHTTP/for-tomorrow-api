from entities.user import User
from usecases.user.login_user.login_user_use_case import LoginUserUseCase
from providers.http_response import HttpResponse
from utils.validation.validation import Validation


class LoginUserController:
    def __init__(self, login_user_use_case: LoginUserUseCase):
        self.__login_user_use_case = login_user_use_case

    async def login_user(self, user: User):
        required_fields = ['email', 'password']
        try:
            Validation.validate_required_fields(required_fields, user)
            login_user = await self.__login_user_use_case.execute(user)
            http_response = HttpResponse(
                success=login_user["success"],
                message=login_user["message"],
                error=login_user["error"],
                status_code=login_user["status_code"],
                token = None
            )
            return http_response
        except Exception as error:
            http_response = HttpResponse(
                success=False,
                message="User not created",
                error=str(error),
                status_code=500,
                token=None
            )
            return http_response
