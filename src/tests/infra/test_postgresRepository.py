import unittest
import psycopg2.extras
from datetime import datetime


from domain.entities.user import User
from domain.usecases.addUser import AddUserModel
from infra.postgres.repository import UserRepository


class TestUserRepository(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.conn = psycopg2.connect(
            host="localhost",
            database="postgres_test",
            user="postgres",
            password="123456",
            port="5432",
        )
        self.cursor = self.conn.cursor(
            cursor_factory=psycopg2.extras.DictCursor
        )
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS users(
            id serial primary key,
            fullname varchar(255) not null,
            email varchar(255) not null,
            password varchar(255) not null,
            created_at timestamp not null);"""
        )
        self.user_repository = UserRepository(self.conn)

    def tearDown(self):
        self.conn.rollback()
        self.conn.commit()
        self.cursor.execute("DROP TABLE IF EXISTS users CASCADE;")
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    async def test_add_user(self):
        userModel: AddUserModel = {
            "fullname": "valid_name",
            "email": "valid_email",
            "password": "valid_password",
        }
        result = await self.user_repository.add(userModel)

        self.cursor.execute("SELECT * FROM users WHERE id = %s", (result.id,))
        db_user = self.cursor.fetchone()
        self.assertEqual(db_user["fullname"], userModel["fullname"])
        self.assertEqual(db_user["email"], userModel["email"])
        self.assertEqual(db_user["password"], userModel["password"])
        self.assertTrue(isinstance(db_user["created_at"], datetime))

        self.assertTrue(isinstance(result, User))
        self.assertEqual(result.fullname, userModel["fullname"])
        self.assertEqual(result.email, userModel["email"])
        self.assertEqual(result.password, userModel["password"])
        self.assertTrue(isinstance(result.createdAt, datetime))
        self.assertTrue(isinstance(result.id, int))

    async def test_load_user(self):
        userModel: AddUserModel = {
            "fullname": "valid_name",
            "email": "valid_email",
            "password": "valid_password",
        }
        self.cursor.execute(
            "INSERT INTO users (fullname, email, password, created_at) "
            "VALUES (%s, %s, %s, %s) RETURNING *;",
            (
                userModel["fullname"],
                userModel["email"],
                userModel["password"],
                datetime.now(),
            ),
        )
        db_user = self.cursor.fetchone()
        self.conn.commit()

        result = await self.user_repository.load(db_user["email"])

        self.assertEqual(result.fullname, userModel["fullname"])
        self.assertEqual(result.email, userModel["email"])
        self.assertEqual(result.password, userModel["password"])
        self.assertTrue(isinstance(result.createdAt, datetime))
        self.assertTrue(isinstance(result.id, int))


if __name__ == "__main__":
    unittest.main()
