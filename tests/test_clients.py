import pytest

from core.clients import ApiClient, UserApiClient
from unittest.mock import Mock


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
        response = api_client.post_request(path=path, data=self.post_data)
        assert response.status_code == 201

    @pytest.mark.parametrize('path',
                             ['/posts', '/comments', '/albums', '/photos'])
    def test_get_request(self, api_client, path):
        response = api_client.get_request(path=path)
        assert response.status_code == 200


class TestUserApiClient:
    @pytest.fixture()
    def user(self):
        return Mock()

    @pytest.fixture()
    def api_client(self, user):
        return UserApiClient(user)

    def test_login(self, api_client):
        get_access_token_mock = Mock(return_value='token')
        api_client._get_access_token = get_access_token_mock
        api_client.login()
        assert api_client._token == 'token'

    def test_logout(self, api_client):
        api_client._token = 'token'
        api_client.logout()
        assert api_client._token == ''
