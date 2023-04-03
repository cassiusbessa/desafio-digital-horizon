import datetime
from unittest import mock
import unittest

import jwt
from domain.entities.user import User
from infra.cryptography.jwtAdapter import JwtAdapter


class TestJwtAdapter(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.secretKey = "secretKey"
        self.user = User(
            id=1,
            fullname="Test User",
            email="testuser@test.com",
            password="testpassword",
            createdAt=datetime.datetime.now(),
        )

    @mock.patch.object(jwt, "encode")
    async def test_should_return_a_token_on_encode(self, mockEncode):
        jwtAdapter = JwtAdapter(secretKey=self.secretKey)
        mockEncode.return_value = "token"
        token = await jwtAdapter.generateToken(self.user)
        self.assertEqual(token, "token")
