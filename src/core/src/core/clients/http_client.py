from typing import Any

import requests
from wireup import injectable

from ..exceptions import HttpError
from ..models.config import Settings


@injectable
class HttpClient:
    def __init__(self, settings: Settings):
        self.base_url = settings.api.base_url.rstrip("/")
        self.session = requests.Session()

    def get(self, endpoint: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
        url = f"{self.base_url}{endpoint}"
        try:
            response = self.session.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as error:
            raise HttpError(f"HTTP request failed: {error}") from error
        except ValueError as error:
            raise HttpError(f"Invalid JSON response: {error}") from error

    def close(self):
        self.session.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
