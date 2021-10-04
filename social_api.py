from clients import RestApiClient


class SocialAppApi:
    def __init__(self):
        self.client = RestApiClient('http://127.0.0.1:8000/')

    def test(self):
        response = self.client.get_request('posts/')
        print(response)