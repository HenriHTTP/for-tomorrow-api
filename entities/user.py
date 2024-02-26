from dataclasses import dataclass


@dataclass
class User:
    name: str
    lastname: str
    username: str
    email: str
    password: str
