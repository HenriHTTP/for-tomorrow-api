from repository.job.interface_job_repository import InterfaceJobRepository
from entities.job import Job


class JobRepository(InterfaceJobRepository):
    def __init__(self, connection, database, collection) -> None:
        self.connection = connection
        self.database = database
        self.collection = collection

    async def insert_job(self, job: Job) -> dict:
        document = {
            "job_title": job.job_title,
            "company": job.company,
            "about_company": job.about_company,
            "localization": job.localization,
            "job_type": job.job_type,
            "job_description": job.job_description,
            "requirements": job.requirements
        }
        self.collection.insert_one(document)
        return document

    async def delete_job(self, id: str):
        pass
