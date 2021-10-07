import logging
import yaml

from random import randint
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
            for _ in range(randint(1, self._config['max_posts_per_user'])):
                user.api.create_post()

    def _like_posts(self):  # todo has not reached max likes
        user_with_most_posts = self._get_user_with_most_posts(self._users)
        users_with_zero_liked_post = self._get_users_with_zero_liked_post(self._users)
        posts_to_like = self._get_posts_from_users(users_with_zero_liked_post)

        # get random post from user, get id, make post request
        # in this class make user.post.likes.append(Like) if request 201

    def _get_user_with_most_posts(self, users: [User]):  # todo in another class
        for user in users:
            user_with_most_posts = user
            if user.posts_count > user_with_most_posts.posts_count:
                user_with_most_posts = user
        return user_with_most_posts

    def _get_users_with_zero_liked_post(self, users: [User]):
        users_with_zero_liked_post = []
        for user in users:
            if user.is_zero_liked_post:
                users_with_zero_liked_post.append(user)
        return users_with_zero_liked_post

    def _get_posts_from_users(self, users: [User]):
        posts = []
        for user in users:
            for post in user.posts:
                posts.append(post)
        return posts

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
