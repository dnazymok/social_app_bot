from abc import ABC, abstractmethod
from typing import Type

from faker import Faker
from core.models import User


class BaseUserFactory(ABC):
    @abstractmethod
    def make_user(self) -> User:
        pass


class FakeUserFactory(BaseUserFactory):
    def __init__(self):
        self.fake = Faker()

    def make_user(self) -> User:
        return User(username=self.fake.user_name(),
                    email=self.fake.email(),
                    password=self.fake.password())


USER_FACTORIES = {
    'fake': FakeUserFactory
}


def get_user_factory(user_factory='fake') -> Type[BaseUserFactory]:
    return USER_FACTORIES[user_factory]()

