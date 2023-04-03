from datetime import datetime
from data.protocols.userDbProtocols import AddUserRepository

from domain.entities.user import User
from domain.usecases.addUser import AddUserModel


class UserRepository(AddUserRepository):
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
