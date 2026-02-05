from platformdirs import user_config_dir
from pathlib import Path

APP_NAME = "cliplug"

def get_config_dir() -> Path:
    path = Path(user_config_dir(APP_NAME))
    path.mkdir(parents=True, exist_ok=True)
    return path

def get_commands_file() -> Path:
    return get_config_dir() / "commands.yaml"