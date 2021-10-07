import logging
import random
import yaml

from exceptions import BotConfigNotFoundError
from factories.user_factories import FakeUserFactory
from post import Post, Like
from user import User
from services import LikesGeneratorService


class AutomatedBot:
    def __init__(self):
        self._config = self._get_config()
        self._users: [User] = []

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
            user = FakeUserFactory().make_user()
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
                user.api.create_post()

    def _like_posts(self):
        LikesGeneratorService(self._users,
                              self._config['max_likes_per_user']).start()

    #  users creating (UserFactory)
    #  users register (UserApiClient)
    #  users login (UserApiClient)
    #  users create posts (PostFactory)
    #  after all users like posts (UserApiClient)

    # 1. get user (who should like)
    #  need count of users posts
    # 2.1 get post
    #  need count of likes of user posts
    # 2.2 like
    # 2.3 repeat until reach max likes
    # 3. repeat
