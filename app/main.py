from fastapi import FastAPI
from domains.people.routes import router as people_router


app = FastAPI(
    title="Star Wars API",
    description="API para consumo de dados do universo Star Wars",
    version="1.0.0"
)

app.include_router(people_router)

@app.get("/health")
def health_check():
    return {"status": "ok"}
