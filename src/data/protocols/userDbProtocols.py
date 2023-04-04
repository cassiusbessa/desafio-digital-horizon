from abc import ABC, abstractmethod
from typing import List
from domain.entities.user import User
from domain.usecases.addUser import AddUserModel


class AddUserRepository(ABC):
    @abstractmethod
    async def add(self, user: AddUserModel) -> User:
        pass


class LoadUserByEmailRepository(ABC):
    @abstractmethod
    async def load(self, email: str) -> User:
        pass


class GetAllUsersRepository(ABC):
    @abstractmethod
    async def getAll(self) -> List[User]:
        pass
