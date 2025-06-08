import logging

import typer
from ..config.registry import command_group
from ..services.user_service import UserService
from wireup import service


@command_group("user")
@service()
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

    def get_user(self, user_id: int = typer.Option(1, "--id", help="User ID to fetch")) -> None:
        try:
            user = self.user_service.get_user_by_id(user_id)
            self.logger.info(f"User: {user.name} ({user.email})")
            self.logger.info(f"Company: {user.company.name}")
            self.logger.info(f"Address: {user.address.street}, {user.address.city}")
        except Exception as e:
            self.logger.error(f"Error fetching user: {e}")
            raise typer.Exit(1)

    def list_users(self) -> None:
        try:
            users = self.user_service.get_all_users()
            self.logger.info(f"Found {len(users)} users:")
            for user in users:
                self.logger.info(f"  {user.id}: {user.name} ({user.email})")
        except Exception as e:
            self.logger.error(f"Error fetching users: {e}")
            raise typer.Exit(1)

    def get_user_posts(self, user_id: int = typer.Option(1, "--id", help="User ID")) -> None:
        try:
            posts = self.user_service.get_user_posts(user_id)
            user = self.user_service.get_user_by_id(user_id)
            self.logger.info(f"Posts by {user.name}:")
            for post in posts:
                self.logger.info(f"  - {post['title']}")
        except Exception as e:
            self.logger.error(f"Error fetching posts: {e}")
            raise typer.Exit(1)
