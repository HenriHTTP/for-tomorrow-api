from repository.job.job_repository import JobRepository
from entities.job import Job


class CreateJobUseCase:
    def __init__(self, job_repository: JobRepository):
        self.job_repository = job_repository

    async def execute(self, job: Job) -> dict | ValueError:
        try:
            await self.job_repository.insert_job(job)
            return {
                "message": "job created successfully",
                "status_code": 200,
                "error": None,
                "success": True
            }
        except Exception as error:
            raise ValueError(error)
