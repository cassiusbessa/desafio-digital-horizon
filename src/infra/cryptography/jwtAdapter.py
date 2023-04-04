import datetime
import jwt
from data.protocols.cryptographyProtocols import TokenGenerator
from domain.entities.user import User
from domain.usecases.tokenValidator import TokenValidator


class JwtAdapter(TokenGenerator, TokenValidator):
    def __init__(self, secretKey: str):
        self.secretKey = secretKey

    async def generateToken(self, payload: User) -> str:
        payload.createdAt = datetime.datetime.strftime(
            payload.createdAt, "%Y-%m-%d %H:%M:%S"
        )
        return jwt.encode(payload.toDict(), self.secretKey, algorithm="HS256")

    async def validateToken(self, token: str) -> bool:
        try:
            jwt.decode(token, self.secretKey, algorithms=["HS256"])
            return True
        except Exception:
            return False
