from typing import Dict, Any, Optional
from integrations.api_client import ExternalApiClient

class StarWarsDataService:
    def __init__(self, api_client: ExternalApiClient):
        self.client = api_client

    def list_people(self, params: Optional[Dict[str, Any]] = None):
        return self.client.get("people", params)

    def get_person(self, person_id: int):
        return self.client.get(f"people/{person_id}")

    def list_planets(self, params: Optional[Dict[str, Any]] = None):
        return self.client.get("planets", params)

    def list_films(self):
        return self.client.get("films")
