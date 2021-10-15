import logging
import random

from typing import Type

from core.factories.user_factories import BaseUserFactory, FakeUserFactory
from core.factories.post_factories import BasePostFactory, FakePostFactory
from core.models import User
from core.services import LikesGeneratorService
from core.configs import YmlConfig, BaseConfig


class AutomatedBot:
    def __init__(self):
        self._config = get_config()
        self._users: [User] = []
        self._user_factory = get_user_factory()
        self._post_factory = get_post_factory()

    def start(self) -> None:
        self._create_users()
        self._register_users()
        self._login_users()
        self._create_posts()
        self._like_posts()

    def _create_users(self) -> None:
        for _ in range(self._config.data['number_of_users']):
            user = self._user_factory.make_user()
            self._users.append(user)
            logging.info(f'User {user.username} created')

    def _register_users(self) -> None:
        for user in self._users:
            user.api.register()

    def _login_users(self) -> None:
        for user in self._users:
            user.api.login()

    def _create_posts(self) -> None:
        for user in self._users:
            for _ in range(
                    random.randint(1, self._config.data['max_posts_per_user'])):
                post = self._post_factory.make_post()
                response = user.api.create_post(post)
                post.id = response.json()['id']
                user.posts.append(post)

    def _like_posts(self) -> None:
        LikesGeneratorService(self._users,
                              self._config.data['max_likes_per_user']).start()
