from clients import ApiClient


class UserApiClient:
    def __init__(self, user):
        self.client = ApiClient('http://127.0.0.1:8000/')
        self._register_data = {'email': user.email,
                               'username': user.username,
                               'password': user.password}

        self._login_data = {'username': user.username,
                            'password': user.password}
        self._token = ''

    def register(self):
        self.client.post_request('users/', data=self._register_data)  # todo add logger

    def login(self):
        self._token = self._get_access_token()

    def logout(self):
        self._token = ''

    def _get_access_token(self):
        response = self.client.post_request('token/', data=self._login_data)
        return response['access']

    def _get_refresh_token(self):
        response = self.client.post_request('token/', data=self._login_data)
        return response['refresh']
