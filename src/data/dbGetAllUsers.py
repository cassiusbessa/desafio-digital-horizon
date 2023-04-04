from typing import List
from data.protocols.userDbProtocols import GetAllUsersRepository
from domain.entities.user import User
from domain.usecases.getAllUsers import GetAllUsers


class DbGetAllUsers(GetAllUsers):
    def __init__(self, getAllUsers: GetAllUsersRepository):
        self.getAllUsers = getAllUsers

    async def list(self) -> List[User]:
        return await self.getAllUsers.getAll()
