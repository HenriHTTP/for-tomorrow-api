from abc import ABC, abstractmethod
from entities.job import Job


class InterfaceJobRepository(ABC):
    @abstractmethod
    def insert_job(self, job: Job):
        pass

    @abstractmethod
    def delete_job(self, id: str):
        pass
