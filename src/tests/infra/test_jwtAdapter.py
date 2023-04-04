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

    @mock.patch.object(jwt, "decode")
    async def test_should_return_true_on_decode(self, mockDecode):
        jwtAdapter = JwtAdapter(secretKey=self.secretKey)
        mockDecode.return_value = self.user.toDict()
        isValid = await jwtAdapter.validateToken("token")
        self.assertTrue(isValid)

    @mock.patch.object(jwt, "decode")
    async def test_should_return_false_on_decode(self, mockDecode):
        jwtAdapter = JwtAdapter(secretKey=self.secretKey)
        mockDecode.side_effect = Exception()
        isValid = await jwtAdapter.validateToken("token")
        self.assertFalse(isValid)
