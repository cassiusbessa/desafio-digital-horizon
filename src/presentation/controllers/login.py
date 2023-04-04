from domain.usecases.authentication import Authentication
from presentation.errors.invalidCredentialsError import InvalidCredentialsError
from presentation.errors.missingParamError import MissingParamError
from presentation.controllers.protocols.controller import (
    Controller,
    HttpRequest,
    HttpResponse,
)
from presentation.controllers.protocols.responses import (
    badRequest,
    created,
    forbidden,
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
            payload = await self.authentication.auth(httpRequest.body)
            if payload is None:
                return forbidden(InvalidCredentialsError())
            return created(payload)
        except Exception as e:
            print(e)
            return serverError(e)
