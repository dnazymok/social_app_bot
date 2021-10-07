import yaml
from exceptions import ConfigNotFoundError


class Config:
    def __init__(self):
        self.path_to_config = '../config.yml'

    def get_config(self):
        try:
            with open(self.path_to_config) as f:
                config_data = yaml.safe_load(f)
            return config_data
        except FileNotFoundError as e:
            raise ConfigNotFoundError(e)
