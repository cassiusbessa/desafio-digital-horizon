import unittest
from unittest.mock import MagicMock
from domain.usecases.authentication import Authentication

from presentation.controllers.protocols.controller import HttpRequest
from presentation.controllers.login import Login


class TestLogin(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.authentication = MagicMock(spec=Authentication)
        self.sut = Login(self.authentication)

    async def test_handle_missing_email(self):
        request = HttpRequest(
            body={
                "password": "any_password",
            }
        )
        response = await self.sut.handle(request)
        self.assertEqual(response.statusCode, 400)
        self.assertEqual(response.body, {"error": "Missing param: email"})

    async def test_handle_missing_password(self):
        request = HttpRequest(
            body={
                "email": "any_email",
            }
        )
        response = await self.sut.handle(request)
        self.assertEqual(response.statusCode, 400)
        self.assertEqual(response.body, {"error": "Missing param: password"})

    async def test_handle_calls_authentication_with_correct_params(self):
        request = HttpRequest(
            body={"email": "any_email", "password": "any_password"}
        )
        await self.sut.handle(request)
        self.authentication.auth.assert_called_once_with(request.body)

    async def test_handle_returns_500_if_authentication_raises(self):
        request = HttpRequest(
            body={"email": "any_email", "password": "any_password"}
        )
        self.authentication.auth.side_effect = Exception("Error")
        response = await self.sut.handle(request)
        self.assertEqual(response.statusCode, 500)
        self.assertEqual(response.body, {"error": "Internal server error"})

    async def test_handle_returns_201_if_authentication_succeeds(self):
        request = HttpRequest(
            body={"email": "valid_email", "password": "valid_password"}
        )
        self.authentication.auth.return_value = {
            "id": "valid_id",
            "fullname": "valid_name",
            "email": "valid_email",
            "password": "valid_password",
            "created_at": "valid_created_at",
            "token": "valid_token",
        }
        response = await self.sut.handle(request)
        self.assertEqual(response.statusCode, 201)
        self.assertEqual(response.body, self.authentication.auth.return_value)
