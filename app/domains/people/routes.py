from fastapi import APIRouter, Depends, Query
from typing import Optional

from domains.people.service import PeopleService
from integrations.swapi.client import ExternalApiClient

router = APIRouter(
    prefix="/people",
    tags=["People"]
)


def get_people_service() -> PeopleService:
    client = ExternalApiClient(base_url="https://swapi.dev/api")
    return PeopleService(client)


@router.get("/")
def list_people(
    page: int = 1,
    page_size: int = 10,
    name: Optional[str] = None,
    service: PeopleService = Depends(get_people_service)
):
    return service.list_people(page, page_size, name)


@router.get("/{person_id}")
def get_person_by_id(
    person_id: int,
    service: PeopleService = Depends(get_people_service)
):
    return service.get_person_by_id(person_id)