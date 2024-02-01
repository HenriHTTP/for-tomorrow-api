from services.password.interface_password import InterfacePassword
from password_validator import PasswordValidator


class Password(InterfacePassword):
    def __init__(self, password: str):
        self.password = password
        self.validator = PasswordValidator()

    def is_valid_password(self):
        password_valid_shape = (
            self.validator
            .min(8)
            .max(100)
            .has()
            .uppercase()
            .has()
            .lowercase()
            .has()
            .digits()
            .has()
            .no()
            .digits())
        is_valid = password_valid_shape.validate(self.password)
        return is_valid