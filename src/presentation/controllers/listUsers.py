from presentation.controllers.protocols.controller import Controller
from presentation.controllers.protocols.http import HttpRequest, HttpResponse
from presentation.controllers.protocols.responses import (
    ok,
    serverError,
    unauthorized,
)
from presentation.errors.invalidCredentialsError import InvalidCredentialsError


class ListUsers(Controller):
    def __init__(self, getAllUsers):
        self.getAllUsers = getAllUsers

    async def handle(self, httpRequest: HttpRequest) -> HttpResponse:
        try:
            auth = httpRequest.headers["authorization"]
            if not auth:
                return unauthorized(InvalidCredentialsError())
            users = await self.getAllUsers.list()
            return ok([user.toDict() for user in users])
        except Exception as e:
            return serverError(e)
