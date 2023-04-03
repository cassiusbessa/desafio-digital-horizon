import jwt

from data.protocols.cryptographyProtocols import TokenGenerator
from domain.entities.user import User


class JwtAdapter(TokenGenerator):
    def __init__(self, secretKey: str):
        self.secretKey = secretKey

    async def generateToken(self, payload: User) -> str:
        return jwt.encode(payload.toDict(), self.secretKey, algorithm="HS256")
