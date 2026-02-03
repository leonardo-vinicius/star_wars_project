import requests
from typing import Dict, Any, Optional, Tuple
from functools import lru_cache

@lru_cache(maxsize=128)
def cached_get(
    base_url: str,
    endpoint: str,
    params: Tuple[Tuple[str, Any], ...],
    timeout: int
) -> Dict[str, Any]:
    url = f"{base_url}/{endpoint.strip('/')}/"

    response = requests.get(
        url,
        params=dict(params),
        timeout=timeout
    )

    response.raise_for_status()
    return response.json()

class ExternalApiClient:
    def __init__(self, base_url: str, timeout: int = 10):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def get(
        self,
        endpoint: str,
        params: Dict[str, Any] | None = None
    ) -> Dict[str, Any]:

        params_tuple = tuple(sorted(params.items())) if params else ()

        try:
            return cached_get(
                self.base_url,
                endpoint,
                params_tuple,
                self.timeout
            )

        except requests.exceptions.HTTPError as exc:
            raise RuntimeError(
                f"Erro HTTP {exc.response.status_code} ao acessar serviço externo"
            )

        except requests.exceptions.RequestException:
            raise RuntimeError("Erro de comunicação com serviço externo")