import psycopg2
from infra.postgres.repository import UserRepository


postgresConnection = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="123456",
    port="5432",
)


def makeUserRepository():
    return UserRepository(postgresConnection)
