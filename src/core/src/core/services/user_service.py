from typing import Any, Dict, List, cast

from ..clients.http_client import HttpClient
from ..models.user import User
from wireup import service


@service()
class UserService:
    def __init__(self, http_client: HttpClient):
        self.http_client = http_client

    def get_user_by_id(self, user_id: int) -> User:
        data = self.http_client.get(f"/users/{user_id}")
        return User.from_dict(cast(Dict[str, Any], data))

    def get_all_users(self) -> List[User]:
        data = self.http_client.get("/users")
        return [User.from_dict(user_data) for user_data in cast(List[Dict[str, Any]], data)]

    def get_user_posts(self, user_id: int) -> List[Dict[str, Any]]:
        return cast(List[Dict[str, Any]], self.http_client.get(f"/users/{user_id}/posts"))
