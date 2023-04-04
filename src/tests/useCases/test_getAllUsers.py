from datetime import datetime
import unittest
from unittest.mock import MagicMock
from data.dbGetAllUsers import DbGetAllUsers
from data.protocols.userDbProtocols import GetAllUsersRepository

from domain.entities.user import User


class TestDbGetAllUsers(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.user = User(
            id=1,
            fullname="valid_name",
            email="valid_email@email.com",
            password="valid_password",
            createdAt=datetime.now(),
        )
        self.user_list = [self.user]
        self.getAllUsersRepository = MagicMock(spec=GetAllUsersRepository)
        self.getAllUsersRepository.getAll.return_value = self.user_list
        self.sut = DbGetAllUsers(self.getAllUsersRepository)

    async def test_getAllUsers_calls_getAllUsersRepository_with_correct_params(
        self,
    ):
        await self.sut.list()
        self.getAllUsersRepository.getAll.assert_called_once_with()

    async def test_getAllUsers_returns_user_on_success(self):
        user = await self.sut.list()
        self.assertEqual(user, self.user_list)
