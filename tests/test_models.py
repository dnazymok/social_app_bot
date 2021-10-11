from unittest.mock import Mock

import pytest

from core.models import User, Like, Post


class TestUser:
    @pytest.fixture()
    def user(self):
        return User('username', 'password', 'email@gmail.com')

    @pytest.fixture()
    def post(self):
        return Post('title', 'descr', 'content')

    @pytest.fixture()
    def post_with_like(self):
        like = Mock()
        post = Post('title', 'descr', 'content')
        post.likes.append(like)
        return post

    def test_register_data(self, user):
        assert user.register_data['email'] == user.email
        assert user.register_data['username'] == user.username
        assert user.register_data['password'] == user.password

    def test_login_data(self, user):
        assert user.register_data['username'] == user.username
        assert user.register_data['password'] == user.password

    def test_posts_count(self, user, post):
        assert user.posts_count == 0
        user.posts.append(post)
        assert user.posts_count == 1

    def test_is_zero_liked_post(self, user, post, post_with_like):
        user.posts.append(post)
        assert user.is_zero_liked_post
        user.posts.pop()
        user.posts.append(post_with_like)
        assert not user.is_zero_liked_post
