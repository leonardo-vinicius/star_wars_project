from typing import Optional, List, Dict, Any
from integrations.swapi.client import ExternalApiClient
from domains.planets.models import (
    PaginatedPlanetsResponse,
    PlanetResponse,
    PlanetResidentResponse,
    PlanetFilmResponse,
    PlanetSummaryResponse,
    PlanetComparisonResponse
)
from fastapi import HTTPException


class PlanetsService:
    def __init__(self, client: ExternalApiClient):
        self.client = client

    def list_planets(
        self,
        page: int = 1,
        page_size: int = 10,
        name: Optional[str] = None,
        climate: Optional[str] = None,
        terrain: Optional[str] = None,
        population_min: Optional[int] = None
    ) -> PaginatedPlanetsResponse:
        """Lista todos os planetas com paginação e filtros opcionais"""
        
        swapi_params = {"page": page}

        if name:
            swapi_params["search"] = name

        response = self.client.get("planets", params=swapi_params)
        results = response.get("results", [])

        if climate:
            results = [
                planet for planet in results
                if climate.lower() in planet.get("climate", "").lower()
            ]
        
        if terrain:
            results = [
                planet for planet in results
                if terrain.lower() in planet.get("terrain", "").lower()
            ]
        
        if population_min is not None:
            results = [
                planet for planet in results
                if planet.get("population", "unknown").isdigit() 
                and int(planet.get("population")) >= population_min
            ]

        start = 0
        end = page_size

        return PaginatedPlanetsResponse(
            page=page,
            page_size=page_size,
            total=len(results),
            results=results[start:end]
        )

    def get_planet_by_id(self, planet_id: int) -> PlanetResponse:
        try:
            response = self.client.get(f"planets/{planet_id}")
            return PlanetResponse(**response)
        except Exception as e:
            raise HTTPException(
                status_code=404,
                detail=f"Planeta {planet_id} não encontrado"
            )

    def get_planet_residents(self, planet_id: int) -> List[PlanetResidentResponse]:
        planet = self.get_planet_by_id(planet_id)
        residents = []

        for resident_url in planet.residents:
            resident_id = resident_url.rstrip('/').split('/')[-1]
            try:
                resident = self.client.get(f"people/{resident_id}")
                residents.append(PlanetResidentResponse(
                    name=resident.get("name"),
                    birth_year=resident.get("birth_year"),
                    gender=resident.get("gender"),
                    species=resident.get("species", [])
                ))
            except:
                continue

        return residents

    def get_planet_films(self, planet_id: int) -> List[PlanetFilmResponse]:
        planet = self.get_planet_by_id(planet_id)
        films = []

        for film_url in planet.films:
            film_id = film_url.rstrip('/').split('/')[-1]
            try:
                film = self.client.get(f"films/{film_id}")
                films.append(PlanetFilmResponse(
                    title=film.get("title"),
                    episode_id=film.get("episode_id"),
                    release_date=film.get("release_date"),
                    director=film.get("director")
                ))
            except:
                continue

        return films

    def get_planet_summary(self, planet_id: int) -> PlanetSummaryResponse:
        planet = self.get_planet_by_id(planet_id)
        
        return PlanetSummaryResponse(
            name=planet.name,
            climate=planet.climate,
            terrain=planet.terrain,
            population=planet.population,
            diameter=planet.diameter,
            gravity=planet.gravity,
            total_residents=len(planet.residents),
            total_films=len(planet.films)
        )

    def search_planets_by_climate(self, climate: str) -> List[PlanetResponse]:
        all_planets = []
        page = 1
        
        while True:
            try:
                response = self.client.get("planets", params={"page": page})
                results = response.get("results", [])
                
                if not results:
                    break
                
                filtered = [
                    planet for planet in results
                    if climate.lower() in planet.get("climate", "").lower()
                ]
                
                all_planets.extend([PlanetResponse(**planet) for planet in filtered])
                
                if not response.get("next"):
                    break
                    
                page += 1
            except:
                break
        
        return all_planets

    def search_planets_by_terrain(self, terrain: str) -> List[PlanetResponse]:
        all_planets = []
        page = 1
        
        while True:
            try:
                response = self.client.get("planets", params={"page": page})
                results = response.get("results", [])
                
                if not results:
                    break
                
                filtered = [
                    planet for planet in results
                    if terrain.lower() in planet.get("terrain", "").lower()
                ]
                
                all_planets.extend([PlanetResponse(**planet) for planet in filtered])
                
                if not response.get("next"):
                    break
                    
                page += 1
            except:
                break
        
        return all_planets

    def compare_planets(self, planet_ids: List[int]) -> List[PlanetComparisonResponse]:
        comparisons = []
        
        for planet_id in planet_ids:
            try:
                planet = self.get_planet_by_id(planet_id)
                comparisons.append(PlanetComparisonResponse(
                    planet_name=planet.name,
                    diameter=planet.diameter,
                    population=planet.population,
                    climate=planet.climate,
                    terrain=planet.terrain,
                    gravity=planet.gravity
                ))
            except:
                continue
        
        return comparisons