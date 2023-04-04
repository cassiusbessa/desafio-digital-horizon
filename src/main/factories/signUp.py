from data.dbAddUser import DbAddUser
from main.factories.repository import makeUserRepository
from presentation.controllers.protocols.controller import Controller
from presentation.controllers.signUp import SignUp


def makeSignUp() -> Controller:
    repository = makeUserRepository()
    useCase = DbAddUser(repository, repository)
    controller = SignUp(useCase)
    return controller
