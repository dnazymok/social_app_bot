import requests
import logging

from abc import ABC, abstractmethod
from requests import HTTPError
from core.exceptions import BotApiException
from core.config import Config

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


class UserApiClient:
    def __init__(self, user):
        self._user = user
        self._client = get_client()
        self._token = ''

    def register(self):
        self._client.post_request('users/', data=self._user.register_data)
        logging.info(f'{self._user.username} registered.')

    def login(self):
        if not self._token:
            self._token = self._get_access_token()

    def logout(self):
        self._token = ''

    def create_post(self, post):
        response = self._client.post_request('posts/', data=vars(post),
                                             headers=self._auth_headers)
        logging.info(f'{self._user.username} created post.')
        return response

    def like_post(self, post_id):
        response = self._client.post_request(f'posts/{post_id}/likes',
                                             headers=self._auth_headers)
        logging.info(f'{self._user.username} liked post {post_id}')
        return response

    def _get_access_token(self):
        response = self._client.post_request('token/',
                                             data=self._user.login_data)
        return response.json()['access']

    def _get_refresh_token(self):
        response = self._client.post_request('token/',
                                             data=self._user.login_data)
        return response.json()['refresh']

    @property
    def _auth_headers(self):
        return {'Authorization': f'Bearer {self._token}'}


CLIENTS = {
    'rest': ApiClient
}


def get_client(client='rest', api_url=config.data['api_url']):
    return CLIENTS[client](api_url)
