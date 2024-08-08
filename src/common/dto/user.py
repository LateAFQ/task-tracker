from typing import Optional

from src.common.dto.base import DTO


class User(DTO):
    id: int
    login: str
    email: Optional[str] = None
    hashed_password: str


class CreateUser(DTO):
    login: str
    email: Optional[str] = None
    hashed_password: str

