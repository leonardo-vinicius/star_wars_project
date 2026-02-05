from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from domains.people.router import router as people_router
from domains.starships.router import router as starships_router
from domains.films.router import router as films_router
from domains.planets.router import router as planets_router

app = FastAPI(
    title="Star Wars API",
    description="API do universo Star Wars",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(people_router)
app.include_router(starships_router)
app.include_router(films_router)
app.include_router(planets_router)

@app.get("/")
def root():
    return {
        "message": "Star Wars API",
        "status": "running",
        "docs": "/docs",
        "version": "1.0.0"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}