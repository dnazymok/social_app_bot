from social_api import SocialAppApi


test_data = {'username': 'username_client', 'password': 'password'}


class AutomatedBot:
    def __init__(self):
        self.social_api = SocialAppApi()

    def start(self):
        self.social_api.login(data=test_data)
