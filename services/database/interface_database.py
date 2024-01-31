from abc import ABC, abstractmethod


class InterfaceDatabase(ABC):
    @abstractmethod
    def client(self):
        pass

    @abstractmethod
    def database(self):
        pass

    @abstractmethod
    def collection(self):
        pass
