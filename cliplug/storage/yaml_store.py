import yaml
from cliplug.storage.paths import get_commands_file

DEFAULT_DATA = {
    "version": 1,
    "commands": {}
}

def load_data() -> dict:
    path = get_commands_file()

    if not path.exists():
        return DEFAULT_DATA.copy()

    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    if not data:
        return DEFAULT_DATA.copy()

    return data


def save_data(data: dict) -> None:
    path = get_commands_file()

    with path.open("w", encoding="utf-8") as f:
        yaml.safe_dump(
            data,
            f,
            sort_keys=False,
            default_flow_style=False
        )