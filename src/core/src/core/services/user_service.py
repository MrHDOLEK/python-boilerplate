from typing import Any, cast

from wireup import injectable

from ..clients.http_client import HttpClient
from ..models.user import User


@injectable()
class UserService:
    def __init__(self, http_client: HttpClient):
        self.http_client = http_client

    def get_user_by_id(self, user_id: int) -> User:
        data = self.http_client.get(f"/users/{user_id}")
        return User.from_dict(data)

    def get_all_users(self) -> list[User]:
        data = self.http_client.get("/users")
        return [User.from_dict(user_data) for user_data in cast(list[dict[str, Any]], data)]

    def get_user_posts(self, user_id: int) -> list[dict[str, Any]]:
        return cast(list[dict[str, Any]], self.http_client.get(f"/users/{user_id}/posts"))
