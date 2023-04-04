from presentation.controllers.protocols.controller import Controller
from presentation.controllers.protocols.http import HttpRequest, HttpResponse
from presentation.controllers.protocols.responses import ok


class ListUsers(Controller):
    def __init__(self, getAllUsers):
        self.getAllUsers = getAllUsers

    async def handle(self, httpRequest: HttpRequest) -> HttpResponse:
        users = await self.getAllUsers.list()
        print(users, "<<<<<<<<<<<<<<<")

        return ok([user.toDict() for user in users])
