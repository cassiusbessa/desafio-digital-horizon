from abc import ABC, abstractmethod
from typing import List

from domain.entities.user import User


class GetAllUsers(ABC):
    @abstractmethod
    async def list(self) -> List[User]:
        pass
