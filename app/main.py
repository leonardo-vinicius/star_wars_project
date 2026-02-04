from fastapi import FastAPI
from domains.people.router import router as people_router
from domains.starships.router import router as starship_router
from domains.films.router import router as films_router
from domains.planets.router import router as planets_router
from domains.users.router import router as user_router


app = FastAPI(
    title="Star Wars API",
    description="API para consumo de dados do universo Star Wars",
    version="1.0.0"
)

app.include_router(people_router)
app.include_router(starship_router)
app.include_router(films_router)
app.include_router(planets_router)
app.include_router(user_router)

@app.get("/health")
def health_check():
    return {"status": "ok"}
