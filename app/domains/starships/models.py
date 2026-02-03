from pydantic import BaseModel, Field
from typing import List, Optional


class StarshipBase(BaseModel):
    name: str
    model: str
    manufacturer: str
    cost_in_credits: str
    length: str
    max_atmosphering_speed: str
    crew: str
    passengers: str
    cargo_capacity: str
    consumables: str
    hyperdrive_rating: str
    MGLT: str
    starship_class: str
    pilots: List[str] = []
    films: List[str] = []
    created: str
    edited: str
    url: str


class StarshipResponse(StarshipBase):
    pass


class PaginatedStarshipsResponse(BaseModel):
    page: int
    page_size: int
    total: int
    results: List[StarshipBase]


class StarshipPilotResponse(BaseModel):
    name: str
    birth_year: str
    gender: str


class StarshipFilmResponse(BaseModel):
    title: str
    episode_id: int
    release_date: str