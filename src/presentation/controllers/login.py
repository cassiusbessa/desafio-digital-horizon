from domain.usecases.authentication import Authentication
from presentation.errors.missingParamError import MissingParamError
from presentation.controllers.protocols.controller import (
    Controller,
    HttpRequest,
    HttpResponse,
)
from presentation.controllers.protocols.responses import (
    badRequest,
    created,
    serverError,
)


class Login(Controller):
    def __init__(self, authentication: Authentication):
        self.authentication = authentication

    async def handle(self, httpRequest: HttpRequest) -> HttpResponse:
        try:
            required_fields = ["email", "password"]
            for field in required_fields:
                if field not in httpRequest.body:
                    return badRequest(MissingParamError(field))
            user = await self.addUser.add(httpRequest.body)
            return created(user)
        except Exception as e:
            print(e)
            return serverError(e)
