import psycopg2
from data.dbAddUser import DbAddUser
from infra.postgres.repository import UserRepository
from presentation.controllers.protocols.controller import Controller
from presentation.controllers.signUp import SignUp

postgresConnection = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="123456",
    port="5432",
)


def makeSignUp() -> Controller:
    repository = UserRepository(postgresConnection)
    useCase = DbAddUser(repository)
    controller = SignUp(useCase)
    return controller
