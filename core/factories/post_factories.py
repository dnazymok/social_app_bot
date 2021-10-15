from abc import ABC, abstractmethod
from typing import Type

from faker import Faker
from core.models import Post


class BasePostFactory(ABC):
    @abstractmethod
    def make_post(self):
        pass


class FakePostFactory(BasePostFactory):
    def __init__(self):
        self.fake = Faker()

    def make_post(self):
        return Post(title=self.fake.sentence(),
                    description=self.fake.sentence(),
                    content=self.fake.paragraph())


POST_FACTORIES = {
    'fake': FakePostFactory
}


def get_post_factory(post_factory='fake') -> Type[BasePostFactory]:
    return POST_FACTORIES[post_factory]()
