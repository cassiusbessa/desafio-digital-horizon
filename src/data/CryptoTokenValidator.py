from data.protocols.cryptographyProtocols import TokenDecrypter
from domain.usecases.tokenValidator import TokenValidator


class CryptoTokenValidator(TokenValidator):
    def __init__(self, decrypter: TokenDecrypter):
        self.decrypter = decrypter

    async def validateToken(self, token: str) -> bool:
        return await self.decrypter.decryptToken(token)
