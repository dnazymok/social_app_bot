import logging
import random

from typing import Type
from core.factories.user_factories import BaseUserFactory
from core.factories.post_factories import BasePostFactory
from core.user import User
from core.services import LikesGeneratorService


class AutomatedBot:
    def __init__(self, user_factory: Type[BaseUserFactory],
                 post_factory: Type[BasePostFactory],
                 config):
        self._config = config()
        self._users: [User] = []
        self._user_factory = user_factory()
        self._post_factory = post_factory()

    def start(self):
        self._create_users()
        self._register_users()
        self._login_users()
        self._create_posts()
        self._like_posts()

    def _create_users(self):
        for _ in range(self._config.data['number_of_users']):
            user = self._user_factory.make_user()
            self._users.append(user)
            logging.info(f'User {user.username} created')

    def _register_users(self):
        for user in self._users:
            user.api.register()

    def _login_users(self):
        for user in self._users:
            user.api.login()

    def _create_posts(self):
        for user in self._users:
            for _ in range(
                    random.randint(1, self._config.data['max_posts_per_user'])):
                post = self._post_factory.make_post()
                response = user.api.create_post(post)
                post.id = response.json()['id']
                user.posts.append(post)

    def _like_posts(self):
        LikesGeneratorService(self._users,
                              self._config.data['max_likes_per_user']).start()
