from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database.connection import init_db
from domains.users.router import router as users_router
from domains.people.router import router as people_router
from domains.starships.router import router as starships_router
from domains.films.router import router as films_router
from domains.planets.router import router as planets_router

app = FastAPI(
    title="Star Wars API",
    description="API para explorar o universo Star Wars",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    init_db()


app.include_router(users_router)
app.include_router(people_router)
app.include_router(starships_router)
app.include_router(films_router)
app.include_router(planets_router)


@app.get("/")
def root():
    return {
        "message": "Star Wars API",
        "docs": "/docs"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)