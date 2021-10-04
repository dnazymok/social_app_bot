from social_api import SocialAppApi


test_data = {'username': 'username_client1', 'password': 'password',
             'email': 'email@gmail.com'}


class AutomatedBot:
    def __init__(self):
        self.social_api = SocialAppApi()

    def start(self):
        self.social_api.register(data=test_data)
