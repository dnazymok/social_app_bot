import pytest
import requests

from core.clients import ApiClient
from core.config import Config


class TestApiClient:
    post_data = {'title': 'foo',
                 'body': 'bar',
                 'userId': 1, }

    @pytest.fixture()
    def api_client(self):
        return ApiClient('https://jsonplaceholder.typicode.com')

    @pytest.mark.parametrize('path',
                             ['/posts', '/comments', '/albums', '/photos'])
    def test_post_request(self, api_client, path):
        response = api_client.post_request(path=path)
        assert response.status_code == 201

    @pytest.mark.parametrize('path',
                             ['/posts', '/comments', '/albums', '/photos'])
    def test_get_request(self, api_client, path):
        response = api_client.get_request(path=path)
        assert response.status_code == 200
