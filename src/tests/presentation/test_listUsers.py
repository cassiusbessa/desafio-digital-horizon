from datetime import datetime
import unittest
from unittest.mock import MagicMock
from domain.entities.user import User
from domain.usecases.getAllUsers import GetAllUsers

from presentation.controllers.listUsers import ListUsers
from presentation.controllers.protocols.http import HttpRequest


class TestListUsers(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.getAllUsers = MagicMock(spec=GetAllUsers)
        self.sut = ListUsers(self.getAllUsers)

    async def test_handle_should_return_200_on_success(self):
        request = HttpRequest(headers={"authorization": "valid_token"})
        user = User(
            id="valid_id",
            fullname="valid_name",
            email="valid_email",
            password="valid_password",
            createdAt=datetime.now(),
        )
        self.getAllUsers.list.return_value = [user]
        response = await self.sut.handle(request)
        self.assertEqual(response.statusCode, 200)
        self.assertEqual(response.body, [user.toDict()])

    async def test_handle_should_return_500_if_getAllUsers_raises(self):
        request = HttpRequest()
        self.getAllUsers.list.side_effect = Exception("Error message")
        response = await self.sut.handle(request)
        self.assertEqual(response.statusCode, 500)
        self.assertEqual(response.body, {"error": "Internal server error"})

    async def test_handle_should_return_401_if_no_token_provided(self):
        request = HttpRequest(headers={"authorization": None})
        response = await self.sut.handle(request)
        self.assertEqual(response.statusCode, 401)
        self.assertEqual(response.body, {"error": "Invalid credentials"})
