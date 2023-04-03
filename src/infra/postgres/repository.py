from datetime import datetime
from data.protocols.userDbProtocols import (
    AddUserRepository,
    LoadUserByEmailRepository,
)

from domain.entities.user import User
from domain.usecases.addUser import AddUserModel


class UserRepository(AddUserRepository, LoadUserByEmailRepository):
    def __init__(self, conn):
        self.conn = conn

    async def add(self, user: AddUserModel) -> User:
        with self.conn.cursor() as cur:
            cur.execute(
                "INSERT INTO users (fullname, email, password, created_at) "
                "VALUES (%s, %s, %s, %s) RETURNING *;",
                (
                    user["fullname"],
                    user["email"],
                    user["password"],
                    datetime.now(),
                ),
            )
            result = cur.fetchone()
            self.conn.commit()
            user = User(*result)
            return user

    async def load(self, email: str) -> User:
        with self.conn.cursor() as cur:
            cur.execute("SELECT * FROM users WHERE email = %s;", (email,))
            result = cur.fetchone()
            if result is None:
                return None
            user = User(*result)
            return user
