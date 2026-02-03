from fastapi import APIRouter, Depends, Query, HTTPException
from typing import Optional, List

from domains.starships.service import StarshipsService
from domains.starships.models import (
    PaginatedStarshipsResponse,
    StarshipResponse,
    StarshipPilotResponse,
    StarshipFilmResponse
)
from integrations.swapi.client import ExternalApiClient

router = APIRouter(
    prefix="/starships",
    tags=["Starships"]
)


def get_starships_service() -> StarshipsService:
    client = ExternalApiClient(base_url="https://swapi.dev/api")
    return StarshipsService(client)


@router.get("/", response_model=PaginatedStarshipsResponse)
def list_starships(
    page: int = Query(1, ge=1, description="Número da página"),
    page_size: int = Query(10, ge=1, le=100, description="Itens por página"),
    name: Optional[str] = Query(None, description="Filtrar por nome da nave"),
    service: StarshipsService = Depends(get_starships_service)
):
    return service.list_starships(page, page_size, name)


@router.get("/{starship_id}", response_model=StarshipResponse)
def get_starship_by_id(
    starship_id: int,
    service: StarshipsService = Depends(get_starships_service)
):
    return service.get_starship_by_id(starship_id)


@router.get("/{starship_id}/pilots", response_model=List[StarshipPilotResponse])
def get_starship_pilots(
    starship_id: int,
    service: StarshipsService = Depends(get_starships_service)
):
    return service.get_starship_pilots(starship_id)


@router.get("/{starship_id}/films", response_model=List[StarshipFilmResponse])
def get_starship_films(
    starship_id: int,
    service: StarshipsService = Depends(get_starships_service)
):
    return service.get_starship_films(starship_id)