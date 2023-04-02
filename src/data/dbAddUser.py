from data.protocols.userDbProtocols import AddUserRepository
from domain.entities.user import User
from domain.usecases.addUser import AddUser, AddUserModel


class DbAddUser(AddUser):
    def __init__(self, addUserRepository: AddUserRepository):
        self.addUserRepository = addUserRepository

    async def add(self, userData: AddUserModel) -> User:
        user = await self.addUserRepository.add(userData)
        return user
