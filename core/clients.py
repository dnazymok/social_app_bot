import requests
from abc import ABC, abstractmethod
from requests import HTTPError
from exceptions import BotApiException
from config import Config

config = Config()


class BaseClient(ABC):
    @abstractmethod
    def post_request(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_request(self, *args, **kwargs):
        pass


class ApiClient(BaseClient):
    def __init__(self, api_url):
        self._api_url = api_url

    def post_request(self, path, data=None, auth=None, headers=None):
        try:
            response = requests.post(f'{self._api_url}{path}', data=data,
                                     headers=headers)
            response.raise_for_status()
        except HTTPError as e:
            raise BotApiException(e)
        return response

    def get_request(self, path, params=None, auth=None, headers=None):
        try:
            response = requests.get(f'{self._api_url}{path}', params=params,
                                    headers=headers)
            response.raise_for_status()
        except HTTPError as e:
            raise BotApiException(e)
        return response


CLIENTS = {
    'rest': ApiClient
}


def get_client(client='rest', api_url=config.data['api_url']):
    return CLIENTS[client](api_url)
