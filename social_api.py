from clients import RestApiClient


class SocialAppApi:
    def __init__(self):
        self.client = RestApiClient('http://127.0.0.1:8000/')

    def register(self, data):
        self.client.post_request('users/', data=data)  # todo add logger
