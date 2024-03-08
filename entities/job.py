from dataclasses import dataclass


@dataclass
class Job:
    job_title: str
    company: str
    about_company: str
    localization: str
    job_type: str
    job_description: str
    requirements: list[str]
