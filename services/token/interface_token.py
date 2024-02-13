from abc import ABC, abstractmethod


class InterfaceToken(ABC):
    @abstractmethod
    def create_token(self):
        pass

    @abstractmethod
    def get_token(self):
        pass

    @abstractmethod
    def validate_token(self, token):
        pass

    @abstractmethod
    def decode_token(self, token):
        pass
