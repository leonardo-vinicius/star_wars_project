from typing import Optional, List, Dict, Any
from integrations.swapi.client import ExternalApiClient
from domains.starships.models import (
    PaginatedStarshipsResponse,
    StarshipResponse,
    StarshipPilotResponse,
    StarshipFilmResponse
)
from fastapi import HTTPException


class StarshipsService:
    def __init__(self, client: ExternalApiClient):
        self.client = client

    def list_starships(
        self,
        page: int = 1,
        page_size: int = 10,
        name: Optional[str] = None
    ) -> PaginatedStarshipsResponse:
        
        swapi_params = {"page": page}

        if name:
            swapi_params["search"] = name

        response = self.client.get("starships", params=swapi_params)
        results = response.get("results", [])

        start = 0
        end = page_size

        return PaginatedStarshipsResponse(
            page=page,
            page_size=page_size,
            total=response.get("count", 0),
            results=results[start:end]
        )

    def get_starship_by_id(self, starship_id: int) -> StarshipResponse:
        try:
            response = self.client.get(f"starships/{starship_id}")
            return StarshipResponse(**response)
        except Exception as e:
            raise HTTPException(
                status_code=404,
                detail=f"Nave {starship_id} não encontrada"
            )

    def get_starship_pilots(self, starship_id: int) -> List[StarshipPilotResponse]:
        starship = self.get_starship_by_id(starship_id)
        pilots = []

        for pilot_url in starship.pilots:
            pilot_id = pilot_url.rstrip('/').split('/')[-1]
            try:
                pilot = self.client.get(f"people/{pilot_id}")
                pilots.append(StarshipPilotResponse(
                    name=pilot.get("name"),
                    birth_year=pilot.get("birth_year"),
                    gender=pilot.get("gender")
                ))
            except:
                continue

        return pilots

    def get_starship_films(self, starship_id: int) -> List[StarshipFilmResponse]:
        starship = self.get_starship_by_id(starship_id)
        films = []

        for film_url in starship.films:
            film_id = film_url.rstrip('/').split('/')[-1]
            try:
                film = self.client.get(f"films/{film_id}")
                films.append(StarshipFilmResponse(
                    title=film.get("title"),
                    episode_id=film.get("episode_id"),
                    release_date=film.get("release_date")
                ))
            except:
                continue

        return films