import unittest
from unittest.mock import MagicMock

from domain.usecases.userUseCases import UserUseCases
from presentation.controllers.protocols.controller import HttpRequest
from presentation.controllers.signUp import SignUp


class TestSignUp(unittest.TestCase):
    def setUp(self):
        self.useCases = MagicMock(spec=UserUseCases)
        self.controller = SignUp(self.useCases)

    def test_handle_missing_name(self):
        request = HttpRequest(
            body={"email": "any_email@email.com", "password": "any_password"}
        )

        response = self.controller.handle(request)
        self.assertEqual(response.statusCode, 400)
        self.assertEqual(response.body, {"error": "Missing param: name"})

    def test_handle_missing_email(self):
        request = HttpRequest(
            body={"name": "any_name", "password": "any_password"}
        )

        response = self.controller.handle(request)
        self.assertEqual(response.statusCode, 400)
        self.assertEqual(response.body, {"error": "Missing param: email"})

    def test_handle_missing_password(self):
        request = HttpRequest(
            body={"name": "any_name", "email": "any_email@email.com"}
        )

        response = self.controller.handle(request)
        self.assertEqual(response.statusCode, 400)
        self.assertEqual(response.body, {"error": "Missing param: password"})
