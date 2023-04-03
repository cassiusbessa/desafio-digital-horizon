from abc import ABC, abstractmethod
from typing import TypedDict


class LoginModel(TypedDict):
    email: str
    password: str


class LoginResponseModel(TypedDict):
    id: str
    fullname: str
    email: str
    password: str
    created_at: str
    token: str


class Authentication(ABC):
    @abstractmethod
    async def auth(self, credentials: LoginModel) -> LoginResponseModel:
        pass
