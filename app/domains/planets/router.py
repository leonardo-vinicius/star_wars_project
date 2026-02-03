from fastapi import APIRouter, Depends, Query
from typing import Optional, List

from domains.planets.service import PlanetsService
from domains.planets.models import (
    PaginatedPlanetsResponse,
    PlanetResponse,
    PlanetResidentResponse,
    PlanetFilmResponse,
    PlanetSummaryResponse,
    PlanetComparisonResponse
)
from integrations.swapi.client import ExternalApiClient

router = APIRouter(
    prefix="/planets",
    tags=["Planets"]
)


def get_planets_service() -> PlanetsService:
    client = ExternalApiClient(base_url="https://swapi.dev/api")
    return PlanetsService(client)


@router.get("/", response_model=PaginatedPlanetsResponse)
def list_planets(
    page: int = Query(1, ge=1, description="Número da página"),
    page_size: int = Query(10, ge=1, le=100, description="Itens por página"),
    name: Optional[str] = Query(None, description="Filtrar por nome do planeta"),
    service: PlanetsService = Depends(get_planets_service)
):
    return service.list_planets(page, page_size, name)


@router.get("/search/climate", response_model=List[PlanetResponse])
def search_planets_by_climate(
    climate: str = Query(..., description="Tipo de clima (ex: arid, temperate, frozen)"),
    service: PlanetsService = Depends(get_planets_service)
):
    return service.search_planets_by_climate(climate)


@router.get("/search/terrain", response_model=List[PlanetResponse])
def search_planets_by_terrain(
    terrain: str = Query(..., description="Tipo de terreno (ex: desert, forest, ocean)"),
    service: PlanetsService = Depends(get_planets_service)
):
    return service.search_planets_by_terrain(terrain)


@router.get("/compare", response_model=List[PlanetComparisonResponse])
def compare_planets(
    planet_ids: List[int] = Query(..., description="Lista de IDs de planetas para comparar"),
    service: PlanetsService = Depends(get_planets_service)
):
    return service.compare_planets(planet_ids)


@router.get("/{planet_id}", response_model=PlanetResponse)
def get_planet_by_id(
    planet_id: int,
    service: PlanetsService = Depends(get_planets_service)
):
    return service.get_planet_by_id(planet_id)


@router.get("/{planet_id}/summary", response_model=PlanetSummaryResponse)
def get_planet_summary(
    planet_id: int,
    service: PlanetsService = Depends(get_planets_service)
):
    return service.get_planet_summary(planet_id)


@router.get("/{planet_id}/residents", response_model=List[PlanetResidentResponse])
def get_planet_residents(
    planet_id: int,
    service: PlanetsService = Depends(get_planets_service)
):
    return service.get_planet_residents(planet_id)


@router.get("/{planet_id}/films", response_model=List[PlanetFilmResponse])
def get_planet_films(
    planet_id: int,
    service: PlanetsService = Depends(get_planets_service)
):
    return service.get_planet_films(planet_id)