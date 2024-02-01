from services.email.interface_email import InterfaceEmail
from email_validator import validate_email, EmailNotValidError


class Email(InterfaceEmail):
    def __init__(self, email):
        self.__email = email

    def is_valid(self):
        try:
            validate_email(self.__email)
            return True
        except EmailNotValidError:
            return False