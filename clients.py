import requests
import logging
from abc import ABC, abstractmethod
from requests import HTTPError


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
            logging.error(e)
        return response.json()

    def get_request(self, path, params=None, auth=None, headers=None):
        try:
            response = requests.get(f'{self._api_url}{path}', params=params,
                                    headers=headers)
            response.raise_for_status()
        except HTTPError as e:
            logging.error(e)
        return response.json()


API_URL = 'http://127.0.0.1:8000/'

CLIENTS = {
    'rest': ApiClient
}


def get_client(client='rest', api_url=API_URL):
    return CLIENTS[client](api_url)
