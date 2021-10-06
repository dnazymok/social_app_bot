from abc import ABC, abstractmethod
from faker import Faker

from user import User


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