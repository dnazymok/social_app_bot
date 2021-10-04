from user_api import UserApiClient


class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.api = UserApiClient(self)
