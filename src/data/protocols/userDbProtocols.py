from abc import ABC, abstractmethod
from domain.entities.user import User


class AddUserRepository(ABC):
    @abstractmethod
    async def add(self, name: str, email: str, password: str) -> User:
        pass
