from abc import ABC, abstractmethod


class InterfaceEncrypt(ABC):
    @abstractmethod
    def encrypt_data(self):
        pass

    def decrypt_data(self, data: str):
        pass

    def validate_data(self, data: str):
        pass
