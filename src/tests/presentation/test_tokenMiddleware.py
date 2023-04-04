import unittest
from unittest.mock import MagicMock
from domain.usecases.tokenValidator import TokenValidator
from presentation.controllers.protocols.http import HttpRequest

from presentation.middleware.tokenMiddleware import TokenMiddleware


class TestTokenMiddleware(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.tokenValidator = MagicMock(spec=TokenValidator)
        self.sut = TokenMiddleware(self.tokenValidator)

    async def test_handle_should_return_401_if_no_token_provided(self):
        request = HttpRequest(headers={"authorization": None})
        response = await self.sut.handle(request)
        self.assertEqual(response.statusCode, 401)
        self.assertEqual(response.body, {"error": "Invalid credentials"})
