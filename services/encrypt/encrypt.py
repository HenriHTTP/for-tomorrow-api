from hashlib import sha256
from services.encrypt.interface_encrypt import InterfaceEncrypt


class Encrypt(InterfaceEncrypt):
    def __init__(self, data):
        self.data = data

    def encrypt_data(self):
        self.data = sha256(self.data.encode()).hexdigest()
        return self.data

    def validate_data(self, data: str):
        if sha256(data.encode()).hexdigest() == self.data:
            return True
        return False