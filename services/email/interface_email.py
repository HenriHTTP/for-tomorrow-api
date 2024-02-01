from abc import ABC, abstractmethod


class InterfaceEmail(ABC):
    @abstractmethod
    def is_valid(self) -> bool:
        pass
