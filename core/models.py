from core.clients import UserApiClient


class User:
    def __init__(self, username: str, password: str, email: str):
        self.username = username
        self.password = password
        self.email = email
        self.posts: [Post] = []
        self.api = UserApiClient(self)

    @property
    def register_data(self) -> dict:
        return {'email': self.email,
                'username': self.username,
                'password': self.password}

    @property
    def login_data(self) -> dict:
        return {'username': self.username,
                'password': self.password}

    @property
    def posts_count(self) -> int:
        return len(self.posts)

    @property
    def is_zero_liked_post(self) -> bool:
        return not all([post.likes for post in self.posts])


class Post:
    def __init__(self, title: str, description: str, content: str):
        self.title = title
        self.description = description
        self.content = content
        self.likes: [Like] = []


class Like:
    def __init__(self, user: User, post: Post):
        self.user = user
        self.post = post
