from abc import ABC, abstractmethod
from domain.entities.user import User
from typing import TypedDict


class AddUserModel(TypedDict):
    fullname: str
    email: str
    password: str


class AddUser(ABC):
    @abstractmethod
    async def add(self, user: AddUserModel) -> User:
        pass
