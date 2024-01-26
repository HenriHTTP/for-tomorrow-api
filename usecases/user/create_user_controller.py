from entities.user import User
from usecases.user.create_user_use_case import CreateUserUseCase
from providers.http_response import HttpResponse
from services.encrypt import Encrypt


class CreateUserController:
    def __init__(self, create_user_use_case: CreateUserUseCase):
        self.create_user_use_case = create_user_use_case

    async def create_user(self, http_request: User):
        required_fields = ['name', 'lastname', 'username', 'email', 'password']
        null_fields = [field for field in required_fields if getattr(http_request, field) is None]
        if null_fields:
            http_response = HttpResponse(
                success=False,
                message="User not created",
                error=f"{', '.join(null_fields)} is required",
                status_code=500
            )
            return http_response
        try:
            encrypt = Encrypt(http_request.password)
            password_encrypt = encrypt.encrypt_data()

            http_request = User(
                username=http_request.username,
                email=http_request.email,
                password=password_encrypt,
                lastname=http_request.lastname,
                name=http_request.name
            )
            await self.create_user_use_case.execute(http_request)
            http_response = HttpResponse(
                success=True,
                message="User created successfully",
                error="no errors",
                status_code=200
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
