from user import User

test_data = {'username': 'username_client', 'password': 'password'}


class AutomatedBot:
    # def __init__(self):
    #     # self.social_api = UserApiClient()

    def start(self):
        user = User(username='username_client_new',
                    email='usernamenew@gmail.com', password='password')
        user.api.register()
        user.api.login()
