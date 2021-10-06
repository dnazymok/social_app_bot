import logging

import yaml
from exceptions import BotConfigNotFoundError
from factories.user_factories import FakeUserFactory
from user import User


class AutomatedBot:
    def __init__(self):
        self._config = self._get_config()
        self._users: [User] = []

    def start(self):
        self._create_users()
        self._register_users()
        # self._login_users()
        # self._create_posts()

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
        pass

    def _create_posts(self):
        pass

    #  users creating (UserFactory)
    #  users register (UserApiClient)
    #  users login (UserApiClient)
    #  users create posts (PostFactory)
    #  after all users like posts (UserApiClient)
