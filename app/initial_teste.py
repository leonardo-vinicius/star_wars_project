from integrations.api_client import ExternalApiClient
from services.starwars_service import StarWarsDataService

api_client = ExternalApiClient(base_url="https://swapi.dev/api")
starwars_service = StarWarsDataService(api_client)

data = starwars_service.list_people()
print(data)