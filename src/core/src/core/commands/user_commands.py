import logging
from typing import Annotated

import typer
from pydantic import ValidationError
from wireup import injectable

from ..config.registry import command_group
from ..exceptions import CoreError
from ..services.user_service import UserService


@command_group("user")
@injectable()
class UserCommands:
    def __init__(self, user_service: UserService, logger: logging.Logger):
        self.user_service = user_service
        self.logger = logger
        self.app = typer.Typer(help="User management commands")
        self._register_commands()

    def _register_commands(self):
        self.app.command("get", help="Fetch a specific user by ID")(self.get_user)
        self.app.command("list", help="List all users")(self.list_users)
        self.app.command("posts", help="Get posts for a specific user")(self.get_user_posts)

    def get_user(
        self, user_id: Annotated[int, typer.Option("--id", help="User ID to fetch")] = 1
    ) -> None:
        try:
            user = self.user_service.get_user_by_id(user_id)
            self.logger.info(f"User: {user.name} ({user.email})")
            self.logger.info(f"Company: {user.company.name}")
            self.logger.info(f"Address: {user.address.street}, {user.address.city}")
        except (CoreError, ValidationError) as e:
            self.logger.error(f"Error fetching user: {e}")
            raise typer.Exit(1) from e

    def list_users(self) -> None:
        try:
            users = self.user_service.get_all_users()
            self.logger.info(f"Found {len(users)} users:")
            for user in users:
                self.logger.info(f"  {user.id}: {user.name} ({user.email})")
        except (CoreError, ValidationError) as e:
            self.logger.error(f"Error fetching users: {e}")
            raise typer.Exit(1) from e

    def get_user_posts(
        self, user_id: Annotated[int, typer.Option("--id", help="User ID")] = 1
    ) -> None:
        try:
            posts = self.user_service.get_user_posts(user_id)
            user = self.user_service.get_user_by_id(user_id)
            self.logger.info(f"Posts by {user.name}:")
            for post in posts:
                self.logger.info(f"  - {post['title']}")
        except (CoreError, ValidationError) as e:
            self.logger.error(f"Error fetching posts: {e}")
            raise typer.Exit(1) from e
