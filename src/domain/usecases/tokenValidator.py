from abc import ABC, abstractmethod


class TokenValidator(ABC):
    @abstractmethod
    async def validateToken(self, token: str) -> bool:
        pass
