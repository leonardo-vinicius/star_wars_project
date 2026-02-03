from typing import Dict, Any, Optional
from integrations.swapi.client import ExternalApiClient


class PeopleService:
    def __init__(self, client: ExternalApiClient):
        self.client = client

    def list_people(self, params: Optional[Dict[str, Any]] = None):

        response = self.client.get(
            "people",
            params=params
        )

        results = response.get("results", [])

        page_size = 10
        start = 0
        end = page_size

        return {
            "page": params.get('page', 1),
            "page_size": page_size,
            "total": response.get("count"),
            "results": results[start:end]
        }