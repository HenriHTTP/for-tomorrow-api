from hashlib import sha256
from services.encrypt.interface_encrypt import InterfaceEncrypt


class Encrypt(InterfaceEncrypt):
    def __init__(self, data):
        self.data = data

    def encrypt_data(self) -> str:
        self.data: str = sha256(self.data.encode()).hexdigest()
        return self.data

    def validate_data(self, data: str) -> bool:
        encrypted_data: str = sha256(self.data.encode()).hexdigest()
        is_valid_encrypted_data: bool = data == encrypted_data
        if is_valid_encrypted_data:
            return True
        return False
