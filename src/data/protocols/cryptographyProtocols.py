from abc import ABC, abstractmethod

from domain.entities.user import User


class TokenGenerator(ABC):
    @abstractmethod
    def generateToken(self, data: User) -> str:
        pass


class TokenDecrypter(ABC):
    @abstractmethod
    def decryptToken(self, token: str) -> User:
        pass
