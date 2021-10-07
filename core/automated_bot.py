import logging
import random
import yaml

from typing import Type
from exceptions import BotConfigNotFoundError
from factories.user_factories import BaseUserFactory
from factories.post_factories import BasePostFactory
from user import User
from services import LikesGeneratorService


class AutomatedBot:
    def __init__(self, user_factory: Type[BaseUserFactory],
                 post_factory: Type[BasePostFactory]):
        self._config = self._get_config()
        self._users: [User] = []
        self._user_factory = user_factory
        self._post_factory = post_factory

    def start(self):
        self._create_users()
        self._register_users()
        self._login_users()
        self._create_posts()
        self._like_posts()

    def _get_config(self):
        try:
            with open('../config.yml') as f:
                config_data = yaml.safe_load(f)
            return config_data
        except FileNotFoundError as e:
            raise BotConfigNotFoundError(e)

    def _create_users(self):
        for _ in range(self._config['number_of_users']):
            user = self._user_factory().make_user()
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
                    random.randint(1, self._config['max_posts_per_user'])):
                post = self._post_factory().make_post()
                response = user.api.create_post(post)
                post.id = response.json()['id']
                user.posts.append(post)

    def _like_posts(self):
        LikesGeneratorService(self._users,
                              self._config['max_likes_per_user']).start()
