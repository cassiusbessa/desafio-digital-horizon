from abc import ABC, abstractmethod

from domain.entities.user import User


class TokenGenerator(ABC):
    @abstractmethod
    async def generateToken(self, data: User) -> str:
        pass


class TokenDecrypter(ABC):
    @abstractmethod
    async def decryptToken(self, token: str) -> bool:
        pass
