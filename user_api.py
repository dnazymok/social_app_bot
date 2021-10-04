import logging
import clients

logging.basicConfig(level=logging.INFO)


class UserApiClient:
    def __init__(self, user):
        self.user = user
        self.client = clients.get_client()
        self._is_registered = False
        self._register_data = {'email': self.user.email,
                               'username': self.user.username,
                               'password': self.user.password}
        self._login_data = {'username': self.user.username,
                            'password': self.user.password}
        self._post_data = {'title': 'client_title1',
                           'description': 'client_description1',
                           'content': 'client_content1'}  # todo remove
        self._token = ''

    def register(self):
        if not self._is_registered:
            self.client.post_request('users/', data=self._register_data)
            self._is_registered = True
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

    def _get_access_token(self):
        response = self.client.post_request('token/', data=self._login_data)
        return response['access']

    def _get_refresh_token(self):
        response = self.client.post_request('token/', data=self._login_data)
        return response['refresh']

    @property
    def _auth_headers(self):
        return {'Authorization': f'Bearer {self._token}'}
