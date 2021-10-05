import logging
import clients
from typing import Type
from factories import BasePostFactory
from requests import HTTPError


class UserApiClient:
    def __init__(self, user, post_factory: Type[BasePostFactory]):
        self.user = user
        self.client = clients.get_client()
        self._post_data = post_factory().make_post()
        self._register_data = {'email': self.user.email,
                               'username': self.user.username,
                               'password': self.user.password}
        self._login_data = {'username': self.user.username,
                            'password': self.user.password}
        self._token = ''

    def register(self):
        try:
            self.client.post_request('users/', data=self._register_data)
        except HTTPError:  # todo custom error from clients.py
            logging.info(f'{self.user.username} already registered.')
        else:
            logging.info(f'{self.user.username} registered.')

    def login(self):
        if not self._token:
            self._token = self._get_access_token()

    def logout(self):
        self._token = ''

    def create_post(self):
        self.client.post_request('posts/', data=self._post_data,
                                 headers=self._auth_headers)
        logging.info(f'{self.user.username} created post.')

    def like_post(self, post_id):
        try:
            self.client.post_request(f'posts/{post_id}/likes',
                                     data=self._post_data,
                                     headers=self._auth_headers)
        except HTTPError:  # todo custom error
            logging.info(f'{self.user.username} already liked post {post_id}')
        else:
            logging.info(f'{self.user.username} liked post {post_id}')

    def _get_access_token(self):
        response = self.client.post_request('token/', data=self._login_data)
        return response.json()['access']

    def _get_refresh_token(self):
        response = self.client.post_request('token/', data=self._login_data)
        return response.json()['refresh']

    @property
    def _auth_headers(self):
        return {'Authorization': f'Bearer {self._token}'}
