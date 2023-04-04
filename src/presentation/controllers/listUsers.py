from presentation.controllers.protocols.controller import Controller
from presentation.controllers.protocols.http import HttpRequest, HttpResponse
from presentation.controllers.protocols.responses import ok, serverError


class ListUsers(Controller):
    def __init__(self, getAllUsers):
        self.getAllUsers = getAllUsers

    async def handle(self, httpRequest: HttpRequest) -> HttpResponse:
        try:
            users = await self.getAllUsers.list()
            return ok([user.toDict() for user in users])
        except Exception as e:
            return serverError(e)
