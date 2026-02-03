from typing import Dict, Any, Optional
from integrations.swapi.client import ExternalApiClient


class PeopleService:
    def __init__(self, client: ExternalApiClient):
        self.client = client

    def list_people(
        self,
        params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        return self.client.get("people", params)

    def get_person_by_id(self, person_id: int) -> Dict[str, Any]:
        return self.client.get(f"people/{person_id}")