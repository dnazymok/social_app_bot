from typing import Type

import yaml

from abc import ABC, abstractmethod
from core.exceptions import ConfigNotFoundError


class BaseConfig(ABC):
    @property
    @abstractmethod
    def data(self):
        pass


class YmlConfig:
    def __init__(self):
        self.path_to_config = 'config.yml'

    @property
    def data(self) -> dict:
        try:
            with open(self.path_to_config) as f:
                config_data = yaml.safe_load(f)
            return config_data
        except FileNotFoundError as e:
            raise ConfigNotFoundError(e)


CONFIGS = {
    'yml': YmlConfig
}


def get_config(config='yml') -> Type[BaseConfig]:
    return CONFIGS[config]()
