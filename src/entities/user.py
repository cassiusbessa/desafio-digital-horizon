import datetime


class User:
    def __init__(self, id, fullname, email, password):
        self.id = id
        self.fullname = fullname
        self.email = email
        self.password = password
        self.createdAt = datetime.now()

    def __str__(self):
        return (
            f"User: {self.id}, {self.fullname}, {self.email}, {self.createdAt}"
        )

    def __repr__(self):
        return (
            f"User: {self.id}, {self.fullname}, {self.email}, {self.createdAt}"
        )

    def toJSON(self):
        return {
            "id": self.id,
            "fullname": self.fullname,
            "email": self.email,
            "password": self.password,
            "createdAt": self.createdAt,
        }
