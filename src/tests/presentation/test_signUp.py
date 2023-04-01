import unittest
from unittest.mock import MagicMock

from domain.usecases.addAccount import AddAccount
from presentation.controllers.protocols.controller import HttpRequest
from presentation.controllers.signUp import SignUp


class TestSignUp(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.addAccount = MagicMock(spec=AddAccount)
        self.sut = SignUp(self.addAccount)

    async def test_handle_missing_name(self):
        request = HttpRequest(
            body={
                "email": "any_email@email.com",
                "password": "any_password",
            }
        )

        response = await self.sut.handle(request)
        self.assertEqual(response.statusCode, 400)
        self.assertEqual(response.body, {"error": "Missing param: name"})

    async def test_handle_missing_email(self):
        request = HttpRequest(
            body={"name": "any_name", "password": "any_password"}
        )

        response = await self.sut.handle(request)
        self.assertEqual(response.statusCode, 400)
        self.assertEqual(response.body, {"error": "Missing param: email"})

    async def test_handle_missing_password(self):
        request = HttpRequest(
            body={
                "name": "any_name",
                "email": "any_email@email.com",
            }
        )

        response = await self.sut.handle(request)
        self.assertEqual(response.statusCode, 400)
        self.assertEqual(response.body, {"error": "Missing param: password"})

    async def test_handle_returns_500_if_addAccount_raises(self):
        request = HttpRequest(
            body={
                "name": "any_name",
                "email": "any_email@email.com",
                "password": "any_password",
            }
        )
        self.addAccount.add.side_effect = Exception("Error message")
        response = await self.sut.handle(request)
        self.assertEqual(response.statusCode, 500)
        self.assertEqual(response.body, {"error": "Internal server error"})

    async def test_handle_calls_addAccount_with_correct_params(self):
        request = HttpRequest(
            body={
                "name": "any_name",
                "email": "any_email@email.com",
                "password": "any_password",
            }
        )

        await self.sut.handle(request)
        self.addAccount.add.assert_called_once_with(
            "any_name", "any_email@email.com", "any_password"
        )

    async def test_handle_returns_201_if_succeeds(self):
        request = HttpRequest(
            body={
                "name": "valid_name",
                "email": "valid_email@email.com",
                "password": "valid_password",
            }
        )
        self.addAccount.add.return_value = {
            "id": "valid_id",
            "name": "valid_name",
            "email": "valid_email@email.com",
            "created_at": "valid_created_at",
        }
        response = await self.sut.handle(request)
        self.assertEqual(response.statusCode, 201)
        self.assertEqual(
            response.body,
            {
                "id": "valid_id",
                "name": "valid_name",
                "email": "valid_email@email.com",
                "created_at": "valid_created_at",
            },
        )
