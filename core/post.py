class Post:
    def __init__(self, title, description, content):
        self.title = title
        self.description = description
        self.content = content
        self.likes: [Like] = []


class Like:
    def __init__(self, user, post):
        self.user = user
        self.post = post
