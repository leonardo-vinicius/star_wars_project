from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import date


class FilmBase(BaseModel):
    title: str
    episode_id: int
    opening_crawl: str
    director: str
    producer: str
    release_date: str
    characters: List[str] = []
    planets: List[str] = []
    starships: List[str] = []
    vehicles: List[str] = []
    species: List[str] = []
    created: str
    edited: str
    url: str


class FilmResponse(FilmBase):
    pass


class PaginatedFilmsResponse(BaseModel):
    page: int
    page_size: int
    total: int
    results: List[FilmBase]


class FilmCharacterResponse(BaseModel):
    name: str
    gender: str
    birth_year: str


class FilmPlanetResponse(BaseModel):
    name: str
    climate: str
    terrain: str
    population: str


class FilmStarshipResponse(BaseModel):
    name: str
    model: str
    starship_class: str
    manufacturer: str


class FilmSummaryResponse(BaseModel):
    title: str
    episode_id: int
    director: str
    release_date: str
    total_characters: int
    total_planets: int
    total_starships: int
    total_vehicles: int
    total_species: int