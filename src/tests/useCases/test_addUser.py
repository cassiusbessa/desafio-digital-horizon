import unittest
from unittest.mock import MagicMock
from data.dbAddUser import DbAddUser
from data.protocols.userDbProtocols import AddUserRepository


class TestDbAddUser(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.addUserRepository = MagicMock(spec=AddUserRepository)
        self.sut = DbAddUser(self.addUserRepository)

    async def test_add_calls_addUserRepository_with_correct_params(self):
        user_data = {
            "name": "any_name",
            "email": "any_email",
            "password": "any_password",
        }
        await self.sut.add(user_data)
        self.addUserRepository.add.assert_called_once_with(user_data)
