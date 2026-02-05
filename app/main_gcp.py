from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

# Importar os routers
from domains.users.router import router as users_router
from domains.people.router import router as people_router
from domains.starships.router import router as starships_router
from domains.films.router import router as films_router
from domains.planets.router import router as planets_router

app = FastAPI(
    title="Star Wars API",
    description="API para explorar o universo Star Wars no GCP",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_router)
app.include_router(people_router)
app.include_router(starships_router)
app.include_router(films_router)
app.include_router(planets_router)

@app.get("/")
def root():
    return {
        "message": "Star Wars API on GCP",
        "docs": "/docs",
        "github": "https://github.com/leonardo-vinicius/star_wars_project.git"
    }

handler = Mangum(app)

def starwars_api(request):
    return handler(request)