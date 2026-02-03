from pydantic import BaseModel, Field
from typing import List, Optional


class PersonBase(BaseModel):
    name: str
    height: str
    mass: str
    hair_color: str
    skin_color: str
    eye_color: str
    birth_year: str
    gender: str
    homeworld: str
    films: List[str] = []
    species: List[str] = []
    vehicles: List[str] = []
    starships: List[str] = []
    url: str
    created: str
    edited: str


class PersonResponse(PersonBase):
    pass


class PaginatedPeopleResponse(BaseModel):
    page: int
    page_size: int
    total: int
    results: List[PersonBase]


class PersonFilmResponse(BaseModel):
    title: str
    episode_id: int
    release_date: str