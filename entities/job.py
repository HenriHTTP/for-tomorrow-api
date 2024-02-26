from dataclasses import dataclass


@dataclass
class Job:
    Job_Title: str
    Company: str
    about_company: str
    localization: str
    job_type: str
    job_description: str
    requirements: str
