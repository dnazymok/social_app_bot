import pytest

from core.configs import get_config
from core.exceptions import ConfigNotFoundError


class TestConfig:
    @pytest.fixture()
    def config(self):
        return get_config()

    @pytest.fixture()
    def config_with_wrong_path(self):
        config = get_config()
        config.path_to_config = ''
        return config

    def test_data(self, config):
        assert config.data['max_likes_per_user']

    def test_data_with_wrong_path(self, config_with_wrong_path):
        with pytest.raises(ConfigNotFoundError):
            config_with_wrong_path.data

