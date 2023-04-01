from abc import ABC, abstractmethod

from presentation.controllers.protocols.http import HttpRequest, HttpResponse


class Controller(ABC):
    @abstractmethod
    async def handle(self, http_request: HttpRequest) -> HttpResponse:
        pass
