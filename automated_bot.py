from social_api import SocialAppApi


class AutomatedBot:
    def __init__(self):
        self.social_api = SocialAppApi()

    def start(self):
        self.social_api.test()