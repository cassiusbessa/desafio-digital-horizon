from abc import ABC, abstractmethod


class TokenValidator(ABC):
    @abstractmethod
    async def validate(self, token: str) -> bool:
        pass
