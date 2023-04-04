from presentation.controllers.protocols.controller import HttpResponse


def created(data: dict) -> HttpResponse:
    return HttpResponse(
        201,
        data,
    )


def ok(data: dict) -> HttpResponse:
    return HttpResponse(
        200,
        data,
    )


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


def forbidden(error: Exception) -> HttpResponse:
    return HttpResponse(
        403,
        {
            "error": str(error),
        },
    )


def unauthorized(error: Exception) -> HttpResponse:
    return HttpResponse(
        401,
        {
            "error": str(error),
        },
    )
