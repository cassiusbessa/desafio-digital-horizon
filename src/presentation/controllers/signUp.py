from domain.usecases.userUseCases import UserUseCases
from presentation.errors.missingParamError import MissingParamError
from presentation.controllers.protocols.controller import (
    Controller,
    HttpRequest,
    HttpResponse,
)
from presentation.controllers.protocols.responses import badRequest


class SignUp(Controller):
    def __init__(self, useCases: UserUseCases):
        self.useCases = useCases

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        required_fields = [
            "name",
            "email",
            "password",
        ]
        for field in required_fields:
            if field not in http_request.body:
                return badRequest(MissingParamError(field))
