import unittest
from unittest.mock import MagicMock
from data.dbAuthLogin import DbAddLogin
from data.protocols.cryptographyProtocols import TokenGenerator
from data.protocols.userDbProtocols import LoadUserByEmailRepository
from domain.entities.user import User


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

    async def test_should_return_login_response_model(self):
        credentials = {
            "email": "any_email@email.com",
            "password": "any_password",
        }
        self.loadUserByEmailRepository.load.return_value = User(
            id="valid_id",
            fullname="valid_name",
            email="valid_email@email.com",
            password="valid_password",
            createdAt="valid_created_at",
        )
        self.tokenGenerator.generateToken.return_value = "valid_token"
        login_response_model = await self.sut.auth(credentials)
        self.assertEqual(
            login_response_model,
            {
                "token": "valid_token",
                "id": "valid_id",
                "fullname": "valid_name",
                "email": "valid_email@email.com",
                "createdAt": "valid_created_at",
                "password": "valid_password",
            },
        )

    async def test_should_return_none_loadUserByEmailRepository_returns_none(
        self,
    ):
        credentials = {
            "email": "invalid_email@email.com",
            "password": "any_password",
        }
        self.loadUserByEmailRepository.load.return_value = None
        login_response_model = await self.sut.auth(credentials)
        self.assertEqual(login_response_model, None)
