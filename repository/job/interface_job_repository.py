from abc import ABC, abstractmethod
from entities.job import Job


class InterfaceJobRepository(ABC):
    @abstractmethod
    async def insert_job(self, job: Job) -> dict:
        pass

    @abstractmethod
    async def delete_job(self, id: str):
        pass
