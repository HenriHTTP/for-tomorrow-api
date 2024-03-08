from entities.job import Job
from usecases.job.create_job.create_job_use_case import CreateJobUseCase
from providers.http_response import HttpResponse
from usecases.job.create_job.create_job_use_case import CreateJobUseCase
from utils.validation.validation import Validation


class CreateJobController:
    def __init__(self, create_job_use_case: CreateJobUseCase):
        self.__create_job_use_case = create_job_use_case

    async def create_job(self, http_request: Job) -> HttpResponse | ValueError:
        required_fields : list[str] = [
            'job_title',
            'company',
            'about_company',
            'localization',
            'job_type',
            'job_description',
            'requirements'
        ]
        try:
            Validation.validate_required_fields(required_fields, http_request)
            job: Job = Job(
                job_title=http_request.job_title,
                company=http_request.company,
                about_company=http_request.about_company,
                localization=http_request.localization,
                job_type=http_request.job_type,
                job_description=http_request.job_description,
                requirements=http_request.requirements
            )
            create_job: dict = await self.__create_job_use_case.execute(job)
            http_response: HttpResponse = HttpResponse(
                success=create_job["success"],
                message=create_job["message"],
                error=create_job["error"],
                status_code=create_job["status_code"],
                token=str(None)
            )
            return http_response
        except Exception as error:
            raise ValueError(error)
