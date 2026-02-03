from typing import Dict, Any, Optional, List
from integrations.swapi.client import ExternalApiClient
from fastapi import HTTPException


class PeopleService:
    def __init__(self, client: ExternalApiClient):
        self.client = client

    def list_people(
        self,
        page: int = 1,
        page_size: int = 10,
        name: Optional[str] = None
    ) -> Dict[str, Any]:


        swapi_params = {"page": page}

        if name:
            swapi_params["search"] = name

        response = self.client.get("people", params=swapi_params)
        results = response.get("results", [])

        start = 0
        end = page_size

        return {
            "page": page,
            "page_size": page_size,
            "total": response.get("count"),
            "results": results[start:end]
        }
    
    def get_person_by_id(self, person_id: int) -> Dict[str, Any]:
        try:
            response = self.client.get(f"people/{person_id}")
            return response
        except Exception as e:
            raise HTTPException(status_code=404, detail=f"Personagem {person_id} não encontrado")
