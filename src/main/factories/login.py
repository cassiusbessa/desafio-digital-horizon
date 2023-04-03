from data.dbAuthLogin import DbAddLogin
from infra.cryptography.jwtAdapter import JwtAdapter
from main.factories.repository import makeUserRepository
from presentation.controllers.login import Login
from presentation.controllers.protocols.controller import Controller


def makeLogin() -> Controller:
    repository = makeUserRepository()
    tokenSecret = "senha_super_secreta"
    tokenGenerator = JwtAdapter(tokenSecret)
    useCase = DbAddLogin(repository, tokenGenerator)
    controller = Login(useCase)
    return controller
