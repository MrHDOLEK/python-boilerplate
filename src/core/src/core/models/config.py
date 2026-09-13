from pathlib import Path

import yaml
from dotenv import load_dotenv
from pydantic import BaseModel
from wireup import injectable
from yaml.loader import SafeLoader
from yaml_env_tag import construct_env_tag

SafeLoader.add_constructor("!ENV", construct_env_tag)


class ApiConfig(BaseModel):
    base_url: str
    retry_attempts: int


class AppConfig(BaseModel):
    name: str
    version: str
    default_greeting: str


@injectable
class Settings(BaseModel):
    api: ApiConfig
    app: AppConfig
    logging: dict

    def __init__(self):
        path = Path(__file__).parent.parent
        config_path = path / "config" / "config.yaml"

        load_dotenv(dotenv_path=path.parent.parent / ".env")

        if not config_path.exists():
            raise FileNotFoundError(f"Config file not found: {config_path}")

        with open(config_path, "r") as config_file:
            config_data = yaml.load(config_file, Loader=SafeLoader)

        super().__init__(**config_data)

    @classmethod
    def load_from_yaml(cls) -> Settings:
        return cls()
