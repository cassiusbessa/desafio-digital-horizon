from abc import ABC, abstractmethod
from typing import List
from domain.entities.user import User


class UserUseCases(ABC):
    @abstractmethod
    async def addAccount(self, user: User) -> User:
        pass

    async def loadAccountByEmail(self, email: str) -> User:
        pass

    async def getAllAccounts(self) -> List[User]:
        pass
