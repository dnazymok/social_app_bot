import logging
import clients
from typing import Type
from factories import BasePostFactory
from requests import HTTPError


class UserApiClient:
    def __init__(self, user, post_factory: Type[BasePostFactory]):
        self._user = user
        self._client = clients.get_client()
        self._post_data = post_factory().make_post()
        self._register_data = {'email': self._user.email,
                               'username': self._user.username,
                               'password': self._user.password}
        self._login_data = {'username': self._user.username,
                            'password': self._user.password}
        self._token = ''

    def register(self):
        self._client.post_request('users/', data=self._register_data)
        logging.info(f'{self._user.username} registered.')

    def login(self):
        if not self._token:
            self._token = self._get_access_token()

    def logout(self):
        self._token = ''

    def create_post(self):
        self._client.post_request('posts/', data=self._post_data,
                                  headers=self._auth_headers)
        logging.info(f'{self._user.username} created post.')

    def like_post(self, post_id):
        self._client.post_request(f'posts/{post_id}/likes',
                                  data=self._post_data,
                                  headers=self._auth_headers)
        logging.info(f'{self._user.username} liked post {post_id}')

    def _get_access_token(self):
        response = self._client.post_request('token/', data=self._login_data)
        return response.json()['access']

    def _get_refresh_token(self):
        response = self._client.post_request('token/', data=self._login_data)
        return response.json()['refresh']

    @property
    def _auth_headers(self):
        return {'Authorization': f'Bearer {self._token}'}
