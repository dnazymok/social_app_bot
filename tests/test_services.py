import pytest

from unittest.mock import Mock
from core.services import LikesGeneratorService


class TestLikesGeneratorService:
    @pytest.fixture()
    def posts(self):
        posts = []
        for _ in range(5):
            post = Mock()
            posts.append(post)
        return posts

    @pytest.fixture()
    def user_with_posts(self, posts):
        user = Mock()
        user.posts = posts
        return user

    @pytest.fixture()
    def users_with_posts(self, user_with_posts):
        users = []
        for _ in range(5):
            users.append(user_with_posts)
        return users

    @pytest.fixture()
    def like_service(self, users_with_posts):
        return LikesGeneratorService(users_with_posts, 10)

    def test_get_posts_from_users(self, like_service, users_with_posts):
        posts = []
        for user in users_with_posts:
            for post in user.posts:
                posts.append(post)
        assert len(
            like_service._get_posts_from_users(like_service._users)) == len(
            posts)

    def test_get_post_by_id(self, like_service):
        post_1 = Mock()
        post_1.id = 1
        post_2 = Mock()
        post_2.id = 2
        posts = [post_1, post_2]
        assert like_service._get_post_by_id(posts, 1) == post_1
        assert like_service._get_post_by_id(posts, 2) == post_2
