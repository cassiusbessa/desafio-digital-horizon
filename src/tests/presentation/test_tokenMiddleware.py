import unittest
from unittest.mock import MagicMock
from domain.usecases.tokenValidator import TokenValidator
from presentation.controllers.protocols.controller import Controller
from presentation.controllers.protocols.http import HttpRequest

from presentation.middleware.tokenMiddleware import TokenMiddleware


class TestTokenMiddleware(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.tokenValidator = MagicMock(spec=TokenValidator)
        self.Controller = MagicMock(spec=Controller)
        self.sut = TokenMiddleware(self.Controller, self.tokenValidator)

    async def test_handle_should_return_401_if_no_token_provided(self):
        request = HttpRequest(headers={"authorization": None})
        response = await self.sut.handle(request)
        self.assertEqual(response.statusCode, 401)
        self.assertEqual(response.body, {"error": "Invalid credentials"})

    async def test_handle_should_return_401_if_token_is_invalid(self):
        request = HttpRequest(headers={"authorization": None})
        self.tokenValidator.validateToken.return_value = False
        response = await self.sut.handle(request)
        self.assertEqual(response.statusCode, 401)
        self.assertEqual(response.body, {"error": "Invalid credentials"})

    async def test_handle_should_call_controller_with_correct_values(self):
        request = HttpRequest(headers={"authorization": "valid_token"})
        self.tokenValidator.validateToken.return_value = True
        await self.sut.handle(request)
        self.Controller.handle.assert_called_with(request)
