from data.CryptoTokenValidator import CryptoTokenValidator
from data.dbGetAllUsers import DbGetAllUsers
from infra.cryptography.jwtAdapter import JwtAdapter
from main.factories.repository import makeUserRepository
from presentation.controllers.listUsers import ListUsers
from presentation.controllers.protocols.controller import Controller
from presentation.middleware.tokenMiddleware import TokenMiddleware


def makeListUsers() -> Controller:
    repository = makeUserRepository()
    useCase = DbGetAllUsers(repository)
    controller = ListUsers(useCase)
    tokenSecret = "senha_super_secreta"
    jwtAdapter = JwtAdapter(tokenSecret)
    tokenValidator = CryptoTokenValidator(jwtAdapter)
    protectedListUser = TokenMiddleware(controller, tokenValidator)
    return protectedListUser
