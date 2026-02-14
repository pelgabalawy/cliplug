from platformdirs import user_config_dir
from pathlib import Path

APP_NAME = "cliplug"

def get_config_dir() -> Path:
    # Setting appauthor=False prevents the double 'cliplug' folder
    path = Path(user_config_dir(APP_NAME, appauthor=False))
    path.mkdir(parents=True, exist_ok=True)
    return path

# \Users\<username>\AppData\Roaming\cliplug\commands.yaml
# /home/<username>/.config/cliplug/commands.yaml
def get_commands_file() -> Path:
    return get_config_dir() / "commands.yaml"