from user import User


class AutomatedBot:
    def start(self):
        user = User(username='username_client_new1',
                    email='usernamenew@gmail.com', password='password')
        user.api.register()
        user.api.login()
        user.api.create_post()
