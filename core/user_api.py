import logging
import clients


class UserApiClient:
    def __init__(self, user):
        self._user = user
        self._client = clients.get_client()
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
