from dataclasses import dataclass


@dataclass
class HttpResponse:
    success: bool
    message: str
    error: str
    status_code: int
    token: str
