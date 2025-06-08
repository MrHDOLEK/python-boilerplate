import typer
import wireup
from .clients.http_client import HttpClient
from .config.registry import get_registered_commands
from .commands.user_commands import UserCommands
from .config.logger_config import create_logger
from .models.config import Settings
from .services.user_service import UserService
from utils import hello as hello_world_from_utils

container = wireup.create_sync_container(
    services=[Settings, create_logger, HttpClient, UserService, UserCommands]
)

app = typer.Typer()

for command_class in get_registered_commands():
    command_instance = container.get(command_class)
    app.add_typer(command_instance.app, name=command_class._command_name)


@app.command(help="Greet someone with a friendly message")
def hello():
    hello_world_from_utils()


def entrypoint():
    app()


if __name__ == "__main__":
    entrypoint()
