from abc import ABC, abstractmethod
from typing import TypedDict


class LoginModel(TypedDict):
    email: str
    password: str


class Authentication(ABC):
    @abstractmethod
    async def auth(self, credentials: LoginModel) -> str:
        pass
