import unittest
from unittest.mock import MagicMock
from data.dbAddUser import DbAddUser
from data.protocols.userDbProtocols import (
    AddUserRepository,
    LoadUserByEmailRepository,
)


class TestDbAddUser(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.addUserRepository = MagicMock(spec=AddUserRepository)
        self.loadUserByEmailRepository = MagicMock(
            spec=LoadUserByEmailRepository
        )
        self.sut = DbAddUser(
            self.addUserRepository, self.loadUserByEmailRepository
        )

    async def test_add_calls_addUserRepository_with_correct_params(self):
        user_data = {
            "fullname": "any_name",
            "email": "any_email",
            "password": "any_password",
        }
        self.loadUserByEmailRepository.load.return_value = None
        await self.sut.add(user_data)
        self.addUserRepository.add.assert_called_once_with(user_data)

    async def test_add_returns_user_on_success(self):
        user_data = {
            "fullname": "valid_name",
            "email": "valid_email",
            "password": "valid_password",
        }
        self.loadUserByEmailRepository.load.return_value = None
        self.addUserRepository.add.return_value = user_data
        user = await self.sut.add(user_data)
        self.assertEqual(user, user_data)

    async def test_should_call_loadUserByEmailRepository_with_correct_email(
        self,
    ):
        user_data = {
            "id": "any_id",
            "fullname": "any_name",
            "email": "any_email",
            "password": "any_password",
            "created_at": "any_created_at",
        }
        await self.sut.add(user_data)
        self.loadUserByEmailRepository.load.assert_called_with(
            user_data["email"]
        )

    async def test_should_return_none_load_not_returns_none(
        self,
    ):
        user_data = {
            "id": "any_id",
            "fullname": "any_name",
            "email": "any_email",
            "password": "any_password",
            "created_at": "any_created_at",
        }
        self.loadUserByEmailRepository.load.return_value = True
        user = await self.sut.add(user_data)
        self.assertIsNone(user)
