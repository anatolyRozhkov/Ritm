from dataclasses import dataclass


@dataclass
class UserData:
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str
