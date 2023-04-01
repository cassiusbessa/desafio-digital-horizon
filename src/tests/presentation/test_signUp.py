import unittest
from unittest.mock import MagicMock

from domain.usecases.userUseCases import UserUseCases
from presentation.controllers.protocols.controller import HttpRequest
from presentation.controllers.signUp import SignUp


class TestSignUp(unittest.TestCase):
    def setUp(self):
        self.useCases = MagicMock(spec=UserUseCases)
        self.sut = SignUp(self.useCases)

    async def test_handle_missing_name(self):
        request = HttpRequest(
            body={"email": "any_email@email.com", "password": "any_password"}
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
            body={"name": "any_name", "email": "any_email@email.com"}
        )

        response = await self.sut.handle(request)
        self.assertEqual(response.statusCode, 400)
        self.assertEqual(response.body, {"error": "Missing param: password"})

    async def test_handle_calls_use_case_with_correct_params(self):
        request = HttpRequest(
            body={
                "name": "any_name",
                "email": "any_email@email.com",
                "password": "any_password",
            }
        )

        await self.sut.handle(request)
        self.useCases.addAccount.assert_called_once_with(
            "any_name", "any_email@email.com", "any_password"
        )
