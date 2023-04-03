import unittest
from unittest.mock import MagicMock
from data.dbAuthLogin import DbAddLogin
from data.protocols.cryptographyProtocols import TokenGenerator
from data.protocols.userDbProtocols import LoadUserByEmailRepository


class TestAuthLogin(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.loadUserByEmailRepository = MagicMock(
            spec=LoadUserByEmailRepository
        )
        self.tokenGenerator = MagicMock(spec=TokenGenerator)
        self.sut = DbAddLogin(
            self.loadUserByEmailRepository, self.tokenGenerator
        )

    async def test_should_call_loadUserByEmailRepository_with_correct_email(
        self,
    ):
        credentials = {
            "email": "any_email@email.com",
            "password": "any_password",
        }
        await self.sut.auth(credentials)
        self.loadUserByEmailRepository.load.assert_called_with(
            credentials["email"]
        )

    async def test_should_call_tokenGenerator_with_correct_data(self):
        credentials = {
            "email": "any_email@email.com",
            "password": "any_password",
        }
        await self.sut.auth(credentials)
        self.tokenGenerator.generateToken.assert_called_with(
            await self.loadUserByEmailRepository.load(credentials["email"])
        )
