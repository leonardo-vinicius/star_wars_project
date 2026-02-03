from fastapi import APIRouter, Depends, Query, HTTPException
from typing import Optional

from domains.people.service import PeopleService
from domains.people.models import (
    PaginatedPeopleResponse,
    PersonResponse
)
from integrations.swapi.client import ExternalApiClient

router = APIRouter(
    prefix="/people",
    tags=["People"]
)


def get_people_service() -> PeopleService:
    client = ExternalApiClient(base_url="https://swapi.dev/api")
    return PeopleService(client)


@router.get("/", response_model=PaginatedPeopleResponse)
def list_people(
    page: int = Query(1, ge=1, description="Número da página"),
    page_size: int = Query(10, ge=1, le=100, description="Itens por página"),
    name: Optional[str] = Query(None, description="Filtrar por nome"),
    service: PeopleService = Depends(get_people_service)
):
    return service.list_people(page, page_size, name)


@router.get("/{person_id}", response_model=PersonResponse)
def get_person_by_id(
    person_id: int,
    service: PeopleService = Depends(get_people_service)
):
    try:
        return service.get_person_by_id(person_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Personagem {person_id} não encontrado")