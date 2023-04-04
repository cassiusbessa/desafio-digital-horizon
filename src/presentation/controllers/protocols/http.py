from typing import Any


class HttpRequest:
    def __init__(self, body: dict = None, headers: dict = None):
        self.body = body
        self.headers = headers


class HttpResponse:
    def __init__(self, statusCode: int, body: Any):
        self.statusCode = statusCode
        self.body = body
