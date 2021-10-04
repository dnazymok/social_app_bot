from abc import ABC, abstractmethod


class BaseClient(ABC):
    @abstractmethod
    def post_request(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_request(self, *args, **kwargs):
        pass


class RestApiClient(BaseClient):
    def post_request(self, *args, **kwargs):
        pass

    def get_request(self, *args, **kwargs):
        pass
