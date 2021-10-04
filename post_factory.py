from faker import Faker


class FakePostFactory:
    def __init__(self):
        self.fake = Faker()

    def make_fake_post(self):
        return {'title': self.fake.sentence(),
                'description': self.fake.sentence(),
                'content': self.fake.paragraph()}
