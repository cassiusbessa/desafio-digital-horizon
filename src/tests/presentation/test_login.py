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
