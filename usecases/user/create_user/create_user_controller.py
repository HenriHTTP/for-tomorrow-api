from entities.user import User
from usecases.user.create_user.create_user_use_case import CreateUserUseCase
from providers.http_response import HttpResponse
from services.encrypt.encrypt import Encrypt
from utils.validation.validation import Validation


class CreateUserController:
    def __init__(self, create_user_use_case: CreateUserUseCase):
        self.__create_user_use_case = create_user_use_case

    async def create_user(self, http_request: User) -> HttpResponse | ValueError:
        required_fields: list[str] = ['name', 'lastname', 'username', 'email', 'password']
        try:
            Validation.validate_required_fields(required_fields, http_request)
            Validation.validate_email(http_request)
            Validation.validate_password(http_request)
            password_encrypt: str = self.__encrypt_password(http_request)
            user: User = User(
                username=http_request.username,
                email=http_request.email,
                password=password_encrypt,
                lastname=http_request.lastname,
                name=http_request.name
            )
            create_user = await self.__create_user_use_case.execute(user)
            http_response: HttpResponse = HttpResponse(
                success=create_user["success"],
                message=create_user["message"],
                error=create_user["error"],
                status_code=create_user["status_code"],
                token=str(None)
            )
            return http_response
        except Exception as error:
            raise ValueError(error)

    def __encrypt_password(self, user: User) -> str:
        encrypt: Encrypt = Encrypt(user.password)
        password_encrypt: str = encrypt.encrypt_data()
        return password_encrypt
