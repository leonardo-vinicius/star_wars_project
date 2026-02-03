from pydantic import BaseModel, Field
from typing import List, Optional


class PlanetBase(BaseModel):
    name: str
    rotation_period: str
    orbital_period: str
    diameter: str
    climate: str
    gravity: str
    terrain: str
    surface_water: str
    population: str
    residents: List[str] = []
    films: List[str] = []
    created: str
    edited: str
    url: str


class PlanetResponse(PlanetBase):
    pass


class PaginatedPlanetsResponse(BaseModel):
    page: int
    page_size: int
    total: int
    results: List[PlanetBase]


class PlanetResidentResponse(BaseModel):
    name: str
    birth_year: str
    gender: str
    species: List[str] = []


class PlanetFilmResponse(BaseModel):
    title: str
    episode_id: int
    release_date: str
    director: str


class PlanetSummaryResponse(BaseModel):
    name: str
    climate: str
    terrain: str
    population: str
    diameter: str
    gravity: str
    total_residents: int
    total_films: int


class PlanetComparisonResponse(BaseModel):
    planet_name: str
    diameter: str
    population: str
    climate: str
    terrain: str
    gravity: str