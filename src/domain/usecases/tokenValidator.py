from abc import ABC, abstractmethod


class TokenValidator(ABC):
    @abstractmethod
    def validate(self, token: str) -> bool:
        pass
