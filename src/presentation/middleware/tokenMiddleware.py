from domain.usecases.tokenValidator import TokenValidator
from presentation.controllers.protocols.controller import Controller
from presentation.controllers.protocols.http import HttpRequest, HttpResponse
from presentation.controllers.protocols.responses import unauthorized
from presentation.errors.invalidCredentialsError import InvalidCredentialsError


class TokenMiddleware(Controller):
    def __init__(self, controller: Controller, tokenValidator: TokenValidator):
        self.controller = controller
        self.tokenValidator = tokenValidator

    async def handle(self, httpRequest: HttpRequest) -> HttpResponse:
        auth = httpRequest.headers["authorization"]
        if not auth:
            return unauthorized(InvalidCredentialsError())
        valid = await self.tokenValidator.validate(auth)
        if not valid:
            return unauthorized(InvalidCredentialsError())
        return await self.controller.handle(httpRequest)
