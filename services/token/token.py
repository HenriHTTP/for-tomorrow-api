from services.token.interface_token import InterfaceToken
import jwt
import datetime
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

secret_key = os.getenv('SECRET_KEY')


class Token(InterfaceToken):
    def __init__(self, user_id, username):
        self.__token = None
        self.__token_expiration = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        self.__payload = None
        self.__id = user_id
        self.__username = username
        self.__secret = secret_key

    def create_token(self) -> str:
        self.__payload = {
            "id": self.__id,
            "username": self.__username,
            "exp": self.__token_expiration
        }
        self.__token = jwt.encode(self.__payload, self.__secret, algorithm='HS256')
        return self.__token

    def get_token(self) -> str:
        return self.__token

    def validate_token(self, token):
        pass

    def decode_token(self, token):
        pass
