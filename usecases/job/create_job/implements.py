from repository.job.job_repository import JobRepository
from services.database.database import Database
from usecases.job.create_job.create_job_controller import CreateJobController
from usecases.job.create_job.create_job_use_case import CreateJobUseCase
from dotenv import load_dotenv
import os

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

host = os.getenv('HOST')
port = int(os.getenv('PORT'))
database_name = os.getenv('DATABASE_NAME')
collection_name = os.getenv('COLLECTION_JOB')

database = Database(host, port, database_name, collection_name)
job_repository = JobRepository(database.client, database.database, database.collection)
create_job_use_case = CreateJobUseCase(job_repository)
create_job_controller = CreateJobController(create_job_use_case)
