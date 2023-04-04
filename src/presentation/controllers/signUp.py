from domain.usecases.addUser import AddUser
from presentation.errors.emailInUseError import EmailInUseError
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
                print()
                if (
                    field not in httpRequest.body
                    or not httpRequest.body[field]
                ):
                    return badRequest(MissingParamError(field))
            user = await self.addUser.add(httpRequest.body)
            if user is None:
                return forbidden(EmailInUseError())
            return created(user.toDict())
        except Exception as e:
            print(e)
            return serverError(e)
