from pathlib import Path
import json
from platformdirs import user_config_dir

APP_NAME = 'cliplug'

class ConfigManager:
    def __init__(self):
        # the path to the config (user level here not global)
        self.config_dir = Path(user_config_dir(APP_NAME))
        # the config file path
        self.config_file = self.config_dir / 'config.json'

        # ensure config exists
        self._ensure_config_exists()
        # load the config
        self.config = self._load()

    def get_config(self):
        """
        the current active config
        :return: config as a dict
        :rtype: dict
        """
        return self.config

    def change_config(self, key, value):
        if key not in self.config:
            raise KeyError(f"Config key '{key}' not found")
        else:
            self.config[key] = value
            self._save(self.config)

    def _default_config(self):
        """
        The default config
        :return: config as a dict
        :rtype: dict
        """
        return {
            "commands_file": str(self.config_dir / 'commands.json'),
            "format": "json"
        }

    def _ensure_config_exists(self):
        """
        ensure config exists before manipulations
        """
        self.config_dir.mkdir(parents=True, exist_ok=True)
        if not self.config_file.exists():
            default = self._default_config()
            self._save(default)

    def _save(self, config):
        """
        :param config: the config we want to save
        :return: void
        """
        with open(self.config_file, "w") as f:
            json.dump(config, f, indent=2)

    def _load(self):
        """
        load the current config
        :return: current active config
        """
        # load the config and return it
        try:
            with open(self.config_file, "r") as f:
                config = json.load(f)
                self._validate(config)
                return config
        except json.JSONDecodeError:
            default = self._default_config()
            self._save(default)
            return default

    def _validate(self, config):
        required_keys = ["commands_file", "format"]
        for key in required_keys:
            if key not in config:
                raise ValueError(f"Config key '{key}' not found")
