from typing import Dict, Any, Optional, List
from integrations.swapi.client import ExternalApiClient
from domains.people.models import (
    PaginatedPeopleResponse,
    PersonResponse,
    PersonFilmResponse
)


class PeopleService:
    def __init__(self, client: ExternalApiClient):
        self.client = client

    def list_people(
        self,
        page: int = 1,
        page_size: int = 10,
        name: Optional[str] = None,
        gender: Optional[str] = None,
        birth_year: Optional[str] = None
    ) -> PaginatedPeopleResponse:
        swapi_params = {"page": page}

        if name:
            swapi_params["search"] = name

        response = self.client.get("people", params=swapi_params)
        results = response.get("results", [])

        if gender:
            results = [p for p in results if p.get("gender", "").lower() == gender.lower()]
        if birth_year:
            results = [p for p in results if birth_year in p.get("birth_year", "")]

        start = 0
        end = page_size

        return PaginatedPeopleResponse(
            page=page,
            page_size=page_size,
            total=response.get("count", 0),
            results=results[start:end]
        )

    def get_person_by_id(self, person_id: int) -> PersonResponse:
        response = self.client.get(f"people/{person_id}")
        
        return PersonResponse(**response)