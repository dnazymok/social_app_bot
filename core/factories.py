from abc import ABC, abstractmethod
from faker import Faker


class BasePostFactory(ABC):
    @abstractmethod
    def make_post(self):
        pass


class FakePostFactory(BasePostFactory):
    def __init__(self):
        self.fake = Faker()

    def make_post(self):
        return {'title': self.fake.sentence(),
                'description': self.fake.sentence(),
                'content': self.fake.paragraph()}
