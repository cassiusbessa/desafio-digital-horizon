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

    async def handle(self, httpRequest: HttpRequest) -> HttpResponse:
        try:
            required_fields = [
                "fullname",
                "email",
                "password",
            ]
            for field in required_fields:
                if field not in httpRequest.body:
                    return badRequest(MissingParamError(field))
            user = await self.addUser.add(httpRequest.body)
            return created(user.toDict())
        except Exception as e:
            print(e)
            return serverError(e)
