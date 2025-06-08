from typing import Any, Dict, Optional

import requests  # type: ignore
from ..models.config import Settings
from wireup import service


@service
class HttpClient:
    def __init__(self, settings: Settings):
        self.base_url = settings.api.base_url.rstrip("/")
        self.session = requests.Session()

    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        url = f"{self.base_url}{endpoint}"
        try:
            response = self.session.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"HTTP request failed: {e}")
        except ValueError as e:
            raise Exception(f"Invalid JSON response: {e}")

    def close(self):
        self.session.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
