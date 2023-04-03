from abc import ABC, abstractmethod
from domain.entities.user import User
from domain.usecases.addUser import AddUserModel


class AddUserRepository(ABC):
    @abstractmethod
    async def add(self, user: AddUserModel) -> User:
        pass
