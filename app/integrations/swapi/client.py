import requests
from typing import Dict, Any, Optional


class ExternalApiClient:
    def __init__(self, base_url: str, timeout: int = 10):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def get(
        self,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"

        try:
            response = requests.get(
                url,
                params=params,
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()

        except requests.exceptions.Timeout:
            raise RuntimeError("Timeout ao acessar serviço externo")

        except requests.exceptions.HTTPError as exc:
            raise RuntimeError(
                f"Erro HTTP {exc.response.status_code} ao acessar serviço externo"
            )

        except requests.exceptions.RequestException:
            raise RuntimeError("Erro de comunicação com serviço externo")
