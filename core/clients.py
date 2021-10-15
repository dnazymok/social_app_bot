import requests
import logging

from abc import ABC, abstractmethod
from requests import HTTPError, Response
from core.exceptions import BotApiException
from core.configs import get_config

config = get_config()


class BaseClient(ABC):
    @abstractmethod
    def post_request(self, *args, **kwargs) -> Response:
        pass

    @abstractmethod
    def get_request(self, *args, **kwargs) -> Response:
        pass


class ApiClient(BaseClient):
    def __init__(self, api_url):
        self._api_url = api_url

    def post_request(self, path, data=None, auth=None, headers=None) -> Response:
        try:
            response = requests.post(f'{self._api_url}{path}', data=data,
                                     headers=headers)
            response.raise_for_status()
        except HTTPError as e:
            raise BotApiException(e)
        return response

    def get_request(self, path, params=None, auth=None, headers=None) -> Response:
        try:
            response = requests.get(f'{self._api_url}{path}', params=params,
                                    headers=headers)
            response.raise_for_status()
        except HTTPError as e:
            raise BotApiException(e)
        return response


class UserApiClient:
    def __init__(self, user):
        self._user = user
        self._client = get_client()
        self._token = ''

    def register(self) -> Response:
        response = self._client.post_request('users/',
                                             data=self._user.register_data)
        logging.info(f'{self._user.username} registered.')
        return response

    def login(self) -> None:
        if not self._token:
            self._token = self._get_access_token()

    def logout(self) -> None:
        self._token = ''

    def create_post(self, post) -> Response:
        response = self._client.post_request('posts/', data=vars(post),
                                             headers=self._auth_headers)
        logging.info(f'{self._user.username} created post.')
        return response

    def like_post(self, post_id) -> Response:
        response = self._client.post_request(f'posts/{post_id}/like/',
                                             headers=self._auth_headers)
        logging.info(f'{self._user.username} liked post {post_id}')
        return response

    def _get_access_token(self) -> str:
        response = self._client.post_request('token/',
                                             data=self._user.login_data)
        return response.json()['access']

    @property
    def _auth_headers(self) -> dict:
        return {'Authorization': f'Bearer {self._token}'}


CLIENTS = {
    'rest': ApiClient
}


def get_client(client='rest', api_url=config.data['api_url']) -> BaseClient:
    return CLIENTS[client](api_url)
