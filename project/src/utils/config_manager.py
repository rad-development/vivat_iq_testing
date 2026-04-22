from py_selenium_auto_core.utilities.root_path_helper import RootPathHelper
from py_selenium_auto_core.logging.logger import Logger

from src.models.config import Config
from src.utils.json_utils import JsonUtils


class ConfigManager:
    __config_instance: Config | None = None
    CONFIG_FILE_PATH = "/config/config.json"

    @classmethod
    def get_config(cls) -> Config:
        if cls.__config_instance is None:
            root = RootPathHelper.calling_root_path()
            config_path = f"{root}{cls.CONFIG_FILE_PATH}"
            Logger.info(f"Loading config from {config_path}")
            data = JsonUtils.read_json(config_path)
            cls.__config_instance = JsonUtils.parse_model(data, Config)
        return cls.__config_instance
