from factories.post_factories import FakePostFactory
from post import Post
from user_api import UserApiClient


class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.posts: [Post] = []
        self.api = UserApiClient(self, FakePostFactory)

    @property
    def register_data(self):
        return {'email': self.email,
                'username': self.username,
                'password': self.password}

    @property
    def login_data(self):
        return {'username': self.username,
                'password': self.password}

    @property
    def posts_count(self):
        return len(self.posts)

    @property
    def is_zero_liked_post(self):
        return not all([post.likes for post in self.posts])
