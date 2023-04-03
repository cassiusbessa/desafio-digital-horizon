from domain.usecases.addUser import AddUser
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
    def __init__(self, addUser: AddUser):
        self.addUser = addUser

    async def handle(self, http_request: HttpRequest) -> HttpResponse:
        try:
            required_fields = [
                "fullname",
                "email",
                "password",
            ]
            for field in required_fields:
                if field not in http_request.body:
                    return badRequest(MissingParamError(field))
            fullname = http_request.body["fullname"]
            email = http_request.body["email"]
            password = http_request.body["password"]

            user = await self.addUser.add(fullname, email, password)
            return created(user)
        except Exception as e:
            return serverError(e)
