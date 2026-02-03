from fastapi import APIRouter, Depends, Query
from typing import Optional, List

from domains.films.service import FilmsService
from domains.films.models import (
    PaginatedFilmsResponse,
    FilmResponse,
    FilmCharacterResponse,
    FilmPlanetResponse,
    FilmStarshipResponse,
    FilmSummaryResponse
)
from integrations.swapi.client import ExternalApiClient

router = APIRouter(
    prefix="/films",
    tags=["Films"]
)


def get_films_service() -> FilmsService:
    client = ExternalApiClient(base_url="https://swapi.dev/api")
    return FilmsService(client)


@router.get("/", response_model=PaginatedFilmsResponse)
def list_films(
    page: int = Query(1, ge=1, description="Número da página"),
    page_size: int = Query(10, ge=1, le=100, description="Itens por página"),
    title: Optional[str] = Query(None, description="Filtrar por título do filme"),
    service: FilmsService = Depends(get_films_service)
):
    return service.list_films(page, page_size, title)


@router.get("/episode-order", response_model=List[FilmResponse])
def list_films_by_episode_order(
    service: FilmsService = Depends(get_films_service)
):
    return service.list_films_by_episode_order()


@router.get("/{film_id}", response_model=FilmResponse)
def get_film_by_id(
    film_id: int,
    service: FilmsService = Depends(get_films_service)
):
    return service.get_film_by_id(film_id)


@router.get("/{film_id}/summary", response_model=FilmSummaryResponse)
def get_film_summary(
    film_id: int,
    service: FilmsService = Depends(get_films_service)
):
    return service.get_film_summary(film_id)


@router.get("/{film_id}/characters", response_model=List[FilmCharacterResponse])
def get_film_characters(
    film_id: int,
    service: FilmsService = Depends(get_films_service)
):
    return service.get_film_characters(film_id)


@router.get("/{film_id}/planets", response_model=List[FilmPlanetResponse])
def get_film_planets(
    film_id: int,
    service: FilmsService = Depends(get_films_service)
):
    return service.get_film_planets(film_id)


@router.get("/{film_id}/starships", response_model=List[FilmStarshipResponse])
def get_film_starships(
    film_id: int,
    service: FilmsService = Depends(get_films_service)
):
    return service.get_film_starships(film_id)