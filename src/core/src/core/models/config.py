from pathlib import Path
import yaml
from pydantic import BaseModel
from wireup import service
from yaml.loader import SafeLoader
from yaml_env_tag import construct_env_tag
from dotenv import load_dotenv

SafeLoader.add_constructor("!ENV", construct_env_tag)


class ApiConfig(BaseModel):
    base_url: str
    retry_attempts: int


class AppConfig(BaseModel):
    name: str
    version: str
    default_greeting: str


@service
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

        with open(config_path, "r") as f:
            config_data = yaml.load(f, Loader=SafeLoader)

        super().__init__(**config_data)

    @classmethod
    def load_from_yaml(cls) -> "Settings":
        return cls()
