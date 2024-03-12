from services.email.email import Email
from services.password.password import Password
from entities.user import User


class Validation:
    @staticmethod
    def validate_required_fields(required_fields: list, http_request: User or any) -> None:
        null_fields = [field for field in required_fields if getattr(http_request, field) is None]
        if null_fields:
            error_message = f"{', '.join(null_fields)} is required, please check the details"
            raise ValueError(error_message)

    @staticmethod
    def validate_email(http_request: User) -> None:
        email = Email(http_request.email)
        if not email.is_valid():
            error_message = f"{http_request.email} is not a valid email, please check the details"
            raise ValueError(error_message)

    @staticmethod
    def validate_password(http_request: User) -> None:
        password = http_request.password
        validate_password = Password(password)
        if not validate_password.is_valid_password():
            error_message = ('invalid password, the password must not contain spaces, '
                             'must contain digits, uppercase and lowercase letters')
            raise ValueError(error_message)
