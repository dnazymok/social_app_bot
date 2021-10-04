import requests

from abc import ABC, abstractmethod

from requests import HTTPError


class BaseClient(ABC):
    @abstractmethod
    def post_request(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_request(self, *args, **kwargs):
        pass


class RestApiClient(BaseClient):
    def __init__(self, api_url):
        self._api_url = api_url

    def post_request(self, path, data=None, auth=None):
        try:
            response = requests.post(f'{self._api_url}{path}', data=data,
                                     auth=auth)
            response.raise_for_status()
        except HTTPError as e:
            print(e)  # todo
        return response.json()

    def get_request(self, path, params=None, auth=None):
        try:
            response = requests.get(f'{self._api_url}{path}', params=params,
                                    auth=auth)
            response.raise_for_status()
        except HTTPError as e:
            print(e)  # todo
        return response.json()
