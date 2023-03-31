from abc import ABC, abstractmethod
from ast import List
from src.domain.entities.user import User


class User_Repository(ABC):
    @abstractmethod
    def create(self, user: User) -> User:
        pass

    @abstractmethod
    def get_all(self) -> List[User]:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> User:
        pass
