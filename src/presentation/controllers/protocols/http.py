from typing import Any


class HttpRequest:
    def __init__(self, body: dict = None):
        self.body = body


class HttpResponse:
    def __init__(self, statusCode: int, body: Any):
        self.statusCode = statusCode
        self.body = body
