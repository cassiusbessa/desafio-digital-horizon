from domain.usecases.addAccount import AddAccount
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


class SignUp(Controller):
    def __init__(self, addAccount: AddAccount):
        self.addAccount = addAccount

    async def handle(self, http_request: HttpRequest) -> HttpResponse:
        try:
            required_fields = [
                "name",
                "email",
                "password",
            ]
            for field in required_fields:
                if field not in http_request.body:
                    return badRequest(MissingParamError(field))
            name = http_request.body["name"]
            email = http_request.body["email"]
            password = http_request.body["password"]

            user = await self.addAccount.add(name, email, password)
            return created(user)
        except Exception as e:
            return serverError(e)
