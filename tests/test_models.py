import pytest

from core.models import User, Like, Post


class TestUser:
    @pytest.fixture()
    def user(self):
        return User('username', 'password', 'email@gmail.com')

    @pytest.fixture()
    def post(self):
        return Post('title', 'descr', 'content')

    def test_posts_count(self, user, post):
        assert user.posts_count == 0
        user.posts.append(post)
        assert user.posts_count == 1
