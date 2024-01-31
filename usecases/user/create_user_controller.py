from entities.user import User
from usecases.user.create_user_use_case import CreateUserUseCase
from providers.http_response import HttpResponse
from services.encrypt import Encrypt


class CreateUserController:
    def __init__(self, create_user_use_case: CreateUserUseCase):
        self.create_user_use_case = create_user_use_case

    async def create_user(self, http_request: User):
        try:
            self.__validate_required_fields(http_request)
            password_encrypt = self.__encrypt_password(http_request)
            http_request = User(
                username=http_request.username,
                email=http_request.email,
                password=password_encrypt,
                lastname=http_request.lastname,
                name=http_request.name
            )
            create_user = await self.create_user_use_case.execute(http_request)
            http_response = HttpResponse(
                success=create_user["success"],
                message=create_user["message"],
                error=create_user["error"],
                status_code=create_user["status_code"]
            )
            return http_response
        except Exception as error:
            http_response = HttpResponse(
                success=False,
                message="User not created",
                error=str(error),
                status_code=500
            )
            return http_response

    def __encrypt_password(self, user: User):
        encrypt = Encrypt(user.password)
        password_encrypt = encrypt.encrypt_data()
        return password_encrypt

    def __validate_required_fields(self, http_request: User):
        required_fields = ['name', 'lastname', 'username', 'email', 'password']
        null_fields = [field for field in required_fields if getattr(http_request, field) is None]
        if null_fields:
            error_message = f"{', '.join(null_fields)} is required"
            raise ValueError(error_message)
