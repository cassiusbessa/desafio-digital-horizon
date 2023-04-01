from presentation.controllers.protocols.controller import HttpResponse


def badRequest(error: Exception) -> HttpResponse:
    return HttpResponse(
        400,
        {
            "error": str(error),
        },
    )


def serverError(error: Exception) -> HttpResponse:
    return HttpResponse(
        500,
        {
            "error": "Internal server error",
        },
    )


def created(data: dict) -> HttpResponse:
    return HttpResponse(
        201,
        data,
    )
