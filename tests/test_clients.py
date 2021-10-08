import pytest

from core.clients import ApiClient, UserApiClient
from unittest.mock import Mock, patch


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
    def user_api_client(self, user):
        return UserApiClient(user)

    @pytest.fixture()
    def response_mock(self):
        response = Mock()
        response.status_code = 201
        return response

    def test_register(self, user_api_client, response_mock):
        with patch.object(user_api_client._client, 'post_request',
                          return_value=response_mock):
            assert user_api_client.like_post(1).status_code == 201

    def test_login(self, user_api_client):
        get_access_token_mock = Mock(return_value='token')
        with patch.object(user_api_client, '_get_access_token',
                          return_value=get_access_token_mock()):
            user_api_client.login()
            assert user_api_client._token == 'token'

    def test_logout(self, user_api_client):
        user_api_client._token = 'token'
        user_api_client.logout()
        assert user_api_client._token == ''

    def test_create_post(self, user_api_client, response_mock):
        post = Mock()
        with patch.object(user_api_client._client, 'post_request',
                          return_value=response_mock):
            assert user_api_client.create_post(post).status_code == 201

    def test_like_post(self, user_api_client, response_mock):
        with patch.object(user_api_client._client, 'post_request',
                          return_value=response_mock):
            assert user_api_client.like_post(1).status_code == 201

    def test_get_access_token(self, user_api_client, response_mock):
        response_mock.json = Mock(return_value={'access': 'access_token'})
        with patch.object(user_api_client._client, 'post_request',
                          return_value=response_mock):
            assert user_api_client._get_access_token() == 'access_token'
