from presentation.controllers.protocols.controller import HttpResponse


def badRequest(error: Exception) -> HttpResponse:
    return HttpResponse(
        400,
        {
            "error": str(error),
        },
    )
