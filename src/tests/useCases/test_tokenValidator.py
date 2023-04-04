import unittest
from unittest.mock import MagicMock
from data.protocols.cryptographyProtocols import TokenDecrypter
from data.CryptoTokenValidator import CryptoTokenValidator


class TestCryptoTokenValidator(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.decrypter = MagicMock(spec=TokenDecrypter)
        self.sut = CryptoTokenValidator(self.decrypter)

    async def test_validate_should_call_decrypter_with_correct_params(self):
        token = "valid_token"
        await self.sut.validate(token)
        self.decrypter.decryptToken.assert_called_once_with(token)

    async def test_validate_should_return_true_if_decrypter_returns_true(self):
        self.decrypter.decryptToken.return_value = True
        result = await self.sut.validate("valid_token")
        self.assertTrue(result)

    async def test_validate_should_return_false_if_decrypter_returns_false(
        self,
    ):
        self.decrypter.decryptToken.return_value = False
        result = await self.sut.validate("valid_token")
        self.assertFalse(result)
