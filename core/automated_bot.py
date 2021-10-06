import yaml
from exceptions import BotConfigNotFoundError
from user import User


class AutomatedBot:
    def __init__(self):
        self._config = self._get_config()

    def start(self):
        print(self._config)
        # self._create_users()
        # self._register_users()
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
        try:
            pass
        except:
            pass

    def _register_users(self):
        pass

    def _login_users(self):
        pass

    def _create_posts(self):
        pass

    #  users creating (UserFactory)
    #  users register (UserApiClient)
    #  users login (UserApiClient)
    #  users create posts (PostFactory)
    #  after all users like posts (UserApiClient)

    # user = User(username='username_client_new1',
    #             email='usernamenew@gmail.com', password='password')
    # user.api.register()
    # user.api.login()
    # user.api.create_post()
    # user.api.like_post(30)