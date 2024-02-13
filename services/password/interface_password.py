from abc import ABC, abstractmethod


class InterfacePassword(ABC):
    @abstractmethod
    def is_valid_password(self) -> bool:
        pass
