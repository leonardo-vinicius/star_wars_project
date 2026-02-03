from typing import Optional, List, Dict, Any
from integrations.swapi.client import ExternalApiClient
from domains.films.models import (
    PaginatedFilmsResponse,
    FilmResponse,
    FilmCharacterResponse,
    FilmPlanetResponse,
    FilmStarshipResponse,
    FilmSummaryResponse
)
from fastapi import HTTPException


class FilmsService:
    def __init__(self, client: ExternalApiClient):
        self.client = client

    def list_films(
        self,
        page: int = 1,
        page_size: int = 10,
        title: Optional[str] = None
    ) -> PaginatedFilmsResponse:
        
        swapi_params = {"page": page}

        if title:
            swapi_params["search"] = title

        response = self.client.get("films", params=swapi_params)
        results = response.get("results", [])

        start = 0
        end = page_size

        return PaginatedFilmsResponse(
            page=page,
            page_size=page_size,
            total=response.get("count", 0),
            results=results[start:end]
        )

    def get_film_by_id(self, film_id: int) -> FilmResponse:
        try:
            response = self.client.get(f"films/{film_id}")
            return FilmResponse(**response)
        except Exception as e:
            raise HTTPException(
                status_code=404,
                detail=f"Filme {film_id} não encontrado"
            )

    def get_film_characters(self, film_id: int) -> List[FilmCharacterResponse]:
        film = self.get_film_by_id(film_id)
        characters = []

        for character_url in film.characters:
            character_id = character_url.rstrip('/').split('/')[-1]
            try:
                character = self.client.get(f"people/{character_id}")
                characters.append(FilmCharacterResponse(
                    name=character.get("name"),
                    gender=character.get("gender"),
                    birth_year=character.get("birth_year")
                ))
            except:
                continue

        return characters

    def get_film_planets(self, film_id: int) -> List[FilmPlanetResponse]:
        film = self.get_film_by_id(film_id)
        planets = []

        for planet_url in film.planets:
            planet_id = planet_url.rstrip('/').split('/')[-1]
            try:
                planet = self.client.get(f"planets/{planet_id}")
                planets.append(FilmPlanetResponse(
                    name=planet.get("name"),
                    climate=planet.get("climate"),
                    terrain=planet.get("terrain"),
                    population=planet.get("population")
                ))
            except:
                continue

        return planets

    def get_film_starships(self, film_id: int) -> List[FilmStarshipResponse]:
        film = self.get_film_by_id(film_id)
        starships = []

        for starship_url in film.starships:
            starship_id = starship_url.rstrip('/').split('/')[-1]
            try:
                starship = self.client.get(f"starships/{starship_id}")
                starships.append(FilmStarshipResponse(
                    name=starship.get("name"),
                    model=starship.get("model"),
                    starship_class=starship.get("starship_class"),
                    manufacturer=starship.get("manufacturer")
                ))
            except:
                continue

        return starships

    def get_film_summary(self, film_id: int) -> FilmSummaryResponse:
        film = self.get_film_by_id(film_id)
        
        return FilmSummaryResponse(
            title=film.title,
            episode_id=film.episode_id,
            director=film.director,
            release_date=film.release_date,
            total_characters=len(film.characters),
            total_planets=len(film.planets),
            total_starships=len(film.starships),
            total_vehicles=len(film.vehicles),
            total_species=len(film.species)
        )

    def list_films_by_episode_order(self) -> List[FilmResponse]:
        response = self.client.get("films")
        results = response.get("results", [])
        
        # Ordena por episode_id
        sorted_films = sorted(results, key=lambda x: x.get("episode_id", 0))
        
        return [FilmResponse(**film) for film in sorted_films]