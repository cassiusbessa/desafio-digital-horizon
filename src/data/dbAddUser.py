from data.protocols.userDbProtocols import (
    AddUserRepository,
    LoadUserByEmailRepository,
)
from domain.entities.user import User
from domain.usecases.addUser import AddUser, AddUserModel


class DbAddUser(AddUser):
    def __init__(
        self,
        addUserRepository: AddUserRepository,
        loadUserByEmailRepository: LoadUserByEmailRepository,
    ):
        self.addUserRepository = addUserRepository
        self.loadUserByEmailRepository = loadUserByEmailRepository

    async def add(self, userData: AddUserModel) -> User:
        exists = await self.loadUserByEmailRepository.load(userData["email"])
        if exists is not None:
            return None
        user = await self.addUserRepository.add(userData)
        return user
