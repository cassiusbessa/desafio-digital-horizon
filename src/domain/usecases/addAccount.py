from abc import ABC, abstractmethod
from domain.entities.user import User


class AddAccount(ABC):
    @abstractmethod
    async def add(self, user: User) -> User:
        pass
