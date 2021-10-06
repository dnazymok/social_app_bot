from user import User


class AutomatedBot:
    def start(self):
        user = User(username='username_client_new1',
                    email='usernamenew@gmail.com', password='password')
        user.api.register()
        user.api.login()
        user.api.create_post()
        user.api.like_post(30)

    #  users creating (UserFactory)
    #  users register (UserApiClient)
    #  users login (UserApiClient)
    #  users create posts (PostFactory)
    #  after all users like posts (UserApiClient)
