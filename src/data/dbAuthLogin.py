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
        if user is None:
            return None
        token = await self.tokenGenerator.generateToken(user)
        return {
            "token": token,
            "id": user.id,
            "fullname": user.fullname,
            "email": user.email,
            "createdAt": user.createdAt,
            "password": user.password,
        }
