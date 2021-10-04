from clients import RestApiClient


class SocialAppApi:
    def __init__(self):
        self.client = RestApiClient('http://127.0.0.1:8000/')

    def register(self, data):
        self.client.post_request('users/', data=data)  # todo add logger

    def login(self, data):
        token = self._get_access_token(data=data)

    def _get_access_token(self, data):
        response = self.client.post_request('token/', data=data)
        return response['access']

    def _get_refresh_token(self, data):
        response = self.client.post_request('token/', data=data)
        return response['refresh']
