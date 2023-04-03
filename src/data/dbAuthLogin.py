from data.protocols.userDbProtocols import LoadUserByEmailRepository
from domain.usecases.authentication import (
    Authentication,
    LoginModel,
    LoginResponseModel,
)


class DbAddLogin(Authentication):
    def __init__(self, loadUser: LoadUserByEmailRepository, tokenGenerator):
        self.loadUser = loadUser
        self.tokenGenerator = tokenGenerator

    async def auth(self, loginData: LoginModel) -> LoginResponseModel:
        user = await self.loadUser.load(loginData["email"])
        await self.tokenGenerator.generateToken(user)
