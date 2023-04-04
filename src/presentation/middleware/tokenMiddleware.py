from presentation.controllers.protocols.controller import Controller
from presentation.controllers.protocols.http import HttpRequest, HttpResponse
from presentation.controllers.protocols.responses import unauthorized
from presentation.errors.invalidCredentialsError import InvalidCredentialsError


class TokenMiddleware(Controller):
    def __init__(self, controller: Controller):
        self.controller = controller

    async def handle(self, httpRequest: HttpRequest) -> HttpResponse:
        auth = httpRequest.headers["authorization"]
        if not auth:
            return unauthorized(InvalidCredentialsError())
